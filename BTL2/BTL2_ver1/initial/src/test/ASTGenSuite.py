import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     input = """Class Program {}"""
    #     expect = "Program([ClassDecl(Id(Program),[])])"
    #     self.assertTrue(TestAST.test(input,expect,300))
    def test_simple_program2(self):
        input = """
        Class Program { }
        Class Test { }
        """
        expect = "Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Test),[])])"
        self.assertTrue(TestAST.test(input,expect,301))
    def test_simple_program3(self):
        input = """
        Class Test:FatherClass { }
        """
        expect = "Program([ClassDecl(Id(Test),Id(FatherClass),[])])"
        self.assertTrue(TestAST.test(input,expect,302))
    def test_simple_funcdecl(self):
        input = """
        Class Program {
            testFunc(My1stCons, My2ndCons: Int; MyFloat: Float) {}
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFunc),Instance,[param(Id(My1stCons),IntType),param(Id(My2ndCons),IntType),param(Id(MyFloat),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,303))
    def test_simple_vardecl(self):
        input = """
        Class Program {
            Var a, $b: Int;
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,304))
    def test_simple_vardecl2(self):
        input = """
        Class Program {
            Var a, b: Int = 12, 13;
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(12))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(13)))])])"
        self.assertTrue(TestAST.test(input,expect,305))
    def test_simple_valdecl(self):
        input = """
        Class Program {
            Val c, $d: Int;
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,None)),AttributeDecl(Static,ConstDecl(Id($d),IntType,None))])])"
        self.assertTrue(TestAST.test(input,expect,306))
    def test_simple_valdecl2(self):
        input = """
        Class Program {
            Val c, d, e: Int = 12, 13, 10;
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(12))),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(13))),AttributeDecl(Instance,ConstDecl(Id(e),IntType,IntLit(10)))])])"
        self.assertTrue(TestAST.test(input,expect,307))
    
    def test_simple_valdecl3(self):
        input = """
        Class Program {
            Var a: Int = 3 + 2;
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(3),IntLit(2))))])])"
        self.assertTrue(TestAST.test(input,expect,308))

    def test_simple_valdecl4(self): # nhan chia truoc
        input = """
        Class Program {
            Var a: Int = 5 + 3 * 2;
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(5),BinaryOp(*,IntLit(3),IntLit(2)))))])])"
        self.assertTrue(TestAST.test(input,expect,309))

    def test_simple_valdecl5(self): # dau ngoac truoc
        input = """
        Class Program {
            Var a: Int = (5 + 3) * 2;
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(*,BinaryOp(+,IntLit(5),IntLit(3)),IntLit(2))))])])"
        self.assertTrue(TestAST.test(input,expect,310))

    def test_exp(self): # fun
        input = """
        Class Program {
            Var a: Int = Self.b;
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FieldAccess(Self(),Id(b))))])])"
        self.assertTrue(TestAST.test(input,expect,311))

    def test_assign_stmt(self):
        input = """
        Class Program {
            testFun() {
                a = b;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AssignStmt(Id(a),Id(b))]))])])"
        self.assertTrue(TestAST.test(input,expect,312))

    def test_for_stmt(self):
        input = """
        Class Program {
            testFun() {
                Foreach (a In 1 .. 100 By 2) {
                        a = a + 3;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3)))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,313))

    def test_return_stmt(self):
        input = """
        Class Program {
            testFun() {
                Return;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,314))
    def test_return_stmt2(self):
        input = """
        Class Program {
            testFun() {
                Return 5;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([Return(IntLit(5))]))])])"
        self.assertTrue(TestAST.test(input,expect,315))
    def test_break_stmt(self):
        input = """
        Class Program {
            testFun() {
                Foreach (a In 1 .. 100 By 2) {
                        a = a + 3;
                        Break;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3))),Break])])]))])])"    
        self.assertTrue(TestAST.test(input,expect,316))
    def test_continue_stmt(self):
        input = """
        Class Program {
            testFun() {
                Foreach (a In 1 .. 100 By 2) {
                        a = a + 3;
                        Continue;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3))),Continue])])]))])])"
        self.assertTrue(TestAST.test(input,expect,317))

    def test_member_access_stmt(self):
        input = """
        Class Program {
            testFun() {
                obj.getName(12, 3);
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([Call(Id(obj),Id(getName),[IntLit(12),IntLit(3)])]))])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test_field_access(self):
        input = """
        Class Program {
            testFun() {
                c = a.b;
                c = Self.b;
                c = a::$b;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AssignStmt(Id(c),FieldAccess(Id(a),Id(b))),AssignStmt(Id(c),FieldAccess(Self(),Id(b))),AssignStmt(Id(c),FieldAccess(Id(a),Id($b)))]))])])"
        self.assertTrue(TestAST.test(input,expect,319))
    def test_call_expr(self):
        input = """
        Class Program {
            testFun() {
                c = a::$b();
                c = a.b();
                a.b(3, 4);
                a::$b();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AssignStmt(Id(c),CallExpr(Id(a),Id($b),[])),AssignStmt(Id(c),CallExpr(Id(a),Id(b),[])),Call(Id(a),Id(b),[IntLit(3),IntLit(4)]),Call(Id(a),Id($b),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,320))
    
    def test_vardecl_stmt(self):
        input = """
        Class Program {
            testFun() {
                Var a: Int = 12;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(12))]))])])"
        self.assertTrue(TestAST.test(input,expect,321))

    def test_if_stmt(self):
        input = """
        Class Program {
            testFun() {
                If (a > b) {
                    a = a + 1;
                }
                Else {
                    a = a - 1;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,322))
    
    def test_if_stmt2(self):
        input = """
        Class Program {
            testFun() {
                If (a > b) {
                    a = a + 1;
                }
                Elseif (a < b) {
                    a = a - 1;
                }
                Else {
                    a = a * 2;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]),Block([AssignStmt(Id(a),BinaryOp(*,Id(a),IntLit(2)))])))]))])])"
        self.assertTrue(TestAST.test(input,expect,323))

    def test_constructor_decl(self):
        input = """Class Program {
            Constructor() {}
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,324))
    def test_destructor_decl(self):
        input = """Class Program {
            Destructor() {}
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,325))
    def test_constructor_with_other_func(self):
        input = """Class A {
            Constructor() {}
            MyTest() {
                Foreach (var1 In 50 .. 100 By 5) {
                    Break;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(MyTest),Instance,[],Block([For(Id(var1),IntLit(50),IntLit(100),IntLit(5),Block([Break])])]))])])"
        self.assertTrue(TestAST.test(input,expect,326))
    def test_destructor_with_other_func(self):
        input = """Class A {
            MyTest() {
                Var a: Int;
                Var b: Float = 0.2;
            }
            Destructor() {}
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType,FloatLit(0.2))])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,327))
    def test_var_decl_with_some_type(self):
        input = """Class A {
            MyTest() {
                Var a: Int = 5;
                Var b: Float = 3.5;
                Var c: String = "Hello";
                Var d: Boolean = True;
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(5)),VarDecl(Id(b),FloatType,FloatLit(3.5)),VarDecl(Id(c),StringType,StringLit(Hello)),VarDecl(Id(d),BoolType,BooleanLit(True))]))])])"
        self.assertTrue(TestAST.test(input,expect,328))
    def test_var_with_arr_type(self):
        input = """Class A {
            MyTest() {
                Var myArray: Array[Int, 5] = Array(1, 3, 5, 7, 9);
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([VarDecl(Id(myArray),ArrayType(5,IntType),[IntLit(1),IntLit(3),IntLit(5),IntLit(7),IntLit(9)])]))])])"
        self.assertTrue(TestAST.test(input,expect,329))
    def test_for_stmt_without_by(self):
        input = """Class Program {
            main() {
                Foreach (var1 In 0 .. 10) {
                    Val myStr: String = "Hello World";
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(var1),IntLit(0),IntLit(10),IntLit(1),Block([ConstDecl(Id(myStr),StringType,StringLit(Hello World))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,330))
    def test_block_stmt_inside_block(self):
        input = """Class Program {
            main() {
                {
                    { Val a, b: Int; }
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([Block([ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),IntType,None)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,331))
    def test_exp_order(self):
        input = """Class Program {
            Val a: Int = 3 + 4 * 5;
            Val b: Int = (1 + 2) * 6;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(3),BinaryOp(*,IntLit(4),IntLit(5))))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(6))))])])"
        self.assertTrue(TestAST.test(input,expect,332))
    def test_random_mixing(self):
        input = """Class Program {
            main() {
                Var r, s: Int;
                r = 2;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),IntLit(2)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])"
        self.assertTrue(TestAST.test(input,expect,333))
    def test_main_empty(self):
        input = """Class Program{
                main(){

                }
             }
             """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 334))
    def test_main_with_other_main(self):
        input = """Class Program {
                    main(){

                    }
                }
                Class testClass {
                    main() { }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(testClass),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 335))
    def test_main_with_param(self):
        input = """Class Program {
                    main(a: Int) {

                    }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 336))
    def test_if_stmt3(self):
        input = """Class Shape {
                    testFunc() {
                        If (a > b) {
                            a = b;
                        }
                        Elseif (a < b) {
                            c = d;
                        }
                        Elseif (a == b) {
                            e = f;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),Id(b))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(c),Id(d))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(e),Id(f))]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 337))
    def test_if_stmt4(self):
        input = """Class Shape {
                    testFunc() {
                        If (a > b) {
                            a = b;
                        }
                        Elseif (a < b) {
                            c = d;
                        }
                        Elseif (a == b) {
                            e = f;
                        }
                        Else {
                            g = h;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),Id(b))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(c),Id(d))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(e),Id(f))]),Block([AssignStmt(Id(g),Id(h))]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 338))
    def test_return_stmt3(self):
        input = """Class Shape {
                    testFunc() {
                        Return Circle::$getArea();
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([Return(CallExpr(Id(Circle),Id($getArea),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 339))
    def test_string_exp(self):
        input = """Class Shape {
                    testFunc() {
                        Var a: String;
                        a = a +. "hello";
                        Return a;
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([VarDecl(Id(a),StringType),AssignStmt(Id(a),BinaryOp(+.,Id(a),StringLit(hello))),Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 340))
    def test_string_exp2(self):
        input = """Class Shape {
                    testFunc() {
                        Var a: String;
                        Return (a ==. "hello");
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([VarDecl(Id(a),StringType),Return(BinaryOp(==.,Id(a),StringLit(hello)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 341))
    def test_logic_exp(self):
        input = """Class Shape {
                    testFunc() {
                        Var a: Boolean;
                        a = (1 == 2) || (3 == 4);
                        Return a;
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([VarDecl(Id(a),BoolType),AssignStmt(Id(a),BinaryOp(||,BinaryOp(==,IntLit(1),IntLit(2)),BinaryOp(==,IntLit(3),IntLit(4)))),Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 342))
    def test_add_sub_exp(self):
        input = """Class Shape {
                    testFunc() {
                        Var a: Int;
                        a = 1 + (2 - 3);
                        a = 5 + 6 - 7;
                        Return a;
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),BinaryOp(+,IntLit(1),BinaryOp(-,IntLit(2),IntLit(3)))),AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,IntLit(5),IntLit(6)),IntLit(7))),Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 343))
    def test_mul_div_exp(self):
        input = """Class Shape {
                    testFunc() {
                        Var a: Int;
                        a = 1 * (2 / 3);
                        a = 5 * 6 / 7;
                        a = 12 % 4;
                        Return a;
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),BinaryOp(*,IntLit(1),BinaryOp(/,IntLit(2),IntLit(3)))),AssignStmt(Id(a),BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(6)),IntLit(7))),AssignStmt(Id(a),BinaryOp(%,IntLit(12),IntLit(4))),Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 344))
    def test_not_exp(self):
        input = """Class Shape {
                    testFunc() {
                        Var a: Boolean;
                        a = !(1 == 2);
                        Return a;
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([VarDecl(Id(a),BoolType),AssignStmt(Id(a),UnaryOp(!,BinaryOp(==,IntLit(1),IntLit(2)))),Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 345))
    def test_sub_unary_exp(self):
        input = """Class Shape {
                    testFunc() {
                        Var a: Int;
                        a = -(1 + 2);
                        Return a;
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),UnaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)))),Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 346))
    def test_index_op(self):
        input = """Class Shape {
                    testFunc() {
                        Var arr: Array[Int, 3] = Array(1, 2, 3);
                        a = a[1];
                        Return a;
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([VarDecl(Id(arr),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)]),AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1)])),Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 347))
    def test_index_op2(self):
        input = """Class Shape {
                    testFunc() {
                        a = arr[1][2][3];
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AssignStmt(Id(a),ArrayCell(Id(arr),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 348))
    def test_new_exp(self):
        input = """Class Test {
            Var myVar1: Shape = New Shape();
        }
            """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(myVar1),ClassType(Id(Shape)),NewExpr(Id(Shape),[])))])])"
        self.assertTrue(TestAST.test(input, expect, 349))
    def test_self_exp(self):
        input = """Class Test {
            Var myVar1: String = Self.name;
        }
            """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(myVar1),StringType,FieldAccess(Self(),Id(name))))])])"
        self.assertTrue(TestAST.test(input, expect, 350))
    def test_random_mixing2(self):
        input = """Class Test {
            Var myVar1: String = "Hello " + Self.name + "!";
        }
            """
        expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(myVar1),StringType,BinaryOp(+,BinaryOp(+,StringLit(Hello ),FieldAccess(Self(),Id(name))),StringLit(!))))])])"
        self.assertTrue(TestAST.test(input, expect, 351))
    def test_random_mixing3(self):
        input = """Class Test {
            testFunc() { }
            main() { }
        }
        Class Program {
            testFunc2() { }
            main() { }
        }
            """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(testFunc),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(testFunc2),Instance,[],Block([])),MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 352))
    def test_random_mixing4(self):
        input = """Class Test {
            testFunc() { }
            main() { }
        }
        Class Program {
            testFunc2() { }
            main() { }
        }
        Class Program2 {
            testFunc3() { }
            main() { }
        }
            """
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(testFunc),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(testFunc2),Instance,[],Block([])),MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Program2),[MethodDecl(Id(testFunc3),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 353))
    def test_random_mixing5(self):
        input = """Class Test {
            $getNumOfShape(My1stCons, My2ndCons: Int; MyFloat: Float) {
                If(3 > 2) {My1stCons = 3 + 6;}
                Else {My1stCons = 99;}
            }
        }"""
        expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id($getNumOfShape),Static,[param(Id(My1stCons),IntType),param(Id(My2ndCons),IntType),param(Id(MyFloat),FloatType)],Block([If(BinaryOp(>,IntLit(3),IntLit(2)),Block([AssignStmt(Id(My1stCons),BinaryOp(+,IntLit(3),IntLit(6)))]),Block([AssignStmt(Id(My1stCons),IntLit(99))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 354))
    def test_random_mixing6(self):
        input = """Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {

            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 355))
    def test_random_mixing7(self):
        input = """Class Shape {
            Var a, b, c: Int = 1, 2, 3;
            $testFunc() {
                Foreach (a In 1 .. 100 By 2) {
                    a = a + 3;
                }
                b = a * 2;
            }
        }
        Class Program {
            main() {
                Shape::$testFunc();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(3))),MethodDecl(Id($testFunc),Static,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3)))])]),AssignStmt(Id(b),BinaryOp(*,Id(a),IntLit(2)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Shape),Id($testFunc),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_random_mixing8(self):
        input = """Class Program {
            Var a, b, c: Int = 1, 2 ,3;
            main() { }
            testFunc() {
                Foreach (i In 0 .. 12 By 3)
                {
                    x = x * x + (3/2)*x + 9;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(3))),MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(testFunc),Instance,[],Block([For(Id(i),IntLit(0),IntLit(12),IntLit(3),Block([AssignStmt(Id(x),BinaryOp(+,BinaryOp(+,BinaryOp(*,Id(x),Id(x)),BinaryOp(*,BinaryOp(/,IntLit(3),IntLit(2)),Id(x))),IntLit(9)))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 357))
    def test_random_mixing9(self):
        input = """
        Class Shape {
            Var a, b, c: Int = 1, 2 ,3;
            $testFunc() {
                Foreach (i In 0 .. 12 By 3)
                {
                    x = i + 1;
                    Break;
                }
            }
        }
        ## Class Program {
            main () { }
        } ##
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(3))),MethodDecl(Id($testFunc),Static,[],Block([For(Id(i),IntLit(0),IntLit(12),IntLit(3),Block([AssignStmt(Id(x),BinaryOp(+,Id(i),IntLit(1))),Break])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 358))
    def test_random_mixing10(self):
        input = """
        Class Shape {
            testFunc() {
                str = "$ $ $ @@ ***" +. "(0)_(0)";
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AssignStmt(Id(str),BinaryOp(+.,StringLit($ $ $ @@ ***),StringLit((0)_(0))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 359))
    def test_random_mixing11(self):
        input = """
        Class Shape {
            testFunc() { }
        }
        Class Circle: Shape {

        }
        Class Rectangle: Shape {
        
        }
        Class myChild: Circle {

        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([]))]),ClassDecl(Id(Circle),Id(Shape),[]),ClassDecl(Id(Rectangle),Id(Shape),[]),ClassDecl(Id(myChild),Id(Circle),[])])"
        self.assertTrue(TestAST.test(input, expect, 360))
    def test_empty_if_else(self):
        input = """
        Class A {
            func() {
                If (a > b) {

                }
                Elseif (c <= d)
                {

                }
                Elseif (e >= f)
                {

                }
                Else {

                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(func),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([]),If(BinaryOp(<=,Id(c),Id(d)),Block([]),If(BinaryOp(>=,Id(e),Id(f)),Block([]),Block([]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 361))
    def test_for_with_if_stmt(self):
        input = """
        Class A {
            func() {
                Foreach (i In 0 .. 10) {
                    If (i == 5) {
                        Break;
                    }
                    Else {
                        Continue;
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(func),Instance,[],Block([For(Id(i),IntLit(0),IntLit(10),IntLit(1),Block([If(BinaryOp(==,Id(i),IntLit(5)),Block([Break]),Block([Continue]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 362))
    def test_fake_main_in_program(self):
        input = """
        Class Program {
            main(a, b: Int) {
                Return;
            }
        }
        Class A {
            func() { }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return()]))]),ClassDecl(Id(A),[MethodDecl(Id(func),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 363))
    def test_some_float_variables(self):
        input = """
        Class Program {
            Var a, b, c: Float = 1.0, 2.0 ,3.0;
            main() {
                a = a + 0.527e-2;
                b = b * (5.72 / 12e-6);
                Return c + b + a;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,FloatLit(1.0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(2.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(3.0))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(+,Id(a),FloatLit(0.00527))),AssignStmt(Id(b),BinaryOp(*,Id(b),BinaryOp(/,FloatLit(5.72),FloatLit(1.2e-05)))),Return(BinaryOp(+,BinaryOp(+,Id(c),Id(b)),Id(a)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 364))
    def test_some_octal_variable(self):
        input = """
        Class Program {
            Var a, b, c: Int = 0132, 0252 ,0375;
            main() {
                a = a + 04751;
                b = b * 02242 + 07545;
                Return c + b + a;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(90))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(170))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(253))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(2537))),AssignStmt(Id(b),BinaryOp(+,BinaryOp(*,Id(b),IntLit(1186)),IntLit(3941))),Return(BinaryOp(+,BinaryOp(+,Id(c),Id(b)),Id(a)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 365))
    def test_some_hex_variable(self):
        input = """
        Class Program {
            Var a, b, c: Int = 0x1A, 0x2B ,0x3C;
            main() {
                a = a + 0x4D + 0x2E6;
                b = b * 0x5EB42 + 0x6FA2F;
                Return c + b + a;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(26))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(43))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(60))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,Id(a),IntLit(77)),IntLit(742))),AssignStmt(Id(b),BinaryOp(+,BinaryOp(*,Id(b),IntLit(387906)),IntLit(457263))),Return(BinaryOp(+,BinaryOp(+,Id(c),Id(b)),Id(a)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 366))
    def test_some_binary_exp(self):
        input = """
        Class TestClass {
            myFunc() {
                a = b * c + d / e - f;
                z = "Hello" +. "World";
            }
        }
        """
        expect = "Program([ClassDecl(Id(TestClass),[MethodDecl(Id(myFunc),Instance,[],Block([AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(c)),BinaryOp(/,Id(d),Id(e))),Id(f))),AssignStmt(Id(z),BinaryOp(+.,StringLit(Hello),StringLit(World)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 367))
    def test_random_mixing12(self):
        input = """
        Class Shape {
            $callMeNow() {
                Return 123;
            }
            $callMeLater(a, b: Int) {
                Return a * b;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$callMeLater(1, 2));
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($callMeNow),Static,[],Block([Return(IntLit(123))])),MethodDecl(Id($callMeLater),Static,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(*,Id(a),Id(b)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[CallExpr(Id(Shape),Id($callMeLater),[IntLit(1),IntLit(2)])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 368))
    def test_random_mixing13(self):
        input = """Class A {
            Constructor() {var1 = 0;}
            Destructor() {}
            MyTest() {
                    If(var1 > 12) { }
                    Elseif(var1 < 4) { }
                    Elseif(var1 == 4) { }
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(var1),IntLit(0))])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(MyTest),Instance,[],Block([If(BinaryOp(>,Id(var1),IntLit(12)),Block([]),If(BinaryOp(<,Id(var1),IntLit(4)),Block([]),If(BinaryOp(==,Id(var1),IntLit(4)),Block([]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 369))
    def test_random_mixing14(self):
        input = """
        Class A {
            $testStatic() { }
            testInstance() { }
            $testStatic2() { }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id($testStatic),Static,[],Block([])),MethodDecl(Id(testInstance),Instance,[],Block([])),MethodDecl(Id($testStatic2),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 370))
    def test_random_mixing15(self):
        input = """
        Class Shape {
            $callMeNow() { }
        }
        Class Circle {
            callMeLater() {
                Var obj: Shape = New Shape();
                obj.name = "Circle";
                Return obj;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($callMeNow),Static,[],Block([]))]),ClassDecl(Id(Circle),[MethodDecl(Id(callMeLater),Instance,[],Block([VarDecl(Id(obj),ClassType(Id(Shape)),NewExpr(Id(Shape),[])),AssignStmt(FieldAccess(Id(obj),Id(name)),StringLit(Circle)),Return(Id(obj))]))])])"
        self.assertTrue(TestAST.test(input, expect, 371))
    def test_random_mixing16(self): # chua check
        input = """
        Class Shape {
            $callMeNow() { }
        }
        Class Circle {
            callMeLater() {
                Var obj: Shape;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($callMeNow),Static,[],Block([]))]),ClassDecl(Id(Circle),[MethodDecl(Id(callMeLater),Instance,[],Block([VarDecl(Id(obj),ClassType(Id(Shape)),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 372))
    def test_random_mixing17(self): # chua check
        input = """
        Class myClass {
            $myFunc() {
                Return 1;
                Return 2;
                Return 3;
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id($myFunc),Static,[],Block([Return(IntLit(1)),Return(IntLit(2)),Return(IntLit(3))]))])])"
        self.assertTrue(TestAST.test(input, expect, 373))
    def test_random_mixing18(self):
        input = """
        Class myClass {
            $myFunc() {
                Return (1 + 2) * 3;
            }
            myFunc2() {
                Return myClass::$myFunc();
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id($myFunc),Static,[],Block([Return(BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)))])),MethodDecl(Id(myFunc2),Instance,[],Block([Return(CallExpr(Id(myClass),Id($myFunc),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 374))
    def test_random_mixing19(self):
        input = """
        Class myClass {
            $myFunc() {
                {
                    Var a: Int;
                    Var b: FLoat = 12.3;
                }
                {
                    Var c: String = "Hello";
                }
            }
            
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id($myFunc),Static,[],Block([Block([VarDecl(Id(a),IntType),VarDecl(Id(b),ClassType(Id(FLoat)),FloatLit(12.3))]),Block([VarDecl(Id(c),StringType,StringLit(Hello))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 375))
    def test_random_mixing20(self):
        input = """
        Class myClass {
            $addFunc(a, b: Int) {
                Return a + b;
            }
            $subFunc(a, b: Int) {
                Return a - b;
            }
            printFunc()
            {
                Return myClass::$addFunc(1, 2);
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id($addFunc),Static,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(+,Id(a),Id(b)))])),MethodDecl(Id($subFunc),Static,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(-,Id(a),Id(b)))])),MethodDecl(Id(printFunc),Instance,[],Block([Return(CallExpr(Id(myClass),Id($addFunc),[IntLit(1),IntLit(2)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 376))
    def test_random_mixing21(self):
        input = """
        Class myClass {
            $addFunc(a, b: Int) {
                Return a + b;
            }
        }
        Class myClass2 {
            $subFunc(a, b: Int) {
                Return a - myClass::$addFunc(a, b);
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id($addFunc),Static,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(+,Id(a),Id(b)))]))]),ClassDecl(Id(myClass2),[MethodDecl(Id($subFunc),Static,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(-,Id(a),CallExpr(Id(myClass),Id($addFunc),[Id(a),Id(b)])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 377))
    def test_random_mixing22(self):
        input = """
        Class Program {
            main() { }
            testFunc() {
                Self.name = "abc";
                Self.age = "12";
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(testFunc),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(name)),StringLit(abc)),AssignStmt(FieldAccess(Self(),Id(age)),StringLit(12))]))])])"
        self.assertTrue(TestAST.test(input, expect, 378))
    def test_random_mixing23(self):
        input = """Class A {
            MyTest() {
                Var yes, no: Boolean;
                ## yes = (True && False) || (False || (3 != 2) || (5 >> 3)); ##
                no = False;
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([VarDecl(Id(yes),BoolType),VarDecl(Id(no),BoolType),AssignStmt(Id(no),BooleanLit(False))]))])])"
        self.assertTrue(TestAST.test(input, expect, 379))
    def test_random_mixing24(self):
        input = """
        Class A {
            MyTest() {
                If (True) {
                    If (False) {
                        If (True) { }
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([If(BooleanLit(True),Block([If(BooleanLit(False),Block([If(BooleanLit(True),Block([]))]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 380))
    def test_random_mixing25(self):
        input = """
        Class Program {
            main() {
                Return "main";
            }
            main(a: Int) {
                Return "main fake";
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(StringLit(main))])),MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([Return(StringLit(main fake))]))])])"
        self.assertTrue(TestAST.test(input, expect, 381))
    def test_random_mixing26(self):
        input = """
        Class myClass {
            Val $a, b: Int;
            Var c, $d: String;
            testFunc() {
                c = b;
                $a = $d;
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,None)),AttributeDecl(Instance,VarDecl(Id(c),StringType)),AttributeDecl(Static,VarDecl(Id($d),StringType)),MethodDecl(Id(testFunc),Instance,[],Block([AssignStmt(Id(c),Id(b)),AssignStmt(Id($a),Id($d))]))])])"
        self.assertTrue(TestAST.test(input, expect, 382))
    def test_random_mixing27(self):
        input = """Class A {
            MyTest() {
                Var a, b, c: Int;
                Val x, y, z: Float;
                a = ((12 * 35) + 137/2 - -14)*(10 * (-16));
                Return a;
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),ConstDecl(Id(x),FloatType,None),ConstDecl(Id(y),FloatType,None),ConstDecl(Id(z),FloatType,None),AssignStmt(Id(a),BinaryOp(*,BinaryOp(-,BinaryOp(+,BinaryOp(*,IntLit(12),IntLit(35)),BinaryOp(/,IntLit(137),IntLit(2))),UnaryOp(-,IntLit(14))),BinaryOp(*,IntLit(10),UnaryOp(-,IntLit(16))))),Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 383))
    def test_random_mixing28(self):
        input = """
        Class myClass {
            testFunc() {
                Foreach (i In 0 .. 100) {
                    Foreach (j In 0 .. 100) {
                        If (i == j) {
                            Continue;
                        }
                        Else {
                            j = j + 3;
                        }
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id(testFunc),Instance,[],Block([For(Id(i),IntLit(0),IntLit(100),IntLit(1),Block([For(Id(j),IntLit(0),IntLit(100),IntLit(1),Block([If(BinaryOp(==,Id(i),Id(j)),Block([Continue]),Block([AssignStmt(Id(j),BinaryOp(+,Id(j),IntLit(3)))]))])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 384))
    def test_random_mixing29(self):
        input = """
        Class myClass {
            testFunc() {
                Var a, b, c: Boolean;
                a = True;
                b = False;
                c = (a && b) || (a || b);
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id(testFunc),Instance,[],Block([VarDecl(Id(a),BoolType),VarDecl(Id(b),BoolType),VarDecl(Id(c),BoolType),AssignStmt(Id(a),BooleanLit(True)),AssignStmt(Id(b),BooleanLit(False)),AssignStmt(Id(c),BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),BinaryOp(||,Id(a),Id(b))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 385))
    def test_random_mixing30(self):
        input = """
        Class myClass {
            testFunc() {
                If (1) {
                    Foreach (i In 0 .. 1000 By 10) {
                    }
                    Foreach (i In 0 .. 1000) {
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id(testFunc),Instance,[],Block([If(IntLit(1),Block([For(Id(i),IntLit(0),IntLit(1000),IntLit(10),Block([])]),For(Id(i),IntLit(0),IntLit(1000),IntLit(1),Block([])])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 386))
    def test_random_mixing31(self):
        input = """
        Class myClass {
            testFunc() {
                obj.getA();
                obj.getB(1, 2, 3);
                obj::$getC();
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id(testFunc),Instance,[],Block([Call(Id(obj),Id(getA),[]),Call(Id(obj),Id(getB),[IntLit(1),IntLit(2),IntLit(3)]),Call(Id(obj),Id($getC),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 387))
    def test_random_mixing32(self):
        input = """
        Class myClass {
            testFunc() {
                obj.getA();
                obj.getB(1, 2, 3);
                obj::$getC();
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id(testFunc),Instance,[],Block([Call(Id(obj),Id(getA),[]),Call(Id(obj),Id(getB),[IntLit(1),IntLit(2),IntLit(3)]),Call(Id(obj),Id($getC),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 388))
    def test_random_mixing33(self):
        input = """
        Class myClass { }
        Class myClass2:myClass { }
        Class myClass3:myClass2 { }
        Class myClass4:myClass3 { }
        """
        expect = "Program([ClassDecl(Id(myClass),[]),ClassDecl(Id(myClass2),Id(myClass),[]),ClassDecl(Id(myClass3),Id(myClass2),[]),ClassDecl(Id(myClass4),Id(myClass3),[])])"
        self.assertTrue(TestAST.test(input, expect, 389))
    def test_random_mixing34(self):
        input = """
        Class myClass {
            testFunc() {
                Foreach (i In (3-2) .. (10 * 100)) {
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(myClass),[MethodDecl(Id(testFunc),Instance,[],Block([For(Id(i),BinaryOp(-,IntLit(3),IntLit(2)),BinaryOp(*,IntLit(10),IntLit(100)),IntLit(1),Block([])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 390))
    def test_random_mixing35(self):
        input = """
        Class Program {
        ##  main() {
                Var a, b, c: Int;
            }
        ##
            main() {
                a = 1;
                b = 2;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),IntLit(1)),AssignStmt(Id(b),IntLit(2))]))])])"
        self.assertTrue(TestAST.test(input, expect, 391))
    def test_random_mixing36(self):
        input = """Class A {
            MyTest() {
                Var str: String;
                If("goodbye" ==. "goodluck") {
                    str = "goodbye" +. "goodluck";
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([VarDecl(Id(str),StringType),If(BinaryOp(==.,StringLit(goodbye),StringLit(goodluck)),Block([AssignStmt(Id(str),BinaryOp(+.,StringLit(goodbye),StringLit(goodluck)))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 392))
    def test_random_mixing37(self):
        input = """Class A {
            MyTest() {
                Var a, b, c: Int;
                Val x, y, z: Float;
                a = -12 + 9;
                b = -3 -5 -7;
                c = 127 *-12 + (-3);
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),ConstDecl(Id(x),FloatType,None),ConstDecl(Id(y),FloatType,None),ConstDecl(Id(z),FloatType,None),AssignStmt(Id(a),BinaryOp(+,UnaryOp(-,IntLit(12)),IntLit(9))),AssignStmt(Id(b),BinaryOp(-,BinaryOp(-,UnaryOp(-,IntLit(3)),IntLit(5)),IntLit(7))),AssignStmt(Id(c),BinaryOp(+,BinaryOp(*,IntLit(127),UnaryOp(-,IntLit(12))),UnaryOp(-,IntLit(3))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 393))
    def test_random_mixing38(self):
        input = """Class A {
            testFunc() {
                a = b[1][2];
                b[1][2] = c[3][4];
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(testFunc),Instance,[],Block([AssignStmt(Id(a),ArrayCell(Id(b),[IntLit(1),IntLit(2)])),AssignStmt(ArrayCell(Id(b),[IntLit(1),IntLit(2)]),ArrayCell(Id(c),[IntLit(3),IntLit(4)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 394))
    def test_random_mixing39(self):
        input = """Class A {
            Constructor(a, b: Int) { }
            testFunc() { }
            Destructor() {
                obj.a = 0;
                obj.b = 0;
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([])),MethodDecl(Id(testFunc),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(obj),Id(a)),IntLit(0)),AssignStmt(FieldAccess(Id(obj),Id(b)),IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 395))
    def test_self_stm(self):
        input = """Class A {
            testFunc() {
                Self.name = "hello";
                Self.getName();
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(testFunc),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(name)),StringLit(hello)),Call(Self(),Id(getName),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 396))
    def test_random_mixing40(self):
        input = """Class A {
            testFunc() {
                If(!(a == b)) {
                    Return;
                }
                Else {
                    Foreach (i In 1 .. 10) {
                        If(i == 5) { Return; }
                        Else { Continue; }
                    }
                }
                Return 5;
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(testFunc),Instance,[],Block([If(UnaryOp(!,BinaryOp(==,Id(a),Id(b))),Block([Return()]),Block([For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([If(BinaryOp(==,Id(i),IntLit(5)),Block([Return()]),Block([Continue]))])])])),Return(IntLit(5))]))])])"
        self.assertTrue(TestAST.test(input, expect, 397))
    def test_random_mixing41(self):
        input = """Class A {
            testFunc() {
                Var arr: Array[Int, 5] = Array(5, 4, 3, 2, 1);
                kq = arr[0] + arr[1] + arr[2] + arr[3] + arr[4];
                kq = kq % 2;
                Return kq;
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(testFunc),Instance,[],Block([VarDecl(Id(arr),ArrayType(5,IntType),[IntLit(5),IntLit(4),IntLit(3),IntLit(2),IntLit(1)]),AssignStmt(Id(kq),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,ArrayCell(Id(arr),[IntLit(0)]),ArrayCell(Id(arr),[IntLit(1)])),ArrayCell(Id(arr),[IntLit(2)])),ArrayCell(Id(arr),[IntLit(3)])),ArrayCell(Id(arr),[IntLit(4)]))),AssignStmt(Id(kq),BinaryOp(%,Id(kq),IntLit(2))),Return(Id(kq))]))])])"
        self.assertTrue(TestAST.test(input, expect, 398))
    def test_random_mixing42(self):
        input = """Class A {
            Constructor() {var1 = 0;}
            Destructor() {}
            MyTest() {
                Foreach (var1 In 50 .. 100 By 5) {
                    If (var1 > 62) { Break; }
                    Else {var1 = var1 + 1;}
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(var1),IntLit(0))])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(MyTest),Instance,[],Block([For(Id(var1),IntLit(50),IntLit(100),IntLit(5),Block([If(BinaryOp(>,Id(var1),IntLit(62)),Block([Break]),Block([AssignStmt(Id(var1),BinaryOp(+,Id(var1),IntLit(1)))]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 399))
    def test_int_value(self):
        input = """ Class Program {
                        getArea() {
                            Val a : Int = 012;
                        }
                    } """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getArea),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(10))]))])])"
        self.assertTrue(TestAST.test(input, expect, 400))