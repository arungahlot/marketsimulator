from marketsim import request, context, event, _, Event, combine, ops, types
from marketsim.types import *

from _ioc import ImmediateOrCancel

from _meta import *

class FixedBudget(Base):
    
    def __init__(self, side, budget):
        Base.__init__(self, None)
        self.side = side
        self.budget = budget

    def onOrderMatched(self, order, price, volume):
        self.budget -= price*volume
        Base.onOrderMatched(self, order, price, volume)
        
    def onOrderDisposed(self, order):
        self._ordersSent -= 1
        if self._ordersSent == 0:
            self.cancel()
        
    def processIn(self, orderBook):
        self.orderBook = orderBook
        orderBook.process(
                    request.EvalVolumesForBudget(
                                self.side, self.budget, 
                                _(self, orderBook)._onEvaluated))
        
    def _onEvaluated(self, orderBook, pvs):
        self._ordersSent = 0
        self._volumeUnmatched = sum([v for p,v in pvs])
        for p,v in pvs:
            self.send(ImmediateOrCancel(self.side, p, v))
            self._ordersSent += 1
            
    def __repr__(self):
        return 'FixedBudget(%s,%s)' % (self.side, self.budget)
            

class Factory(types.IOrderGenerator, combine.SideBudget):
    
    def bind(self, ctx):
        self._ctx = ctx.context.copy()
        
    def __call__(self):
        params = combine.SideBudget.__call__(self)
        return FixedBudget(*params) if params is not None else None