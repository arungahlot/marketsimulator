package generator.python
import predef._

object random extends gen.PythonGenerator
{
    case class Parameter(p : Typed.Parameter) extends base.Parameter

    case class Import(f : Typed.Function) extends base.Printer()
    {
        val name = f.name
        val parameters = f.parameters map Parameter
        val alias = f.docstring.get.brief
        val docstring = f.docstring.get.detailed
        val rv_type = "float"
        override def base_class = s"ops.Function[$rv_type]"
        override val category = "Random"

        type Parameter = random.Parameter

        def casts_to =
            "def _casts_to(self, dst):" |> {
                s"return $name._types[0]._casts_to(dst)"
            }

        val impl_module = "random"

        val prologue =
            "from marketsim import registry, types, ops" |
            "import random" | stop

        override def body = super.body | call | casts_to | nl
    }

    def apply(/** arguments of the annotation */ args  : List[String])
             (/** function to process         */ f     : Typed.Function) =
    {
        Import(f).toString
    }

    val name = "python.random"

}