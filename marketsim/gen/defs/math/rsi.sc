package math
{
    /**
     *  Observable that adds a lag to an observable data source so [Lagged(x, dt)]t=t0 == [x]t=t0+dt
     */
    @python.intrinsic("observable.lagged.Lagged_Impl")
    @label = "Lagged_{%(timeframe)s}(%(source)s)"
    def Lagged (/** observable data source */   source = const (1.),
                /** lag size */                 timeframe = 10.0) : IObservable[Float]

    /**
     *  Returns positive movements of some observable *source* with lag *timeframe*
     */
    @label = "Ups_{%(timeframe)s}(%(source)s)"
    def UpMovements(/** observable data source */   source = const (1.),
                    /** lag size */                 timeframe = 10.0)

        = Max(0.0, source - source~>Lagged(timeframe))

    /**
     *  Returns negative movements of some observable *source* with lag *timeframe*
     */
    @label = "Downs_{%(timeframe)s}(%(source)s)"
    def DownMovements(  /** observable data source */   source = const (1.),
                        /** lag size */                 timeframe = 10.0)

        = Max(0.0, source~>Lagged(timeframe) - source)

    @category = "RSI"
    package rsi
    {
        /**
         *  Absolute value for Relative Strength Index
         */
        @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
        @method = "rsi_Raw"
        def Raw(/** observable data source */   source      = const (1.),
                /** lag size */                 timeframe   = 10.0,
                /** alpha parameter for EWMA */ alpha       = 0.015)

            =   source~>UpMovements  (timeframe)~>EW(alpha)~>Avg /
                source~>DownMovements(timeframe)~>EW(alpha)~>Avg
    }

    /**
     *  Relative Strength Index
     */
    @label = "RSI_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
    def RSI(    /** observable data source */   source      = const (1.),
                /** lag size */                 timeframe   = 10.0,
                /** alpha parameter for EWMA */ alpha       = 0.015)

        = 100.0 - 100.0 / (1.0 + source~>rsi_Raw(timeframe, alpha))

    /**
     *  Log returns
     */
    @label = "LogReturns_{%(timeframe)s}(%(x)s)"
    def LogReturns(/** observable data source */   x = const(1.),
                   /** lag size */                 timeframe   = 10.0)

        =  Log(x / x~>Lagged(timeframe))
}