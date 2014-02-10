from marketsim import IObservable
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Statistics", "StdDev"])
class StdDev_IObservableFloatFloat(Function[float]):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        self.source = source if source is not None else _const(1.0)
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'alpha' : float
    }
    def __repr__(self):
        return "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}(%(source)s)}" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.math._sqrt import Sqrt_IFunctionFloat as _math_Sqrt
        from marketsim.gen._out.math.EW._var import Var_IObservableFloatFloat as _math_EW_Var
        return _math_Sqrt(_math_EW_Var(self.source,self.alpha))
    
def StdDev(source = None,alpha = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[float]):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return StdDev_IObservableFloatFloat(source,alpha)
    raise Exception("Cannot find suitable overload")
