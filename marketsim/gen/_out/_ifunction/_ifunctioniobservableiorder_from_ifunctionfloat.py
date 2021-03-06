from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctioniorder_from_ifunctionfloat import IFunctionIFunctionIOrder_from_IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionievent_from_ifunctionfloat import IFunctionIEvent_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionfloat import IFunctionobject_from_IFunctionfloat
#(() => .Float) => .IObservable[.IOrder]
class IFunctionIObservableIOrder_from_IFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IObservableIOrder)]
    _types.append(IFunctionobject_from_IFunctionfloat)
    _types.append(IFunctionIFunctionIOrder_from_IFunctionfloat)
    _types.append(IFunctionIEvent_from_IFunctionfloat)
    def price_Iceberg(self, lotSize = None):
        from marketsim.gen._out.order._curried._price_iceberg import price_Iceberg
        return price_Iceberg(self,lotSize)
    
    def price_StopLoss(self, maxloss = None):
        from marketsim.gen._out.order._curried._price_stoploss import price_StopLoss
        return price_StopLoss(self,maxloss)
    
    @property
    def price_ImmediateOrCancel(self):
        from marketsim.gen._out.order._curried._price_immediateorcancel import price_ImmediateOrCancel
        return price_ImmediateOrCancel(self)
    
    @property
    def price_Peg(self):
        from marketsim.gen._out.order._curried._price_peg import price_Peg
        return price_Peg(self)
    
    def price_FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._curried._price_floatingprice import price_FloatingPrice
        return price_FloatingPrice(self,floatingPrice)
    
    def price_WithExpiry(self, expiry = None):
        from marketsim.gen._out.order._curried._price_withexpiry import price_WithExpiry
        return price_WithExpiry(self,expiry)
    
    def FloatingPrice(self, floatingPrice = None):
        from marketsim.gen._out.order._floatingprice import FloatingPrice
        return FloatingPrice(self,floatingPrice)
    
    @property
    def Peg(self):
        from marketsim.gen._out.order._peg import Peg
        return Peg(self)
    
    pass



