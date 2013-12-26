package generator.python

object Printer {

    import syntax.scala.Printer.{base => pp, types => st}

    trait Printable {
        def toPython : String
        def imports : List[predef.Importable]
    }

    object types {

        trait Bound extends Printable

        trait Unit extends Bound {
            def toPython =
                throw new Exception("Unit types are not supported yet for python generation")
            def imports = Nil

        }

        trait Tuple extends Bound {
            val elems : List[Bound]
            def toPython = {
                throw new Exception("Tuple types are not supported yet for python generation")
                //elems.mkString("(", ",", ")")
            }

            def imports = Nil
        }

        trait Function extends Bound {
            val args : List[Bound]
            val ret : Bound
            def toPython = {
                val a = args match {
                    case Nil => ""
                    case x :: Nil => "," + x
                    case _ => throw new Exception("Only unary and nullary functions are supported for python generation")
                }
                s"types.IFunction[$ret$a]"
                //(if (args.length == 1) args(0) else args.mkString("(", ",", ")")) + s" => $ret"
            }

            def imports = predef.ImportFrom("types", "marketsim") :: ret.imports ++ (args match {
                case Nil => Nil
                case x :: Nil =>
                    println(x.imports)
                    x.imports
                case _ => throw new Exception("Only unary and nullary functions are supported for python generation")
            })
        }

        trait UsedDefined extends st.UsedDefined with Printable with Bound
        {
            val builtins = Map("Float"  -> "float",
                               "Int"    -> "int",
                               "Boolean"-> "bool",
                               "String" -> "str")

            def imports =
                if (builtins contains name)
                    Nil
                else
                    predef.ImportFrom(name, "marketsim") :: Nil


            def toPython = builtins.getOrElse(name, name)
        }
    }

    trait PrintablePort extends Printable
    {
        def toScala : String
        override def toPython = toScala
    }

    trait Expr extends pp.Expr with PrintablePort

    trait BinOp extends pp.BinOp[Typed.Expr] with PrintablePort
    {
        override def imports = x.imports ++ y.imports
    }

    trait Neg extends pp.Neg[Typed.Expr] with PrintablePort
    {
        override def imports = x.imports
    }

    trait IfThenElse extends pp.IfThenElse[Typed.Expr, Typed.Expr] with PrintablePort
    {
        override def toPython = s"($cond)[${wrap(x)}, ${wrap(y)}]"

        override def imports = x.imports ++ y.imports ++ cond.imports
    }

    trait StringLit extends pp.StringLit with PrintablePort
    {
        override def imports = Nil
    }

    trait IntLit extends pp.IntLit with PrintablePort
    {
        override def imports = Nil
    }

    trait And extends pp.And[Typed.Expr] with PrintablePort
    {
        override def imports = x.imports ++ y.imports
    }
    trait Or extends pp.Or[Typed.Expr] with PrintablePort {
        override def imports = x.imports ++ y.imports
    }

    trait Not extends pp.Not[Typed.Expr, Typed.Expr] with PrintablePort {
        override def imports = x.imports
    }

    trait Condition extends pp.Condition[Typed.Expr] with PrintablePort {
        override def imports = x.imports ++ y.imports
    }

    type Priority_0 = pp.Priority_0

    trait FloatLit extends Expr with Priority_0 {
        self: Typed.FloatLit =>
        override def toPython = x.toString

        def imports = Nil
    }

    trait ParamRef extends Expr with Priority_0 {
        self: Typed.ParamRef =>
        override def toPython = "self." + p.name

        def imports = Nil
    }

    trait FunCall extends Expr with Priority_0 {
        self: Typed.FunctionCall =>
        override def toPython = target.name + arguments.map({ _._2 }).mkString("(",",",")")

        def moduleName = {
            val name = target.parent.qualifiedName mkString "."
            val d = if (name == "") name else "." + name
            "marketsim.gen._out" + (if (name == "") name else "." + name) + "._" + target.name
        }

        override def imports = predef.ImportFrom(target.name, moduleName) :: (arguments flatMap { p => p._2.imports })
    }

}
