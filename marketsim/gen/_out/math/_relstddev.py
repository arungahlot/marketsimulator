# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.math._cumulative import Cumulative
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_mathCumulative(Observablefloat):
    """ **Relative standard deviation**
    
    
    Parameters are:
    
    **x**
    """ 
    def __init__(self, x = None):
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.math._cumulative import Cumulative_IObservableFloat as _math_Cumulative_IObservableFloat
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_Cumulative_IObservableFloat())
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative
    }
    
    
    def __repr__(self):
        return "RelStdDev(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.math._cumulative import Cumulative
        rtti.typecheck(Cumulative, self.x)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.impl.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
    def getImpl(self):
        from marketsim.gen._out.math._stddev import StdDev_mathCumulative as _math_StdDev_mathCumulative
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatFloat as _ops_Sub_IObservableFloatFloat
        from marketsim.gen._out.math._source import Source_mathCumulative as _math_Source_mathCumulative
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.math._avg import Avg_mathCumulative as _math_Avg_mathCumulative
        from marketsim import deref_opt
        return deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_ops_Sub_IObservableFloatFloat(deref_opt(_math_Source_mathCumulative(self.x)),deref_opt(_math_Avg_mathCumulative(self.x)))),deref_opt(_math_StdDev_mathCumulative(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.math._ew import EW
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_mathEW(Observablefloat):
    """ **Relative standard deviation**
    
    
    Parameters are:
    
    **x**
    """ 
    def __init__(self, x = None):
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_EW_IObservableFloatFloat())
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : EW
    }
    
    
    def __repr__(self):
        return "RelStdDev(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.math._ew import EW
        rtti.typecheck(EW, self.x)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.impl.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
    def getImpl(self):
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatFloat as _ops_Sub_IObservableFloatFloat
        from marketsim.gen._out.math._source import Source_mathEW as _math_Source_mathEW
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.math._stddev import StdDev_mathEW as _math_StdDev_mathEW
        from marketsim import deref_opt
        return deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_ops_Sub_IObservableFloatFloat(deref_opt(_math_Source_mathEW(self.x)),deref_opt(_math_Avg_mathEW(self.x)))),deref_opt(_math_StdDev_mathEW(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.math._moving import Moving
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_mathMoving(Observablefloat):
    """ **Relative standard deviation**
    
    
    Parameters are:
    
    **x**
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._moving import Moving_IObservableFloatFloat as _math_Moving_IObservableFloatFloat
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_Moving_IObservableFloatFloat())
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    
    
    def __repr__(self):
        return "RelStdDev(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.math._moving import Moving
        rtti.typecheck(Moving, self.x)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.impl.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
    def getImpl(self):
        from marketsim.gen._out.math._source import Source_mathMoving as _math_Source_mathMoving
        from marketsim.gen._out.math._stddev import StdDev_mathMoving as _math_StdDev_mathMoving
        from marketsim.gen._out.math._avg import Avg_mathMoving as _math_Avg_mathMoving
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatFloat as _ops_Sub_IObservableFloatFloat
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_ops_Sub_IObservableFloatFloat(deref_opt(_math_Source_mathMoving(self.x)),deref_opt(_math_Avg_mathMoving(self.x)))),deref_opt(_math_StdDev_mathMoving(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def RelStdDev(x = None): 
    from marketsim.gen._out.math._cumulative import Cumulative
    from marketsim.gen._out.math._ew import EW
    from marketsim.gen._out.math._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Cumulative):
        return RelStdDev_mathCumulative(x)
    if x is None or rtti.can_be_casted(x, EW):
        return RelStdDev_mathEW(x)
    if x is None or rtti.can_be_casted(x, Moving):
        return RelStdDev_mathMoving(x)
    raise Exception('Cannot find suitable overload for RelStdDev('+str(x) +':'+ str(type(x))+')')
