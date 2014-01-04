from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
@registry.expose(["Order", "ImmediateOrCancel"])
class side_ImmediateOrCancel(IFunction[IOrderGenerator, types.IFunction[Side]
]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._Limit import side_Limit
        self.proto = proto if proto is not None else side_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, types.IFunction[Side]
        ]
    }
    def __repr__(self):
        return "side_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        proto = self.proto
        return ImmediateOrCancel(proto(side))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "ImmediateOrCancel"])
class price_ImmediateOrCancel(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._Limit import price_Limit
        self.proto = proto if proto is not None else price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "price_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        proto = self.proto
        return ImmediateOrCancel(proto(price))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import types
from marketsim import Side
@registry.expose(["Order", "ImmediateOrCancel"])
class side_price_ImmediateOrCancel(IFunction[IFunction[IOrderGenerator, IFunction[float]], types.IFunction[Side]
]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._Limit import side_price_Limit
        self.proto = proto if proto is not None else side_price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], types.IFunction[Side]
        ]
    }
    def __repr__(self):
        return "side_price_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        proto = self.proto
        return price_ImmediateOrCancel(proto(side))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import Order
@registry.expose(["Order", "ImmediateOrCancel"])
class ImmediateOrCancel(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out.order._Limit import Limit
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.proto = proto if proto is not None else Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IObservable[Order]
        
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.ioc import Order_Impl
        proto = self.proto()
        if proto is None: return None
        
        return Order_Impl(proto)
    

from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "ImmediateOrCancel"])
class volume_ImmediateOrCancel(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._Limit import volume_Limit
        self.proto = proto if proto is not None else volume_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "volume_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        proto = self.proto
        return ImmediateOrCancel(proto(volume))
    
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
        from marketsim.gen._out.order._Limit import sideprice_Limit
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
        proto = self.proto
        return ImmediateOrCancel(proto(side,price))
    
