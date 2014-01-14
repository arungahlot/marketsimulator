type Optional[T]

type Side
type String

type Boolean
type Float
type Int : Float

type Volume : Int
type Price : Float

type IOrderQueue
type IOrderBook

type IFunction[T] = () => T

type IEvent
type IObservable[U] : IFunction[U], IEvent

type IOrderGenerator = IObservable[Order]

type IAccount
type ISingleAssetTrader : IAccount

type IDifferentiable : IFunction[Float]

type CandleStick
type VolumeLevels
type Order

type ISingleAssetStrategy
type IMultiAssetStrategy

