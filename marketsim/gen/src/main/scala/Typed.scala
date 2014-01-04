package object Typed
{
    import AST.{BinOpSymbol, CondSymbol, DocString, QualifiedName}
    import syntax.scala.Printer.{typed => sc}
    import generator.python.{Printer => py}
    import AST.{ScPrintable, ScPyPrintable}

    abstract class Expr
            extends ScPyPrintable
            with    sc.Expr
            with    py.Expr
    {
        def ty : TypesBound.Base
    }

    case class Neg(x : Expr)
            extends Expr
            with    sc.Neg
            with    py.Neg
            with    TypeInference.Neg

    case class BinOp(symbol : BinOpSymbol,
                     x      : Expr,
                     y      : Expr)
            extends Expr
            with    sc.BinOp
            with    py.BinOp
            with    TypeInference.BinOp

    case class IfThenElse(cond  : Expr,
                          x     : Expr,
                          y     : Expr)
            extends Expr
            with    sc.IfThenElse
            with    py.IfThenElse
            with    TypeInference.IfThenElse

    case class StringLit(value : String)
            extends Expr
            with    sc.StringLit
            with    py.StringLit
            with    TypeInference.StringLit

    case class IntLit(value : Int)
            extends Expr
            with    sc.IntLit
            with    py.IntLit
            with    TypeInference.IntLit


    case class FloatLit(x : Double)
            extends Expr
            with    sc.FloatLit
            with    py.FloatLit
            with    TypeInference.FloatLit

    case class ParamRef(p : Parameter)
            extends Expr
            with    sc.ParamRef
            with    py.ParamRef
            with    TypeInference.ParamRef

    case class FunctionCall(target      : Function,
                            arguments   : List[(Parameter, Expr)])
            extends Expr
            with    sc.FunCall
            with    py.FunCall
            with    TypeInference.FunctionCall

    case class Annotation(target    : AnnotationHandler,
                          parameters: List[String])
            extends sc.Annotation
            with    ScPrintable

    case class Attributes(items : Map[String, String])
            extends sc.Attributes
            with    ScPrintable

    case class Parameter(name        : String,
                         ty          : TypesBound.Base,
                         initializer : Option[Expr],
                         comment     : List[String])
            extends sc.Parameter
            with    ScPrintable

    case class Or(x : Expr,
                  y : Expr)
            extends Expr
            with    sc.Or
            with    py.Or
            with    TypeInference.BinaryBoolean

    case class And(x : Expr,
                   y : Expr)
            extends Expr
            with    sc.And
            with    py.And
            with    TypeInference.BinaryBoolean

    case class Not(x : Expr)
            extends Expr
            with    sc.Not
            with    py.Not
            with    TypeInference.UnaryBoolean

    case class Condition(symbol : CondSymbol,
                         x      : Expr,
                         y      : Expr)
            extends Expr
            with    sc.Condition
            with    py.Condition
            with    TypeInference.Condition

    case class Function(parent      : Package,
                        name        : String,
                        parameters  : List[Parameter],
                        ret_type    : TypesBound.Base,
                        body        : Option[Expr],
                        docstring   : Option[DocString],
                        annotations : List[Annotation],
                        attributes  : Attributes)
            extends sc.Function
            with    ScPrintable
    {
        def decorators = attributes :: annotations

        def getAttribute(name : String) = tryGetAttribute(name) match {
            case Some(v) => v
            case None =>    throw new Exception(s"Cannot find attribute '$name' for function $this")
        }
        def tryGetAttribute(name : String) = attributes.items get name match {
            case Some(v) => Some(v)
            case None =>    parent tryGetAttribute name
        }

        override def equals(o : Any) = o match {
            case that : Function =>
                parent.qualifiedName == that.parent.qualifiedName &&
                name                 == that.name &&
                parameters           == that.parameters &&
                ret_type             == that.ret_type &&
                body                 == that.body &&
                docstring            == that.docstring &&
                attributes           == that.attributes &&
                annotations          == that.annotations
            case _ => false
        }

    }


    trait TypeDeclaration
    {
        val name        : String
        val scope       : Typed.Package
        val generics    : List[TypesUnbound.Parameter]

        def apply(genericArgs : List[TypesUnbound.Base] = Nil) : TypesUnbound.Base

        override def equals(o : Any) = o match {
            case that : TypeDeclaration => name == that.name && scope.qualifiedName == that.scope.qualifiedName
            case _ => false
        }

        def label = (scope qualifyName name) + (if (generics.isEmpty) "" else generics mkString ("[", ",", "]"))
    }

    case class AliasDecl(name       : String,
                         scope      : Typed.Package,
                         target     : TypesUnbound.Base,
                         generics   : List[TypesUnbound.Parameter])
            extends TypeDeclaration
            with    sc.AliasDecl
            with    ScPrintable
    {
        private val unbound = predef.Memoize1({
            genericArgs : List[TypesUnbound.Base] => TypesUnbound.Alias(this, genericArgs)
        })
        def apply(genericArgs : List[TypesUnbound.Base]) = unbound(genericArgs)
    }

    case class InterfaceDecl(name       : String,
                             scope      : Typed.Package,
                             bases      : List[TypesUnbound.Base],
                             generics   : List[TypesUnbound.Parameter])
            extends TypeDeclaration
            with    sc.InterfaceDecl
            with    ScPrintable
    {
        private val unbound = predef.Memoize1({
            genericArgs : List[TypesUnbound.Base] => TypesUnbound.Interface(this, genericArgs)
        })
        def apply(genericArgs : List[TypesUnbound.Base]) = unbound(genericArgs)
    }



    class Package extends sc.TopLevelPackage with ScPrintable
    {
        var functions = Map[String, Function]()
        var packages = Map[String, SubPackage]()
        var anonymous = List[AnonymousPackage]()
        var types = Map[String, TypeDeclaration]()
        var annotations = List[Annotation]()
        val attributes = Attributes(Map.empty)

        def qualifiedName : List[String] = Nil

        def qualifyName(x : String) = x

        def tryGetAttribute(name : String) : Option[String] = None

        def getName = ""

        def insert(f : Function)  = {
            functions = functions updated (f.name, f)
            f
        }

        def insert(t : TypeDeclaration) = {
            types = types updated (t.name, t)
            t
        }

        def createChild(n : String, a : Attributes) = {
            val p = new SubPackage(n, this, a)
            packages = packages updated (p.name, p)
            p
        }

        def createChild(a : Attributes) = {
            anonymous find { _.attributes == a } match {
                case Some(p) => p
                case None    =>
                    val p = new AnonymousPackage(this, a)
                    anonymous = p :: anonymous
                    p
            }
        }

        override def equals(o : Any) = o match {
            case that : Package =>
                (functions  equals that.functions) &&
                (packages   equals that.packages)  &&
                (anonymous  equals that.anonymous) &&
                (attributes equals that.attributes)
            case _ => false
        }

        def getOrElseUpdateFunction(name : String, default : => Typed.Function) =
            functions get name match {
                case Some(f) => f
                case None => insert(default)
            }

        // TODO: factor common implementation out

        def getOrElseUpdateType(name : String, default : => TypeDeclaration) =
            types get name match {
                case Some(t) => t
                case None => insert(default)
            }
    }

    val topLevel = new Package

    class AnonymousPackage(val parent : Package, override val attributes : Attributes)
            extends Package
            with    sc.AnonymousPackage
            with    ScPrintable
    {
        override def qualifiedName = parent.qualifiedName

        override def qualifyName(x : String) = parent qualifyName x

        override def tryGetAttribute(name : String) = attributes.items get name match {
            case Some(v) => Some(v)
            case None    => parent tryGetAttribute name
        }

    }

    class SubPackage(val name   : String,
                     parent     : Package,
                     attributes : Attributes)
            extends AnonymousPackage(parent, attributes)
            with    sc.SubPackage
            with    ScPrintable
    {
        override def qualifiedName = parent.qualifiedName :+ name

        override def qualifyName(x : String) = (qualifiedName mkString ".") + "." + x

        override def getName = name

        override def equals(o : Any) = o match {
            case that : SubPackage => super.equals(o) && name == that.name
            case _ => false
        }
    }

    trait AnnotationHandler
    {
        val name : String
    }

    object Annotations
    {
        var registry = Map[String, AnnotationHandler]()

        def register(handler : AnnotationHandler){
            registry = registry.updated(handler.name, handler)
        }

        def lookup(name : String) = registry.get(name) match {
            case Some(handler) => handler
            case None => throw new Exception(s"Cannot find annotation handler $name")
        }

        override def toString = registry.toString()
    }

    trait BeforeTyping extends Typed.AnnotationHandler
    {
        def beforeTyping(/** arguments of the annotation     */ args  : List[String])
                        (/** function to process             */ f     : AST.FunDef,
                         /** scope where function is defined */ scope : NameTable.Scope)
    }

    object BeforeTyping
    {
        def apply(scope : NameTable.Scope)
        {
            scope.packages.values foreach { apply }
            scope.anonymous       foreach { apply }

            scope.members.values collect { case f : AST.FunDef =>
                Typer.annotationsOf(f) collect { case Typed.Annotation(g : BeforeTyping, args) => g.beforeTyping(args)(f, scope) }
            }
        }
    }

    trait AfterTyping extends AnnotationHandler
    {
        def afterTyping(/** arguments of the annotation */ args  : List[String])
                       (/** function to process         */ f     : Typed.Function)
    }

    object AfterTyping
    {
        def apply(pkg : Package = topLevel)
        {
            pkg.packages.values foreach { apply(_) }
            pkg.anonymous       foreach { apply(_) }

            pkg.functions.values foreach { f=>
                f.annotations collect { case Typed.Annotation(g : AfterTyping, args) => g.afterTyping(args)(f) }
            }
        }
    }
}

