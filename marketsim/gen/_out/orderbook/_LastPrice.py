# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.orderbook.last_price import LastPrice_Impl
from marketsim.gen._out._iorderqueue import IOrderQueue
@registry.expose(["Asset", "LastPrice"])
class LastPrice_IOrderQueue(Observablefloat,LastPrice_Impl):
    """ **Returns last defined price at *queue***
    
      Returns None is *queue* has been always empty
    
    Parameters are:
    
    **queue**
    """ 
    def __init__(self, queue = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.queue = queue if queue is not None else deref_opt(_orderbook_Asks_IOrderBook())
        rtti.check_fields(self)
        LastPrice_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue
    }
    
    
    
    def __repr__(self):
        return "LastPrice(%(queue)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.queue.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def LastPrice(queue = None): 
    from marketsim.gen._out._iorderqueue import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        return LastPrice_IOrderQueue(queue)
    raise Exception('Cannot find suitable overload for LastPrice('+str(queue) +':'+ str(type(queue))+')')
