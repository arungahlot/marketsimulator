from marketsim import types, Side, ops
from marketsim.types import *

from _market import Market as MarketOrder
from _limit import Limit as LimitOrder, LimitOrderFactory

def correct_volume(x):
    return None if x is None or abs(x) < 1 else int(x)
    
def correct_price(x):
    return x
    
def correct_side(x):
    return x

class Market_Base(types.IOrderGenerator):
    
    def __call__(self):
        params = self.get()
        return MarketOrder(*params) if params is not None else None

class Market(Market_Base):
    
    def __init__(self, 
                 side = ops.constant(Side.Sell),  
                 volume = ops.constant(1.)):
        self.side = side
        self.volume = volume
        
    _properties = { 
        'side'      : types.IFunction[Side],
        'volume'    : types.IFunction[float]
    }
        
    def get(self):
        side = correct_side(self.side())
        if side is None:
            return None
        volume = correct_volume(self.volume())
        if volume is None:
            return None
        return (side, volume)
    
class MarketSigned(Market_Base):
    
    def __init__(self, signedVolume = ops.constant(1.)):
        self.signedVolume = signedVolume

    _properties = { 
        'signedVolume'    : types.IFunction[float]
    }
        
    def get(self):
        signedVolume = correct_volume(self.signedVolume())
        if signedVolume is None:
            return None
        side = Side.Buy if signedVolume > 0 else Side.Sell
        return (side, abs(signedVolume))

class SignedVolume_Market(IFunction[IOrderGenerator, SignedVolume]):
    
    def __call__(self, signedVolume):
        return MarketSigned(signedVolume)
    
class Side_Market(IFunction[IOrderGenerator, Side]):
    
    def __init__(self, 
                 volume = ops.constant(1.)):
        self.volume = volume
        
    _properties = { 
        'volume'    : types.IFunction[float]
    }
        
    def __call__(self, side):
        return Market(side, self.volume)
    
class Limit(types.IOrderGenerator):
    
    def __init__(self, 
                 side = ops.constant(Side.Sell), 
                 price = ops.constant(100.), 
                 volume = ops.constant(1.)):
        self.side = side
        self.price = price
        self.volume = volume
        
    _properties = { 
        'side'      : types.IFunction[Side],
        'price'     : types.IFunction[float],
        'volume'    : types.IFunction[float],
    }
        
    def __call__(self):
        side = correct_side(self.side())
        if side is None:
            return None
        price = correct_price(self.price())
        if price is None:
            return None
        volume = correct_volume(self.volume())
        if volume is None:
            return None
        return LimitOrder(side, price, volume)
    
limit = {}

limit[types.SidePriceVolume] = LimitOrderFactory()   
    
class SidePrice_Limit(IFunction[IOrderGenerator, SidePrice]):
    
    def __init__(self, volume = ops.constant(1.)):
        self.volume = volume
        
    _properties = { 'volume' : types.IFunction[float] }
    
    def __call__(self, side, price):
        return Limit(side, price, self.volume)