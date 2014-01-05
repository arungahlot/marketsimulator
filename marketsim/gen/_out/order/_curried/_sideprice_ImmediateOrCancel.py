from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "ImmediateOrCancel"])
class sideprice_ImmediateOrCancel(IFunction[IOrderGenerator, types.IFunction[Side],IFunction[float]

]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._sideprice_Limit import sideprice_Limit
        self.proto = proto if proto is not None else sideprice_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, types.IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sideprice_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        from marketsim.gen._out.order._ImmediateOrCancel import ImmediateOrCancel
        proto = self.proto
        return ImmediateOrCancel(proto(side,price))
    
