from marketsim import registry, types, event
import math
from _all import Observable, Constant

@registry.expose(['Trigonometric', 'Atan'])
class Atan(Observable[float]):
    """ 
    """ 
    def __init__(self, x  = const(0.0)):
        Observable[float].__init__(self)
        self.x = x
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)

    @property
    def label(self):
        return repr(self)

    _properties = {
        'x' : types.IFunction[float]
    }

    def __repr__(self):
        return "atan(%(x)s)" % self.__dict__


    def __call__(self, *args, **kwargs):
        x = self.x()
        if x is None: return None
        return math.atan(self.x)


