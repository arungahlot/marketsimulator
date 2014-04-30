# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.observable.breaks_at_changes import BreaksAtChanges_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Basic", "BreaksAtChanges"])
class BreaksAtChanges_IObservableFloat(Observablefloat,BreaksAtChanges_Impl):
    """ **Observable listening to *source***
    
      When *source* changes it inserts *undefined* value and then immidiately becomes equal to *source* value
    
    Parameters are:
    
    **source**
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.source = source if source is not None else deref_opt(_const_Float(1.0))
        rtti.check_fields(self)
        BreaksAtChanges_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat
    }
    
    
    def on_source_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'source', value)
    
    def __repr__(self):
        return "BreaksAtChanges(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.source.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def BreaksAtChanges(source = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        return BreaksAtChanges_IObservableFloat(source)
    raise Exception('Cannot find suitable overload for BreaksAtChanges('+str(source) +':'+ str(type(source))+')')
