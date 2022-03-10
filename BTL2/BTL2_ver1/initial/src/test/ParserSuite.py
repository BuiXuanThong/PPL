import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """
        Class Shape { }
        Class Circle { }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_more_complex_program(self):
        input = """Class Shape {
            testFunc() { }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_wrong_miss_close(self):
        input = """Class Shape {
            testFunc( { }
        }"""
        expect = "Error on line 2 col 22: {"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_class_declaration(self):
        """Simple class"""
        input = """Class Shape_of_u { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_class_inheritance(self):
        """Simple class"""
        input = """Class Shape: Circle { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_fucntion_declaration(self):
        """Simple func"""
        input = """Class Shape {
            $getAllName() {}
            getAllStudent() {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_var_declaration(self):
        """Simple var declare"""
        input = """Class Shape {
            Val $immutableAttribute: Int = 23;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_multiline_var_declaration(self):
        """Simple var declare"""
        input = """Class Shape {
            Val $immutableAttribute: Int = 23;
            Var testNum: Float = 58;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_multivar_inline_declaration(self):
        """Simple var declare"""
        input = """Class Shape {
            Var length, width: Int;
            Var height, top: Int = 72, 13;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_more_complex_class_var_func(self):
        """class and var and func"""
        input = """Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {

            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_paramlist(self):
        """paramlist declaration"""
        input = """Class Shape {
            $getNumOfShape(My1stCons, My2ndCons: Int; MyFloat: Float) {

            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_arithmetic_operator(self):
        """arithmetic operator"""
        input = """Class Test {
            Var myVar1: Int = 3 * 2 + 6;
            Var myVar2: Int = 3 % 2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_relation_operators(self):
        """relation operators"""
        input = """Class Test {
            Var myVar1: Int = (3 < 2);
            Var myVar2: Int = ((5 >= 2) || (5 == 2));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_func_call(self):
        """Function call ( )"""
        input = """Class Test {
            Var myVar1: Int = Shape::$getNum(12 + 6);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_if_statement(self):
        """if statement"""
        input = """Class Test {
            $getNumOfShape(My1stCons, My2ndCons: Int; MyFloat: Float) {
                If(3 > 2) {My1stCons = 3 + 6;}
                Else {My1stCons = 99;}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_elseif_statement(self):
        """elif statement"""
        input = """Class Test {
             $getNumOfShape(My1stCons, My2ndCons: Int; MyFloat: Float) {
                If(3 > 2) {My1stCons = 3 + 6;}
                Elseif(My1stCons > 9) {My1stCons = 11;}
                Else {My1stCons = 99;}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_assign_statement(self):
        """assign statement"""
        input = """Class Test {
             $getNumOfShape(var1, var2: Int; var3: Float) {
                var1 = var2;
                var2 = 9;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_foreach_statement(self):
        """foreach in"""
        input = """Class Test {
            myTestFunc(var1, var2: Int; var3: Float) {
                Foreach (var1 In 1 .. 100 By 2) {
                    var2 = var2 + 3;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_break_statement(self):
        """break"""
        input = """Class Test {
            myTestFunc(var1, var2: Int; var3: Float) {
                Foreach (var1 In 1 .. 100 By 2) {
                    If(3 == 2) {
                        var2 = 14 * 9;
                        Break;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_continue_statement(self):
        """continue"""
        input = """Class Test {
            myTestFunc(var1, var2: Int; var3: Float) {
                Foreach (var1 In 1 .. 100 By 2) {
                    If(3 == 2) {
                        var2 = 14 * 9;
                        Continue;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_return_statement(self):
        """return"""
        input = """Class Test {
            myTestFunc(var1, var2: Int; var3: Float) {
                Foreach (var1 In 1 .. 100 By 2) {
                    If(3 == 2) {
                        var2 = 14 * 9;
                        Return var2;
                    }
                }
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_var_declaration_but_compare_number_param(self):
        input = """Class Test {
            Val a, b: Int = 2,3;

            ##FunnyFunc() {
                Val a, b: Int = 2, 3, 4;
            }##
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_break_stmt_outside_loop(self):
        input = """Class Test {
            myTestFunc(var1, var2: Int; var3: Float) {
                Foreach (var1 In 1 .. 100 By 2) {
                    Break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_return_stmt_outside_func(self):
        input = """Class Test {
            Return;
            myTestFunc() {
                
            }
        }"""
        expect = "Error on line 2 col 12: Return"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_method_invocation_statement(self):
        input = """Class Test {
            myTestFunc() {
                Shape::$getNumOfShape();
                Out.printInt(i);
                Out.printInt(Shape::$numOfShape);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_fake_return(self):
        input = """Class A {
            testing() {
                ss = r * r * Self.myPI;
                return ss;
            }
        }"""
        expect = "Error on line 4 col 23: ss"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_index_operator(self):
        input = """Class A {
            testing() {
                a[2][4] = a[5][6];
                Self.var = 14;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_index_operator_with_var(self):
        input = """Class A {
            testing() {
                arr[i] = 5;
                arr[5] = x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_index_operator_but_fail(self):
        input = """Class A {
            testing() {
                a[2][4] = a[5][6;
            }
        }"""
        expect = "Error on line 3 col 32: ;"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_simple_block_stmt(self):
        input = """Class A {
            testing() {
                Out.printInt(arr[x]);
                {
                    arr[5] = 12;
                    arr[6] = 19;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_block_stmt_but_empty(self):
        input = """Class A {
            testing() {
                Out.printInt(arr[x]);
                {
                }
                { }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_block_stmt_inside_block_stmt(self):
        input = """Class A {
            testing() {
                Out.printInt(arr[x]);
                {
                    { myVar = 12; }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_array_type(self):
        input = """Class A {
            Var a:Array[Int, 1];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_destructor(self):
        input = """Class A {
            Destructor() {Return;}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_destructor_but_fail(self): # with param
        input = """Class A {
            Destructor(var1: Int) {}
        }"""
        expect = "Error on line 2 col 23: var1"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_constructor(self):
        input = """Class A {
            Constructor(var1: Int) {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_constructor2(self):
        input = """Class A {
            Constructor() {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_constructor_with_other_func(self):
        input = """Class A {
            Constructor() {}
            MyTest() {
                Foreach (var1 In 50 .. 100 By 5) {
                    Break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_destructor_with_other_func(self):
        input = """Class A {
            Destructor() {}
            MyTest() {
                Foreach (var1 In 50 .. 100 By 5) {
                    Break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_constructor_destructor_with_other_func(self):
        input = """Class A {
            Constructor() {var1 = 0;}
            Destructor() {}
            MyTest() {
                Foreach (var1 In 50 .. 100 By 5) {
                    Break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_assign_stmt_but_multi_assign(self):
        input = """Class A {
            Constructor() {var1 = 0;}
            Destructor() {}
            MyTest() {
                var1 = 12;
                var1 = 12 = 13;
            }
        }"""
        expect = "Error on line 6 col 26: ="
        self.assertTrue(TestParser.test(input,expect,241))
    def test_if_stmt_but_no_else(self):
        input = """Class A {
            Constructor() {var1 = 0;}
            Destructor() {}
            MyTest() {
                If(var1 > 12) { }
                Elseif(var1 < 4) { }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_if_stmt_but_else_before_elseif(self):
        input = """Class A {
            Constructor() {var1 = 0;}
            Destructor() {}
            MyTest() {
                If(var1 > 12) { }
                Else(var1 < 4) { }
                Elseif(var1 == 4) { }
            }
        }"""
        expect = "Error on line 6 col 20: ("
        self.assertTrue(TestParser.test(input,expect,243))
    def test_if_stmt_inside_foreach(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_if_stmt_inside_if(self):
        input = """Class A {
            Constructor() {}
            Destructor() {}
            MyTest() {
                If (var1 > 62) {
                    If(var1 < 70) {var1 = var1 -2;}
                }
                Else {var1 = var1 + 1;}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_foreach_stmt_inside_if(self):
        input = """Class A {
            Constructor() {}
            Destructor() {}
            MyTest() {
                If (var1 > 62) {
                    If(var1 < 70) {
                        Foreach (var1 In 90 .. 100 By 1) { }
                    }
                }
                Else {var1 = var1 + 1;}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_foreach_stmt_inside_foreach(self):
        input = """Class A {
            Constructor() {}
            Destructor() {}
            MyTest() {
                Foreach (var1 In 90 .. 100 By 1) {
                    Foreach (var2 In 10 .. 100 By 5) {
                        Break;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_foreach_stmt_without_by(self):
        input = """Class A {
            MyTest() {
                Foreach (var1 In 90 .. 100) {
                    Foreach (var2 In 10 .. 100) {
                        Break;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_array_decl_with_value(self):
        input = """Class A {
            MyTest() {
                Var myArray: Array[Int, 5] = Array(1, 3, 5, 7, 9);
                myArray[2] = 12;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_array_decl_with_value_but_fail(self):
        input = """Class A {
            MyTest() {
                Var myArray: Array[Int, 5] = Array(1, 3, 5, 7, 9,);
                myArray[2] = 12;
            }
        }"""
        expect = "Error on line 3 col 65: )"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_array_decl_with_value_but_fail2(self):
        input = """Class A {
            MyTest() {
                Var myArray: Array(Int, 5) = Array(1, 3, 5, 7, 9);
                myArray[2] = 12;
                myArray[3] = 5;
            }
        }"""
        expect = "Error on line 3 col 34: ("
        self.assertTrue(TestParser.test(input,expect,251))
    def test_var_decl_inside_method(self):
        input = """Class A {
            MyTest() {
                Var a, b, c: Int;
                Val x, y, z: Float;
                a = b + c;
                b = y * z;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_var_decl_inside_method_but_fail(self):
        input = """Class A {
            MyTest() {
                Var a, $b, c: Int;
                Val x, y, z: Float;
                a = b + c;
                b = y * z;
            }
        }"""
        expect = "Error on line 3 col 23: $b"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_var_decl_in_and_outside_method(self):
        input = """Class A {
            Var $name, $age: Int;
            Val birth: Int;
            MyTest() {
                Var a, b, c: Int;
                Val x, y, z: Float;
                a = b + c;
                b = y * z;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_var_decl_in_and_outside_method_with_call(self):
        input = """Class A {
            Var $name, $age: Int;
            Val birth: Int;
            MyTest() {
                Var a, b, c: Int;
                Val x, y, z: Float;
                a = b + c;
                b = y * z;
                birth = Person::$getMyDay();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_number_with_sign_op(self):
        input = """Class A {
            MyTest() {
                Var a, b, c: Int;
                Val x, y, z: Float;
                a = -12 + 9;
                b = -3 -5 -7;
                c = 127 *-12 + (-3);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_number_inside_LP(self):
        input = """Class A {
            MyTest() {
                Var a, b, c: Int;
                Val x, y, z: Float;
                a = ((12 * 35) + 137/2 - -14)*(10 * (-16));
                Return a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_number_with_unclosed_LP(self):
        input = """Class A {
            MyTest() {
                Var a, b, c: Int;
                Val x, y, z: Float;
                a = ((12 * 35) + 137/2 - -14)*(10 * (-16);
                Return a;
            }
        }"""
        expect = "Error on line 5 col 57: ;"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_number_with_fake_LP(self):
        input = """Class A {
            MyTest() {
                Var a, b, c: Int;
                Val x, y, z: Float;
                a = ((12 * 35} + 137/2 - -14)*(10 * (-16));
                Return a;
            }
        }"""
        expect = "Error on line 5 col 29: }"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_number_remainder_op(self):
        input = """Class A {
            MyTest() {
                Var a, b, c: Int;
                a = ((b + c) % c) + (c % a);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_number_remainder_op_but_fail(self):
        input = """Class A {
            MyTest() {
                Var a, b, c: Int;
                a = ((b + c) %% c) + (c % a);
            }
        }"""
        expect = "Error on line 4 col 30: %"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_string_op(self):
        input = """Class A {
            MyTest() {
                Var str: String;
                If("goodbye" ==. "goodluck") {
                    str = "goodbye" +. "goodluck";
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_boolean_with_var(self):
        input = """Class A {
            MyTest() {
                Var yes: Boolean;
                yes = (True && False) || (False || (3 != 2) || (5 >= 3));
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_boolean_with_var_but_fail(self):
        input = """Class A {
            MyTest() {
                Var yes, no: Boolean;
                yes = (True && False) || (False || (3 != 2) || (5 >> 3));
                no = False;
            }
        }"""
        expect = "Error on line 4 col 67: >"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_block_comment_on_error(self):
        input = """Class A {
            MyTest() {
                Var yes, no: Boolean;
                ## yes = (True && False) || (False || (3 != 2) || (5 >> 3)); ##
                no = False;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_index_operator_but_fail2(self):
        input = """Class A {
            MyTest() {
                a[5] = 14;
                a[[5]] = 12;
            }
        }"""
        expect = "Error on line 4 col 18: ["
        self.assertTrue(TestParser.test(input,expect,266))
    def test_call_other_func(self):
        input = """
        Class Shape {
            $callMeNow() {
                Return 123;
            }
        }
        Class A {
            MyTest() {
                Shape::$callMeNow();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    def test_call_other_func_but_fail(self): # without dollar
        input = """
        Class Shape {
            $callMeNow() {
                Return 123;
            }
            $callMeLater(a, b: Int) {
                Return a * b;
            }
        }
        Class A {
            MyTest() {
                Shape::callMeNow();
                Shape::$callMeLater(12, 3);
            }
        }"""
        expect = "Error on line 12 col 23: callMeNow"
        self.assertTrue(TestParser.test(input,expect,268))
    def test_random_mixing1(self):
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
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_random_mixing2(self):
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
                Out.printInt(Shape:$callMeLater(1, 2));
            }
        }"""
        expect = "Error on line 12 col 34: :"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_random_mixing3(self):
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
                Out.printInt(Shape.$callMeLater(1, 2));
            }
        }"""
        expect = "Error on line 12 col 35: $callMeLater"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_random_mixing4(self): # ???
        input = """
        Class Shape {
            Var a, b, c: Int = 1, 2, 3;
            a = a + 2;
            $testFunc() {
                b = a * 2;
            }
        }
        Class Program {
            main() {
                Shape::testFunc();
            }
        }"""
        expect = "Error on line 4 col 14: ="
        self.assertTrue(TestParser.test(input,expect,272))
    def test_random_mixing5(self): # ???
        input = """
        Class Shape {
            Var a, b, c: Int = 1, 2, 3;
            Foreach (a In 1 .. 100 By 2) {
                    a = a + 3;
            }
            $testFunc() {
                b = a * 2;
            }
        }
        Class Program {
            main() {
                Shape::testFunc();
            }
        }"""
        expect = "Error on line 4 col 12: Foreach"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_random_mixing6(self): # class inside class ?
        input = """
        Class Program {
            main() { }
            Class Shape {
                Var a, b, c: Int = 1, 2, 3;
                Foreach (a In 1 .. 100 By 2) {
                        a = a + 3;
                }
            }
        }"""
        expect = "Error on line 4 col 12: Class"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_random_mixing7(self): # column 32 or 34 ???
        input = """
        Class Program {
            main() { }
            testFunc() {
                Foreach (i In 0 . . 12 By 3)
                {
                    x = x * x + (3/2)*x + 9;
                }
            }
        }"""
        expect = "Error on line 5 col 32: ."
        self.assertTrue(TestParser.test(input,expect,275))
    def test_var_vs_value(self):
        input = """
        Class Program {
            Var a, b, c: Int = 1, 2 ,3;
            main() { }
            testFunc() {
                Foreach (i In 0 .. 12 By 3)
                {
                    x = x * x + (3/2)*x + 9;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_var_vs_value_but_fail(self):
        input = """
        Class Program {
            Var a, b, c: Int = 1, 2;
            main() { }
            testFunc() {
                Foreach (i In 0 .. 12 By 3)
                {
                    x = x * x + (3/2)*x + 9;
                }
            }
        }"""
        expect = "Error on line 3 col 35: ;"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_var_vs_value_but_fail2(self):
        input = """
        Class Program {
            Var a, b, c: Int = 1, 2, 3, 4;
            main() { }
            testFunc() {
                Foreach (i In 0 .. 12 By 3)
                {
                    x = x * x + (3/2)*x + 9;
                }
            }
        }"""
        expect = "Error on line 3 col 38: ,"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_var_vs_value_stmt_inside_method(self):
        input = """
        Class Program {
            main() {
                Var a, b, c: Int = 1, 2, 3, 4;
            }
            testFunc() {
                Foreach (i In 0 .. 12 By 3)
                {
                    x = x * x + (3/2)*x + 9;
                }
            }
        }"""
        expect = "Error on line 4 col 42: ,"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_random_mixing8(self):
        input = """
        Class Program {
            main() {
                Var a, b, c: Int = 1, 2, 3, 4;
            }
            testFunc() {
                Foreach (i In 0 .. 12 By 3)
                {
                    x = x * x + (3/2)*x + 9;
                }
            }
        }"""
        expect = "Error on line 4 col 42: ,"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_random_mixing9(self):
        input = """
        Class Shape {
            Val a, b: Int = (1 + 12)*6, 3 * 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_random_mixing10(self):
        input = """
        Class Shape {
            Val a, b: String = "abc %", "## ##";
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_random_mixing11(self):
        input = """
        Class Shape {
            testFunc() {
                str = "$ $ $ @@ ***" +. "(0)_(0)";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_random_mixing12(self):
        input = """
        Class Shape {
            testFunc() {
                str += "$ $ $ @@ ***" +. "(0)_(0)";
            }
        }
        """
        expect = "Error on line 4 col 21: ="
        self.assertTrue(TestParser.test(input,expect,284))
    def test_random_mixing13(self):
        input = """
        Class Shape {
            testFunc() {
                {
                    Var r, s: Int;
                    r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self.myPI;
                        a[0] = s;
                    }
                }
            }
        }
        """
        expect = "Error on line 13 col 8: }"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_random_mixing14(self): ## ???
        input = """
        Class Program {
            main() { }
            testFunc() {
                Self.name = "abc";
                Self .age = "12";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_random_mixing15(self):
        input = """
        Class Program {
            main() { }
            testFunc() {
                testFunc2() {
                    Var a, b: Int;
                    a = 20;
                }
            }
        }"""
        expect = "Error on line 5 col 25: ("
        self.assertTrue(TestParser.test(input,expect,287))
    def test_random_mixing16(self):
        input = """
        Class Shape {
            Var a, b: Int;
            testFunc(c, d: Int;) { }
        }
        """
        expect = "Error on line 4 col 31: )"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_random_mixing17(self):
        input = """
        Class Shape {
            Var a, b: Int;
            testFunc(##c, d##) { }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_random_mixing18(self):
        input = """
        Class Shape {
            Var a, b: String;
            testFunc() {
                a = "with some \\t \\r";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
    def test_random_mixing19(self):
        input = """
        Class Shape { }
        Class ComplexShape: Shape { }
        Class SimpleShape: Shape, ComplexShape { }
        """
        expect = "Error on line 4 col 32: ,"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_random_mixing20(self):
        input = """
        Class Shape {
            $myFunc() {
                 Class SimpleShape { }
            }
        }
        Class ComplexShape: Shape {
        }
        """
        expect = "Error on line 4 col 17: Class"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_random_mixing21(self):
        input = """
        Class Shape {
        };
        Class ComplexShape: Shape {
        }
        """
        expect = "Error on line 3 col 9: ;"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_random_mixing23(self): ## ???
        """boolean operators"""
        input = """Class Test {
            Var myVar1: Boolean = !(2 > 3);
            Var myVar2: Boolean = (2 == 3) && (2 == 2);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_random_mixing24(self):
        input = """Class Test {
            Var myVar1: Boolean = !(2 > 3);
            Var myVar2: Boolean == (2 == 3) && (2 == 2);
        }"""
        expect = "Error on line 3 col 32: =="
        self.assertTrue(TestParser.test(input,expect,295))
    def test_random_mixing25(self):
        input = """Class Test {
            Var myVar1: Shape = New Shape();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    def test_random_mixing26(self):
        input = """Class Test {
            Var myVar1: Shape = New Shape;
        }"""
        expect = "Error on line 2 col 41: ;"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_random_mixing27(self):
        input = """
            Class Program {
                main() {
                }
                test() {
                    Return $getName;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
    def test_random_mixing28(self):
        input = """
            Class Program {
                Foreach (var1 In 1 .. 100 By 2) {
                    var2 = var2 + 3;
                }
            }
            """
        expect = "Error on line 3 col 16: Foreach"
        self.assertTrue(TestParser.test(input, expect, 299))
    def test_random_mixing29(self):
        input = """
            Class Program {
                Var a: String = "Happy new yearrrrrrrrrrrrr";
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
    