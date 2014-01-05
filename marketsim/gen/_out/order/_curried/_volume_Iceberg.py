from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "Iceberg"])
class volume_Iceberg(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._curried._volume_Limit import volume_Limit
        self.lotSize = lotSize if lotSize is not None else const(10.0)
        self.proto = proto if proto is not None else volume_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IObservable[float],
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "volume_Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out.order._Iceberg import Iceberg
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(lotSize, proto(volume))
    
