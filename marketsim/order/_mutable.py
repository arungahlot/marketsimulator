from marketsim import _, event, Event, types

from _cancel import Cancel

from _limit import Limit

class Base(types.IOrder):
    """ Meta order with mutable parameters
        User should provide an observable that generates new parameters for the order
    """
    
    def __init__(self, source, factory):
        self._order = None
        self.source = source
        self.factory = factory
        self.on_matched = Event()
        self.on_charged = Event()
        self.on_cancelled = Event()
        
    def processIn(self, orderBook):
        self.orderBook = orderBook 
        self.source += _(self)._update
        self._update(None)
        
    def _dispose(self):
        if self._order is not None:
            self._onMatched.dispose()
            self._onCancelled.dispose()
            self._onCharged.dispose()
            self.orderBook.process(Cancel(self._order))
        
    def _update(self, dummy):
        self._dispose()
        params = self.source()
        if params is not None:
            self._order = self.factory(*params)
            self._onMatched = event.subscribe(self._order.on_matched, 
                                              self.on_matched.fire, self, {}) 
            self._onCancelled = event.subscribe(self._order.on_cancelled, 
                                              self.on_cancelled.fire, self, {})
            self._onCharged = event.subscribe(self._order.on_charged, 
                                              self.on_charged.fire, self, {})
            self.orderBook.process(self._order)
            
    @property
    def side(self):
        return self._order.side
        
    def __str__(self):
        if self._order is not None:
            return type(self).__name__ + "("+str(self.side)+", volume=" + str(self.volume) \
                    + ", P&L="+str(self.PnL)+")"
        else:
            return "MutableOrder"

    def __repr__(self):
        return self.__str__()

    @property
    def signedPrice(self):
        """ Returns "signed" price of the order:
        positive if the order is on sell side
        negative if the order is on buy side 
        """
        return self._order.signedPrice

    @property
    def price(self):
        """ Limit price of the order
        """
        return self._order.price

    @property
    def volume(self):
        """ Volume to trade
        """
        return self._order.volume

    @property
    def signedVolume(self):
        return self._order.signedVolume
    
    @property 
    def PnL(self):
        """ P&L of the order. 
        positive, if it is a sell side order
        negative, if it is a buy side order
        """
        return self._order.PnL

    @property
    def empty(self):
        """ Volume is empty iff its volume is 0
        """
        return self._order.empty

    @property
    def cancelled(self):
        """ Is order cancelled
        """
        return self._order.cancelled
    

    def cancel(self):
        """ Marks order as cancelled. Notifies the order book about it
        """
        self._dispose()
        self.source -= _(self)._update
        self.on_cancelled.fire(self)

    def __hash__(self):
        return id(self)
    
class SidePriceVolume(Base):
    
    _properties = { 
        'source' : types.IObservable[types.SidePriceVolume],
        'factory': types.IOrderFactory[types.SidePriceVolume] 
    }
    
import factory
    
def Mutable(source, f = factory.limit):
    
    if source.T == types.SidePriceVolume:
        return SidePriceVolume(source, f[source.T])
    
    return None