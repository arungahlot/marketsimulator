from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim import meta
#(.Float,.Float,.Float,.IOrderBook) => (() => .Side)
class IFunctionIFunctionSidefloatfloatfloatIOrderBook(object):
    _types = [meta.function((float,float,float,IOrderBook,),IFunctionSide)]
    
    pass


