import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """Class Program {
            myFun() { }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redecl_class(self):
        input = """
        Class myClass {

        }
        Class myClass {

        }"""
        expect = "Redeclared Class: myClass"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redecl_func(self):
        input = """Class myClass {
            getName() { }
            getName() { }
        }"""
        expect = "Redeclared Method: getName"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redecl_var(self):
        input = """Class myClass {
            Var a, a: Int;
        }"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclare_param(self):
        input = """Class myClass {
            myFun(a, b, a: Int) { }
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclare_var_inside_method(self):
        input = """
        Class myClass {
            myFun(a, b: Int) {
                Var a : Int;
            }
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_assign_stmt(self):
        input = """
        Class Program {
            main(a, b: Int) {
                c = 2;
            }
        }"""
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclare_const_stmt(self):
        input = """
        Class Program {
            main(a, b: Int) {
                Var d, c : Int;
                Val c : Float = 2.0;
            }
        }"""
        expect = "Redeclared Constant: c"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_undeclare_class_parent(self):
        input = """
        Class Program: myClass {
            main() {

            }
        }
        """
        expect = "Undeclared Class: myClass"
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_cannot_assign_to_constant(self):
        input = """
        Class Program {
            main() {
                Val a : Int = 2;
                a = 3;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(3))"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_type_mismatch_in_constant(self):
        input = """
        Class Program {
            main() {
                Val a : Int = 2.5;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(2.5))"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_type_mismatch_in_constant2(self):
        input = """
        Class Program {
            main() {
                Val a : Float = "2.5";
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),FloatType,StringLit(2.5))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undecl_var_block_stmt(self):
        input = """
        Class Program {
            main() {
                {
                    Var a : Int;
                }
                a = 12;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_illegal_constant_expr(self):
        input = """
        Class Program {
            main() {
                Var a : Int;
                Val b : Int = a;
            }
        }
        """
        expect = "Illegal Constant Expression: Id(a)"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_illegal_constant_expr2(self):
        input = """
        Class Program {
            main() {
                Var a : Int;
                Val b : Int = - a;
            }
        }
        """
        expect = "Illegal Constant Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_type_mismatch_of_unary(self):
        input = """
        Class Program {
            main() {
                Var a : Int;
                a = - "2";
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,StringLit(2))"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_type_mismatch_of_unary_bool(self):
        input = """
        Class Program {
            main() {
                Var a : Boolean;
                a = ! (12);
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(12))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_binary_op(self):
        input = """
        Class Program {
            main() {
                Var a : Int;
                a = a + "haha";
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(haha))"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_binary_op_devide(self):
        input = """
        Class Program {
            main() {
                Var result : Int;
                result = 4 / 2;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(result),BinaryOp(/,IntLit(4),IntLit(2)))"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_binary_op_percent(self):
        input = """
        Class Program {
            main() {
                Var result : Int;
                result = 4 % 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLit(4),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_binary_op_compare(self):
        input = """
        Class Program {
            main() {
                Var result : Int;
                result = 4 >= 2;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(result),BinaryOp(>=,IntLit(4),IntLit(2)))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_binary_op_compare_diff_type(self):
        input = """
        Class Program {
            main() {
                Var result : Boolean;
                result = (12 > "good");
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,IntLit(12),StringLit(good))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_binary_op_and(self): #?
        input = """
        Class Program {
            main() {
                Var result : Boolean;
                result = True && 2;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,BooleanLit(True),IntLit(2))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_binary_op_string_compare(self):
        input = """
        Class Program {
            main() {
                Var result : Boolean;
                result = "haha" ==. 2;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==.,StringLit(haha),IntLit(2))"
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_binary_op_string_concat(self):
        input = """
        Class Program {
            main() {
                Var result : Int;
                result = "haha" +. "hehe";
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(result),BinaryOp(+.,StringLit(haha),StringLit(hehe)))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_if_stmt(self): #?
        input = """
        Class Program {
            main() {
                Var a : Int = 1;
                Var b : Int = 2;
                
                If (1) {
                    a = a + 1;
                }
                Else {
                    a = a - 1;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]))"
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_if_stmt2(self): #?
        input = """
        Class Program {
            main() {
                Var a : Int = 1;
                Var b : Int = 2;
                
                If (a > b) {
                    Var c : Int = 1;
                    a = a + c;
                }
                Else {
                    a = a - 1;
                    a = a + c;
                }
            }
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_for_stmt(self):
        input = """
        Class Program {
            main() {
                Var b : Int = 0;
                Foreach (a In 1 .. 100 By 2) {
                        a = a + 3;
                }
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_for_stmt2(self):
        input = """
        Class Program {
            main() {
                Var a, b : Int = 0, 0;
                Foreach (a In 1.5 .. 100 By 2) {
                        b = b + 3;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(a),FloatLit(1.5),IntLit(100),IntLit(2),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(3)))])])"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_for_stmt3(self):
        input = """
        Class Program {
            main() {
                Var a, b : Int = 0, 0;
                Foreach (a In 1 .. 100 By 2.5) {
                        b = b + 3;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(a),IntLit(1),IntLit(100),FloatLit(2.5),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(3)))])])"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_break_not_in_loop(self):
        input = """
        Class Program {
            main() {
                Var a, b : Int = 0, 0;
                Break;
                Foreach (a In 1 .. 100 By 2) {
                        b = b + 3;
                }
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_continue_not_in_loop(self):
        input = """
        Class Program {
            main() {
                Var a, b : Int = 0, 0;
                Foreach (a In 1 .. 100 By 2) {
                        b = b + 3;
                        Break;
                }
                Continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_array_cell(self):
        input = """
        Class Program {
            main() {
                Var arr: Array[Int, 5] = Array(1, 3, 5, 7, 9);
                arr[1] = 12.5;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),FloatLit(12.5))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_array_cell2(self): # check
        input = """
        Class Program {
            main() {
                Var arr: Array[Int, 5] = Array(1, 3, 5, 7, 9);
                arr[1] = arr[2] * 2.0;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),BinaryOp(*,ArrayCell(Id(arr),[IntLit(2)]),FloatLit(2.0)))"
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_array_cell3(self): #?
        input = """
        Class Program {
            main() {
                Var arr: Array[Int, 5] = Array(1, 3, 5, 7, 9);
                arr[1][2.5] = 12;
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),[IntLit(1),FloatLit(2.5)])"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_array_cell4(self):
        input = """
        Class Program {
            main() {
                Var a: Int = 1;
                a[0] = 12;
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(0)])"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_new_expr(self):
        input = """
        Class myClass {

        }
        Class Program {
            main() {
                Var a: myClass = New Ast();
            }
        }
        """
        expect = "Undeclared Class: Ast"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_new_expr2(self): # ?
        input = """
        Class myClass {

        }
        Class Program {
            main() {
                Var a: Test = New Test();
            }
        }
        """
        expect = "Undeclared Class: Test"
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test_constructor(self):
        input = """
        Class myClass {
            myFun() {

            }
        }
        Class Program {
            main() {
                Var a: myClass = New myClass(1, 2);
            }
        }
        """
        expect = "Undeclared Method: Constructor"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_constructor2(self):
        input = """
        Class myClass {
            Constructor(a, b, c: Int) {

            }
            main() {

            }
        }
        Class Program {
            main() {
                Var a: myClass = New myClass(1, 2);
            }
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(myClass),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_constructor3(self):
        input = """
        Class myClass {
            Constructor(a, b: Int) {

            }
            myFun() {

            }
        }
        Class Program {
            main() {
                Var a: myClass = New myClass(1, 2.5);
            }
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(myClass),[IntLit(1),FloatLit(2.5)])"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_fieldAccess_self(self):
        input = """
        Class Program {
            Var a: Int = 1;
            main() {
                Var b: Int;
                b = Self.c;
            }
        }
        """
        expect = "Undeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_fieldAccess(self):
        input = """
        Class myClass {
            Var c: Int = 1;
        }
        Class Program {
            Var a: Int = 1;
            main() {
                Var obj: myClass = New myClass();
                Var b: Int;
                b = obj.d;
            }
        }
        """
        expect = "Undeclared Attribute: d"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_fieldAccess2(self):
        input = """
        Class myClass {
            Var c: Int = 1;
        }
        Class Program {
            Var a: Int = 1;
            main() {
                Var obj: myClass = New myClass();
                Var b: Int;
                b = abc.c;
            }
        }
        """
        expect = "Undeclared Class: abc"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_return_stmt(self):
        input = """
        Class Program {
            main() {
                Var a: Int = 1;
                Return b;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_return_stmt2(self): # use Self
        input = """
        Class Program {
            Var a: Int = 1;
            main() {
                Var b: Int = 1;
                Return a;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_return_stmt2(self):
        input = """
        Class Program {
            Val $numOfShape: Int = 0;
            main() {

            }
            $getNumOfShape() {
                Return mud::$numOfShape;
            }
        }
        """
        expect = "Undeclared Class: mud"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_return_stmt3(self): # chua fixxx
        input = """
        Class Program {
            Val $numOfShape: Int = 0;
            main() {

            }
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        """
        expect = "Undeclared Identifier: $numOfShape"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_callExpr(self):
        input = """
        Class Program {
            main() {
                Return Program::$getName();
            }
            $getNumOfShape() {
                Return 2;
            }
        }
        """
        expect = "Undeclared Method: $getName"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_callExpr2(self):
        input = """
        Class Program {
            main() {
                Return Program::$getSum();
            }
            $getSum(a, b: Int) {
                Return a + b;
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(Program),Id($getSum),[])"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_callExpr3(self):
        input = """
        Class Program {
            main() {
                Return Program::$getSum(1, 2.5);
            }
            $getSum(a, b: Int) {
                Return a + b;
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(Program),Id($getSum),[IntLit(1),FloatLit(2.5)])"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_callExpr4(self):
        input = """
        Class myClass {
            $getSum(a, b: Int) {
                Return a + b;
            }
        }
        Class Program {
            main() {
                Return myClass::$getAdd(1, 2);
            }
        }
        
        """
        expect = "Undeclared Method: $getAdd"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_var_type_decl(self): # chua check
        input = """
        Class Program {
            Var a: Int = 13.5;
            main() {
                
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),IntType,FloatLit(13.5))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_var_type_decl2(self):
        input = """
        Class Program {
            main() {
                Var a: String = 54;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),StringType,IntLit(54))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_callStmt(self):
        input = """
        Class myClass {
            $printName() {

            }
        }
        Class Program {
            main() {
                Var obj: myClass = New myClass();
                myObj::$printName();
            }
        }
        """
        expect = "Undeclared Class: myObj"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_callStmt2(self):
        input = """
        Class myClass {
            $printName() {

            }
        }
        Class Program {
            main() {
                Var obj: myClass = New myClass();
                obj::$printSum();
            }
        }
        """
        expect = "Undeclared Method: $printSum"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_no_entry_point2(self):
        input = """
        Class myClass {

        }
        Class Program {
            
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,456))
    
    def test_no_entry_point3(self): # not real main
        input = """
        Class Program {
            main(a, b: Int) {

            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_class_inherit_class(self):
        input = """
        Class myClass: myClass {
            myFun() {

            }
        }
        """
        expect = "Undeclared Class: myClass"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_member_access(self):
        input = """
        Class E {
            Var a : Int;
            myFun() {

            }
        }
        Class Program {
            main() {
                    Var b : Int = E.a;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(E),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_array_decl(self):
        input = """
        Class Program {
            Var a: Array[Int, 1] = Array(1, 2, 3, 4);
            main() {

            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),ArrayType(1,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_array_decl2(self):
        input = """
        Class Program {
            Var a: Array[Int, 1] = Array(True);
            main() {

            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),ArrayType(1,IntType),[BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_for_stmt4(self):
        input = """
        Class A {
            foo() {
                Val x : Int = 10;
                Foreach(x In 1 .. 100 By 1)
                {

                }
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(x),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_class_declare_with_order(self):
        input = """
        Class Program: myClass {
            main() {

            }
        }
        Class myClass {

        }
        """
        expect = "Undeclared Class: myClass"
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_class_declare_with_order2(self):
        input = """
        Class BClass {

        }
        Class Program {
            main() {
                Var obj: myClass = New myClass();
            }   
        }
        Class myClass {

        }
        """
        expect = "Undeclared Class: myClass"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_break_stmt(self):
        input = """
        Class Program {
            main() {
                Var x: Int;
                Var a: Int;
                Foreach(x In 1 .. 100 By 1)
                {
                    a = 12 + x;
                }
                {
                    Break;
                }
            }   
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_no_entry_point4(self):
        input = """
        Class myClass {
            func() {
                Var a: Int;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_random_input1(self):
        input = """
        Class Program {
            main() {
                If (1) {
                    Var i: Int = 1;
                    Foreach (i In 0 .. 1000 By 1) {

                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(IntLit(1),Block([VarDecl(Id(i),IntType,IntLit(1)),For(Id(i),IntLit(0),IntLit(1000),IntLit(1),Block([])])]))"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_random_input2(self):
        input = """
        Class Program {
            main() {
                If (True) {
                    Var i: Int = 1;
                    Val b: Int = 2;
                    Foreach (i In 0 .. 1000 By "12") {

                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(0),IntLit(1000),StringLit(12),Block([])])"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_random_input3(self):
        input = """
        Class Program {
            main() {
                If (True) {
                    Var a: Int = 2;
                }
                Else {
                    a = a + 1;
                }
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_random_input4(self):
        input = """
        Class Program {
            main() {
                Var a: Int = 2;
                Var b: Boolean = True;

                If(a && b) {
                    a = a + 1;
                }
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_random_input5(self):
        input = """
        Class Program {
            main() {
                Var str: String = "12";
                Var result: String;
                result = str + "abcd";
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(str),StringLit(abcd))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_random_input6(self):
        input = """
        Class Program {
            main() {
                Var str: String = "12";
                Var result: String;
                result = (str +. "abcd") == "12abcd";
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,BinaryOp(+.,Id(str),StringLit(abcd)),StringLit(12abcd))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_random_input7(self):
        input = """
        Class Program {
            main() {
                Var lst: Array[Int, 4] = Array(1, 2, 3, 4);
                lst["1"] = 12;
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(lst),[StringLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_random_input8(self):
        input = """
        Class Program {
            main() {
                Var lst: Array[Int, 4] = Array(1, 2, 3, 4);
                lst[1 * 2.0] = 12;
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(lst),[BinaryOp(*,IntLit(1),FloatLit(2.0))])"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_random_input9(self):
        input = """
        Class myClass {
            printName() {

            }
            $printAge() {

            }
        }
        Class Program {
            main() {
                Var obj: myClass = New myClass();
                obj.$printAge();
            }
        }
        """
        expect = "Illegal Member Access: Call(Id(obj),Id($printAge),[])"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_random_input10(self):
        input = """
        Class myClass {
            Var $a: Int;
            $printAge() {

            }
        }
        Class Program {
            main() {
                Var obj: myClass = New myClass();
                obj.$a = 1;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(obj),Id($a))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_random_input11(self):
        input = """
        Class myClass {
            Var $a: Int;
            $printAge() {

            }
        }
        Class Program {
            main() {
                Var obj: myClass = New myClass();
                obj.$printAge();
            }
        }
        """
        expect = "Illegal Member Access: Call(Id(obj),Id($printAge),[])"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_random_input12(self):
        input = """
        Class myClass {
            Var $a: Int;
            getAge() {

            }
        }
        Class Program {
            main() {
                Var result: Int;
                result = myClass::getAge();
            }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(myClass),Id(getAge),[])"
        self.assertTrue(TestChecker.test(input,expect,478))
    
    def test_random_input13(self):
        input = """
        Class Program {
            getAge() {
                Return 1;
            }
            getName() {
                Return 2;
            }
            main() {
                Var result: Int = Self.getHeight();
            }
        }
        """
        expect = "Undeclared Method: getHeight"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_random_input14(self):
        input = """
        Class myClass {

        }
        Class Program {
            main() {
                Var a: myClass = New myClass(1, 2);
            }
        }
        """
        expect = "Undeclared Method: Constructor"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_random_input15(self):
        input = """
        Class Program {
            main() {
                Var i: String;
                Foreach(i In 1 .. 10) {
                    
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([])])"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_random_input16(self):
        input = """
        Class Program {
            Var i: String;
            Var j: String;
            main() {
                Var result: String;
                result = Self.i +. Self.j;
                result = True;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(result),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_random_input17(self):
        input = """
        Class Program {
            Var i: String;
            Var j: String;
            main() {
                Var result: String;
                result = Self.i +. Self.j;
                result = True;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(result),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_random_input18(self):
        input = """
        Class Program {
            main() {
  
            }
        }
        Class A {
            getAge() {
                Return 1;
            }
        }
        Class B: A {
            Var age : Int = Self.getAge();
            Var height: Int = Self.getHeight();
        }
        """
        expect = "Undeclared Method: getHeight"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_random_input19(self):
        input = """
        Class Program {
            main() {
  
            }
        }
        Class A {
            Var age: Int;
        }
        Class B: A {
            myFun() {
                Self.ages = 1;
            }
        }
        """
        expect = "Undeclared Attribute: ages"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_random_input20(self):
        input = """
        Class Program {
            main() {
                Program = 12;
            }
        }
        """
        expect = "Undeclared Identifier: Program"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_random_input21(self):
        input = """
        Class Program {
            main() {
                main = 12;
            }
        }
        """
        expect = "Undeclared Identifier: main"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_random_input22(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([])
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("myVar"),
                                StringType(),
                                StringLiteral("Hello World")
                            )
                        ),
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("myVar"),
                                IntType()
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Redeclared Attribute: myVar"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_random_input23(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block(
                                [
                                    Assign(
                                        Id("myVar"),
                                        IntLiteral(10)
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Undeclared Identifier: myVar"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_random_input24(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block([
                                ConstDecl(
                                    Id("myVar"),
                                    IntType(),
                                    IntLiteral(5)
                                ),
                                Assign(
                                    Id("myVar"),
                                    IntLiteral(10)
                                )]
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Cannot Assign To Constant: AssignStmt(Id(myVar),IntLit(10))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_random_input25(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block(
                                [
                                    Break()
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_random_input26(self):
        input = Program(
            [
                ClassDecl(
                    Id("Program"),
                    [
                        MethodDecl(
                            Static(),
                            Id("main"),
                            [],
                            Block(
                                [
                                    ConstDecl(
                                        Id("myVar"),
                                        IntType(),
                                        FloatLiteral(1.2)
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(myVar),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_random_input27(self):
        input = """
        Class Program {
            testFun() {
                Var a, b: Int = 1, 2;
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
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_random_input28(self):
        input = """
        Class Program {
            main() {
                Var a, b: Int = 1, 2;
                If (a > b) {
                    a = a + 1;
                }
                Elseif (a < b) {
                    a = a / b;
                }
                Else {
                    a = a * 2;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(/,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_random_input29(self):
        input = """
        Class Program {
            main() {
                Var arr: Array[Int, 5] = Array(1, 2, 3, 4, 5);
                If (arr[0] > arr[1] || "array") {

                }
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,ArrayCell(Id(arr),[IntLit(1)]),StringLit(array))"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_random_input30(self):
        input = """
        Class Program {
            main() {
                Var arr0: Int;
                Val arr: Int;
            }
        }
        """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_random_input31(self):
        input = """
        Class Program {
            main() {
                
            }
            testFunc() {
                Var i: Int;
                Foreach (i In 0 .. 12 By 3)
                {
                    x = x * x + (3/2)*x + 9;
                }
            }
        }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_random_input32(self):
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
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_random_input33(self):
        input = """
        Class Program {
            Var a, b, c: Float = 1.0, 2.0 ,3.0;
            main() {
                Var a: Float = a + 0.527e-2;
                Var b: Float = b * (5.72 / 12e-6);
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_random_input34(self):
        input = """
        Class Program {
            main() {
                Var a: Float = b * c + d / e - f;
                z = "Hello" +. "World";
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,500))
