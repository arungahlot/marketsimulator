from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.strategy.weight import _Score_Impl
from marketsim import IAccount
@registry.expose(["Strategy", "Score"])
class Score(Function[float], _Score_Impl):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy as _observable_trader_SingleProxy
        self.trader = trader if trader is not None else _observable_trader_SingleProxy()
        _Score_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "Score(%(trader)s)" % self.__dict__
    
