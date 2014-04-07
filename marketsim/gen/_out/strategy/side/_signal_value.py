from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.strategy.side._rsibis import RSIbis
from marketsim import context
@registry.expose(["Side function", "Signal_Value"])
class Signal_Value_strategysideRSIbis(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._rsibis import RSIbis_FloatFloatFloat as _strategy_side_RSIbis_FloatFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_RSIbis_FloatFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSIbis
    }
    
    
    def __repr__(self):
        return "Signal_Value(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        from marketsim.gen._out.strategy.side._alpha import Alpha_strategysideRSIbis as _strategy_side_Alpha_strategysideRSIbis
        from marketsim.gen._out.strategy.side._timeframe import Timeframe_strategysideRSIbis as _strategy_side_Timeframe_strategysideRSIbis
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.math._value import Value_mathRSI as _math_Value_mathRSI
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        from marketsim.gen._out.math._rsi import RSI_IObservableFloatFloatFloat as _math_RSI_IObservableFloatFloatFloat
        return deref_opt(_ops_Sub_FloatFloat(deref_opt(_constant_Float(50.0)),deref_opt(_math_Value_mathRSI(deref_opt(_math_RSI_IObservableFloatFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_orderbook_OfTrader_IAccount()))),deref_opt(_strategy_side_Timeframe_strategysideRSIbis(self.x)),deref_opt(_strategy_side_Alpha_strategysideRSIbis(self.x))))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
from marketsim import context
@registry.expose(["Side function", "Signal_Value"])
class Signal_Value_strategysideTrendFollower(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._trendfollower import TrendFollower_FloatFloatIOrderBook as _strategy_side_TrendFollower_FloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_TrendFollower_FloatFloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : TrendFollower
    }
    
    
    def __repr__(self):
        return "Signal_Value(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.side._book import Book_strategysideTrendFollower as _strategy_side_Book_strategysideTrendFollower
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.strategy.side._alpha import Alpha_strategysideTrendFollower as _strategy_side_Alpha_strategysideTrendFollower
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim.gen._out.math._derivative import Derivative_IDifferentiable as _math_Derivative_IDifferentiable
        return deref_opt(_math_Derivative_IDifferentiable(deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_Book_strategysideTrendFollower(self.x)))),deref_opt(_strategy_side_Alpha_strategysideTrendFollower(self.x))))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
from marketsim import context
@registry.expose(["Side function", "Signal_Value"])
class Signal_Value_strategysideCrossingAverages(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages_FloatFloatFloatIOrderBook as _strategy_side_CrossingAverages_FloatFloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_CrossingAverages_FloatFloatFloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : CrossingAverages
    }
    
    
    def __repr__(self):
        return "Signal_Value(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim.gen._out.strategy.side._book import Book_strategysideCrossingAverages as _strategy_side_Book_strategysideCrossingAverages
        from marketsim.gen._out.strategy.side._alpha_1 import Alpha_1_strategysideCrossingAverages as _strategy_side_Alpha_1_strategysideCrossingAverages
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        from marketsim.gen._out.strategy.side._alpha_2 import Alpha_2_strategysideCrossingAverages as _strategy_side_Alpha_2_strategysideCrossingAverages
        return deref_opt(_ops_Sub_FloatFloat(deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_Book_strategysideCrossingAverages(self.x)))),deref_opt(_strategy_side_Alpha_1_strategysideCrossingAverages(self.x)))))),deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_Book_strategysideCrossingAverages(self.x)))),deref_opt(_strategy_side_Alpha_2_strategysideCrossingAverages(self.x))))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.strategy.side._signal import Signal
from marketsim import context
@registry.expose(["Side function", "Signal_Value"])
class Signal_Value_strategysideSignal(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_Signal_FloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Signal
    }
    
    
    def __repr__(self):
        return "Signal_Value(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        from marketsim.gen._out.strategy.side._source import Source_strategysideSignal as _strategy_side_Source_strategysideSignal
        from marketsim import deref_opt
        return deref_opt(_strategy_side_Source_strategysideSignal(self.x))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Signal_Value(x = None): 
    from marketsim import rtti
    from marketsim.gen._out.strategy.side._signal import Signal
    from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
    from marketsim.gen._out.strategy.side._rsibis import RSIbis
    from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
    if x is None or rtti.can_be_casted(x, RSIbis):
        return Signal_Value_strategysideRSIbis(x)
    if x is None or rtti.can_be_casted(x, TrendFollower):
        return Signal_Value_strategysideTrendFollower(x)
    if x is None or rtti.can_be_casted(x, CrossingAverages):
        return Signal_Value_strategysideCrossingAverages(x)
    if x is None or rtti.can_be_casted(x, Signal):
        return Signal_Value_strategysideSignal(x)
    raise Exception('Cannot find suitable overload for Signal_Value('+str(x) +':'+ str(type(x))+')')
