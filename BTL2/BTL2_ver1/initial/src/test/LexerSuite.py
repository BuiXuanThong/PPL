import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",103))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123 a 123","123,a,123,<EOF>",104))
    def test_block_comment(self):
        """test block comments"""
        self.assertTrue(TestLexer.test("## my comments here ##","<EOF>",105))
    def test_comment_in_multiple_lines(self):
        self.assertTrue(TestLexer.test("""
        ## my comments here 
        enjoy
        goodluck
        ## 
        ""","<EOF>",106))
    def test_string_literal(self): # not ?
        """test string literals"""
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \\t" """,'This is a string containing tab \\t,<EOF>',107))
    def test_string_literal2(self): # not ?
        """test string literals 2"""
        self.assertTrue(TestLexer.test(""" "He asked me: '"Where is John?'"" ""","""He asked me: '"Where is John?'",<EOF>""",108))
    def test_float(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.234 1.2e3 7E-10 1_234.567","1.234,1.2e3,7E-10,1234.567,<EOF>",109))
    def test_int(self):
        """test int"""
        self.assertTrue(TestLexer.test("1234 0123 0x1A 0b11111111 1_234_567","1234,0123,0x1A,0b11111111,1234567,<EOF>",110))
    def test_boolean(self):
        """test boolean"""
        self.assertTrue(TestLexer.test("True 129_122 False ","True,129122,False,<EOF>",111))
    def test_int_array(self):
        """test int array"""
        self.assertTrue(TestLexer.test("Array(128129, 5,72.5, 7, 12) ","Array,(,128129,,,5,,,72.5,,,7,,,12,),<EOF>",112))
    def test_int_00_in_dec_or_oct(self):
        """test 00 in int or oct"""
        self.assertTrue(TestLexer.test("17 0 00","17,0,00,<EOF>",113))
    def test_unclosed_string(self):
        """unclosed string"""
        self.assertTrue(TestLexer.test(""" "abc def""","Unclosed String: abc def",114))
    def test_unclosed_string_with_newline(self): # chưa check
        """unclosed string with new line ?"""
        self.assertTrue(TestLexer.test(
        """ "abc
        def" ""","Unclosed String: abc",115))
    def test_illegal_escape_with_word(self):
        """Illegal Escape"""
        self.assertTrue(TestLexer.test(""" "abc def \\h xyz" ""","Illegal Escape In String: abc def \h",116))
    def test_illegal_escape_with_space(self):
        """Illegal Escape"""
        self.assertTrue(TestLexer.test(""" "abc def \\ xyz" ""","Illegal Escape In String: abc def \ ",117))
    def test_error_token(self):
        """simple error token"""
        self.assertTrue(TestLexer.test(""" 123_456? ""","123456,Error Token ?",118))
    def test_error_token2(self):
        """simple error token"""
        self.assertTrue(TestLexer.test(""" 123~abc ""","123,Error Token ~",119))
    def test_string_literal_multiple_lines(self):
        """string literal multiple lines"""
        self.assertTrue(TestLexer.test(
        """
        "goodbye"
        "friend"
        "see u soon"
        ""","goodbye,friend,see u soon,<EOF>",120))
    def test_string_literal_multiple_lines_and_escape(self):
        """string literal multiple lines and escape"""
        self.assertTrue(TestLexer.test(
        """
        "goodbye \\f"
        "friend"
        "see u soon \\n ok"
        ""","goodbye \\f,friend,see u soon \\n ok,<EOF>",121))
    def test_illegal_escape_with_2_escape(self):
        self.assertTrue(TestLexer.test(
            """ "Hello friend \\b \\z" """, "Illegal Escape In String: Hello friend \\b \\z", 122))
    def test_indexed_array(self):
        self.assertTrue(TestLexer.test(
            """ Array(1, 5, 7, 12) """, "Array,(,1,,,5,,,7,,,12,),<EOF>", 123))
    def test_indexed_array_with_string(self):
        self.assertTrue(TestLexer.test(
            """ Array("Kangxi", "Yongzheng", "Qianlong") """, "Array,(,Kangxi,,,Yongzheng,,,Qianlong,),<EOF>", 124))
    def test_multi_dimensional_array(self):
        self.assertTrue(TestLexer.test(
            """
            Array (
                Array("Volvo", "22", "18"),
                Array("Saab", "5", "2"),
                Array("Land Rover", "17", "15")
            )
            """, "Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>", 125))
    def test_some_keyword(self):
        self.assertTrue(TestLexer.test(
            """
            Break Continue If Elseif Else
            Foreach True False Array In
            Int Float Boolean String Return
            """, "Break,Continue,If,Elseif,Else,Foreach,True,False,Array,In,Int,Float,Boolean,String,Return,<EOF>", 126))
    def test_more_keyword(self):
        self.assertTrue(TestLexer.test(
            """
            Null Class Val Var
            Constructor Destructor New By Self
            """, "Null,Class,Val,Var,Constructor,Destructor,New,By,Self,<EOF>", 127))
    def test_some_operator(self):
        self.assertTrue(TestLexer.test(
            """
            + - * / %
            ! && || == =
            """, "+,-,*,/,%,!,&&,||,==,=,<EOF>", 128))
    def test_more_operator(self):
        self.assertTrue(TestLexer.test(
            """
            != > <= > >=
            ==. +. . :: New
            """, "!=,>,<=,>,>=,==.,+.,.,::,New,<EOF>", 129))
    def test_separator(self):
        self.assertTrue(TestLexer.test(
            """
            ( ) [ ] . , ; { }
            """, "(,),[,],.,,,;,{,},<EOF>", 130))
    def test_indentifier_with_underscore(self):
        self.assertTrue(TestLexer.test(
            """
            my_test_var MY_ID9
            """, "my_test_var,MY_ID9,<EOF>", 131))
    def test_int_literal_multiple_line(self):
        self.assertTrue(TestLexer.test(
            """
            199_152
            012743
            120_055_492
            0b101
            """, "199152,012743,120055492,0b101,<EOF>", 132))
    def test_int_literal_binary_but_fail(self):
        self.assertTrue(TestLexer.test(
            """
            0b1101
            0B0
            ## Not a binary ## 0b1201
            """, "0b1101,0B0,0b1,201,<EOF>", 133))
    def test_int_literal_hexa_but_fail(self):
        self.assertTrue(TestLexer.test(
            """
            0x23AB
            0X4952
            ## Not a hexa ## 0x33CYA
            """, "0x23AB,0X4952,0x33C,YA,<EOF>", 134))
    def test_float_literal_but_fail(self):
        self.assertTrue(TestLexer.test(
            """
            3.472
            15.0
            14E-10
            ## Not a hexa ## 153.25E
            """, "3.472,15.0,14E-10,153.25,E,<EOF>", 135))
    def test_float_literal_but_fail2(self):
        self.assertTrue(TestLexer.test(
            """
            3.2E19
            ## Not a hexa ## 3.2E.19
            """, "3.2E19,3.2,E,.,19,<EOF>", 136))

    def test_boolean_literal_with_number(self):
        self.assertTrue(TestLexer.test(
            """
            True 128_942 False 32.175 0x100
            """, "True,128942,False,32.175,0x100,<EOF>", 137))
    def test_boolean_literal_with_indexed_array(self):
        self.assertTrue(TestLexer.test(
            """
            Array(False, True, False)
            """, "Array,(,False,,,True,,,False,),<EOF>", 138))
    def test_unclosed_string_with_escape(self):
        self.assertTrue(TestLexer.test(
            """
            "hey bro what is your name \\r""", "Unclosed String: hey bro what is your name \\r", 139))
    def test_empty(self):
        self.assertTrue(TestLexer.test(
            """

            """, "<EOF>", 140))
    def test_int_literal_with_underscore(self):
        self.assertTrue(TestLexer.test(
            """
            120_475 0b1_101_010 0x34A_57F 0172_543
            """, "120475,0b1101010,0x34A57F,0172543,<EOF>", 141))
    def test_int_literal_with_failed_underscore(self):
        self.assertTrue(TestLexer.test(""" 123_456 78_910_ _192856""","123456,78910,_,_192856,<EOF>",142))
    def test_float_literal_after_fix(self):
        self.assertTrue(TestLexer.test("127.5e-10 127e-10 127.5 .5e-10","127.5e-10,127e-10,127.5,.5e-10,<EOF>",143))
    def test_float_literal_without_num_at_dot(self):
        self.assertTrue(TestLexer.test("129.17e10 129. 129.e10 .17e10","129.17e10,129.,129.e10,.17e10,<EOF>",144))
    def test_dollar_identifier(self):
        self.assertTrue(TestLexer.test("$123456 $abc123 $abc_123","$123456,$abc123,$abc_123,<EOF>",145))
    def test_dollar_identifier2(self):
        self.assertTrue(TestLexer.test("$_abc_ $0123 $__","$_abc_,$0123,$__,<EOF>",146)) # ?????
    def test_dollar_identifier_with_id(self):
        self.assertTrue(TestLexer.test("$abcdef abcdef $12742abc 12742abc","$abcdef,abcdef,$12742abc,12742,abc,<EOF>",147))
    def test_error_token3(self):
        self.assertTrue(TestLexer.test("a +- ^ == * >= % !","a,+,-,Error Token ^",148))
    def test_error_token4(self):
        self.assertTrue(TestLexer.test("( { /* . , */ } ) &","(,{,/,*,.,,,*,/,},),Error Token &",149))
    def test_error_token5(self):
        self.assertTrue(TestLexer.test(">> << ## `` ## @",">,>,<,<,Error Token @",150))
    def test_random_mixing(self):
        self.assertTrue(TestLexer.test(
        """Class Shape {
           myTest() {
               a = b;
           }
        }""","Class,Shape,{,myTest,(,),{,a,=,b,;,},},<EOF>",151))
    def test_random_mixing2(self):
        self.assertTrue(TestLexer.test(
        """
        Var a, b, c: Int;
        a = ((b + c) % c) + (c % a);
        ""","Var,a,,,b,,,c,:,Int,;,a,=,(,(,b,+,c,),%,c,),+,(,c,%,a,),;,<EOF>",152))
    def test_random_mixing3(self):
        self.assertTrue(TestLexer.test(
        """
        Var myArray: Array[Int, 5] = Array(1, 3, 5, 7, 9);
        myArray[2] = 12;
        ""","Var,myArray,:,Array,[,Int,,,5,],=,Array,(,1,,,3,,,5,,,7,,,9,),;,myArray,[,2,],=,12,;,<EOF>",153))
    def test_random_mixing4(self):
        self.assertTrue(TestLexer.test(
        """
        testing() {
                Out.printInt(arr[x]);
                {
                    { myVar = 12; }
                }
        }
        ""","testing,(,),{,Out,.,printInt,(,arr,[,x,],),;,{,{,myVar,=,12,;,},},},<EOF>",154))
    def test_random_mixing5(self):
        self.assertTrue(TestLexer.test(
        """
        myTestFunc(var1, var2: Int; var3: Float) {
                Break;
                Foreach (var1 In 1 .. 100 By 2) {
                    Break;
                }
        }
        ""","myTestFunc,(,var1,,,var2,:,Int,;,var3,:,Float,),{,Break,;,Foreach,(,var1,In,1,..,100,By,2,),{,Break,;,},},<EOF>",155))
    def test_random_mixing6(self):
        self.assertTrue(TestLexer.test(
        """
        $getNumOfShape(My1stCons, My2ndCons: Int; MyFloat: Float) {
                If(3 > 2) {My1stCons = 3 + 6;}
                Else {My1stCons = 99;}
        }
        ""","$getNumOfShape,(,My1stCons,,,My2ndCons,:,Int,;,MyFloat,:,Float,),{,If,(,3,>,2,),{,My1stCons,=,3,+,6,;,},Else,{,My1stCons,=,99,;,},},<EOF>",156))
    def test_random_mixing7(self):
        self.assertTrue(TestLexer.test(
        """
        Var yes: Boolean;
        yes = (True && False) || (False || (3 != 2) || (5 >= 3));
        ""","Var,yes,:,Boolean,;,yes,=,(,True,&&,False,),||,(,False,||,(,3,!=,2,),||,(,5,>=,3,),),;,<EOF>",157))
    def test_random_mixing8(self):
        self.assertTrue(TestLexer.test(
        """
        Var str: String;
        If("goodbye" ==. "goodluck") {
            str = "goodbye" +. "goodluck";
        }
        ""","Var,str,:,String,;,If,(,goodbye,==.,goodluck,),{,str,=,goodbye,+.,goodluck,;,},<EOF>",158))
    def test_random_mixing9(self):
        self.assertTrue(TestLexer.test(
        """
        Class Shape {
            $callMeNow() {
                Return 123;
            }
        }
        Class A {
            MyTest() {
                Shape::$callMeNow();
            }
        }
        ""","Class,Shape,{,$callMeNow,(,),{,Return,123,;,},},Class,A,{,MyTest,(,),{,Shape,::,$callMeNow,(,),;,},},<EOF>",159))
    def test_random_mixing10(self):
        self.assertTrue(TestLexer.test(
        """
        Foreach (var1 In 1 .. 100) {
            Foreach (var2 In 1 .. 100 By 5) {
                If(var1 > 12) { }
                Elseif(var1 < 4) { } 
            }
        }
        ""","Foreach,(,var1,In,1,..,100,),{,Foreach,(,var2,In,1,..,100,By,5,),{,If,(,var1,>,12,),{,},Elseif,(,var1,<,4,),{,},},},<EOF>",160))
    def test_number_literal_after_fix(self):
        self.assertTrue(TestLexer.test(
        """
        0B0 0b0 0x0 0X0 00 0
        ""","0B0,0b0,0x0,0X0,00,0,<EOF>",161))
    def test_number_literal_after_fix_but_fail(self):
        self.assertTrue(TestLexer.test(
        """
        0b1101 0b01101 ## not a binary ##
        ""","0b1101,0b0,1101,<EOF>",162))
    def test_number_literal_after_fix_but_fail2(self):
        self.assertTrue(TestLexer.test(
        """
        0x123_456 ## okay ##
        0x_123_456 ## fail ##
        ""","0x123456,0,x_123_456,<EOF>",163))
    def test_number_literal_after_fix_but_fail3(self):
        self.assertTrue(TestLexer.test(
        """
        0x123_456 ## okay ##
        0x123____456 ## fail ##
        ""","0x123456,0x123,____456,<EOF>",164))
    def test_unclosed_string_with_comment(self): # ?????
        self.assertTrue(TestLexer.test(
        """ "Happy ##new## year ""","Unclosed String: Happy ##new## year ",165))
    def test_unclosed_string_with_2_strings(self):
        self.assertTrue(TestLexer.test(
        """ "Happy" "New Year ""","Happy,Unclosed String: New Year ",166))
    def test_unclosed_string_with_2_strings_but_comment_first(self):
        self.assertTrue(TestLexer.test(
        """ ##"Happy"## "New Year ""","Unclosed String: New Year ",167))
    def test_block_comment_with_3_char(self):
        self.assertTrue(TestLexer.test( # ???
        """ ### Hello ### Class ""","Error Token #",168))
    def test_string_with_other(self):
        self.assertTrue(TestLexer.test(
        """ "abc + 12 * 13 % ~ !" ""","abc + 12 * 13 % ~ !,<EOF>",169))
    def test_string_with_other2(self):
        self.assertTrue(TestLexer.test(
        """ 123 * 456 && "123 * 456 &&"  ""","123,*,456,&&,123 * 456 &&,<EOF>",170))
    def test_double_quote_inside_string(self):
        self.assertTrue(TestLexer.test(
        """ "Normal string" "with '"double quote'" here" ""","""Normal string,with '"double quote'" here,<EOF>""",171))
    def test_double_quote_with_escape(self):
        self.assertTrue(TestLexer.test(
        """ "Normal string" "with '"double quote'" here //t //r !!!" ""","""Normal string,with '"double quote'" here //t //r !!!,<EOF>""",172))
    def test_multi_double_quote(self):
        self.assertTrue(TestLexer.test(
        """ "'"a'" '"b'" '"(1+1) = 3'"" ""","""'"a'" '"b'" '"(1+1) = 3'",<EOF>""",173))
    def test_multi_double_quote2(self):
        self.assertTrue(TestLexer.test(
        """ "'"abc'" def '"tuv'" xyz" ""","""'"abc'" def '"tuv'" xyz,<EOF>""",174))
    def test_escape_char(self):
        self.assertTrue(TestLexer.test(
        """ " \\b \\f \\n \\r \\t \\' \\\ " """,""" \\b \\f \\n \\r \\t \\' \\\ ,<EOF>""",175))
    def test_block_comment_but_fail(self):
        self.assertTrue(TestLexer.test(
        """ ## comment here ##
            ## not here """ ,"""Error Token #""",176))
    def test_random_mixing11(self):
        self.assertTrue(TestLexer.test(
        """
        {
            var r, s: Int;
            r = 2.0;
            var a, b: Array[Int, 5];
            s = r * r * Self.myPI;
            a[0] = s;
        }
        """ ,"""{,var,r,,,s,:,Int,;,r,=,2.0,;,var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>""",177))
    def test_random_mixing13(self):
        self.assertTrue(TestLexer.test(
        """
        element_expression -> expression index_operators
        index_operators -> [ expression ]
                         | [ expression ] index_operators
        """ ,"""element_expression,-,>,expression,index_operators,index_operators,-,>,[,expression,],Error Token |""",178))
    def test_random_mixing14(self):
        self.assertTrue(TestLexer.test(
        """
        For example, var a: Array[Int, 5]; indicates a five-element array: a[1], a[2], a[3], a[4], a[5].

        """ ,"""For,example,,,var,a,:,Array,[,Int,,,5,],;,indicates,a,five,-,element,array,:,a,[,1,],,,a,[,2,],,,a,[,3,],,,a,[,4,],,,a,[,5,],.,<EOF>""",179))
    def test_random_mixing15(self):
        self.assertTrue(TestLexer.test(
        """
        <expression>.<identifier <identifier>::<identifier>

        """ ,"""<,expression,>,.,<,identifier,<,identifier,>,::,<,identifier,>,<EOF>""",180))
    def test_random_mixing16(self):
        self.assertTrue(TestLexer.test(
        """ "Hello ##My## Friend" ""","Hello ##My## Friend,<EOF>",181))
    def test_random_mixing17(self):
        self.assertTrue(TestLexer.test(
        """ "Hello Friend## " ## ""","Hello Friend## ,Error Token #",182))
    def test_random_mixing18(self):
        self.assertTrue(TestLexer.test(
        """
        Foreach (<scalar variable> In <expr1> .. <expr2> [By <expr3>]?) <block statement>
        ""","Foreach,(,<,scalar,variable,>,In,<,expr1,>,..,<,expr2,>,[,By,<,expr3,>,],Error Token ?",183))
    def test_random_mixing19(self):
        self.assertTrue(TestLexer.test(
        """
        Array (
            Array("a", "b", "c"),
            Array("-", "*", "+"),
            Array("ufo", "space", "god")
            Array("dont", "do", "that")
        )
        ""","Array,(,Array,(,a,,,b,,,c,),,,Array,(,-,,,*,,,+,),,,Array,(,ufo,,,space,,,god,),Array,(,dont,,,do,,,that,),),<EOF>",184))
    def test_random_mixing20(self):
        self.assertTrue(TestLexer.test(
        """
        Array (
            Array(19, 27),
            Array(22, 12),
            Array(15, 42)
            Array(45, 57)
        )
        Array (
            Array("a", "b", "c"),
            Array("gg", "ez", "wp")
        )
        ""","Array,(,Array,(,19,,,27,),,,Array,(,22,,,12,),,,Array,(,15,,,42,),Array,(,45,,,57,),),Array,(,Array,(,a,,,b,,,c,),,,Array,(,gg,,,ez,,,wp,),),<EOF>",185))
    def test_random_mixing21(self):
        self.assertTrue(TestLexer.test(
        """
        001 0001 00001
        ""","00,1,00,01,00,00,1,<EOF>",186))
    def test_random_mixing22(self):
        self.assertTrue(TestLexer.test(
        """
        Class Shape {
            Val a, b: Int = (1 + 12), 3 * 5;
        }
        ""","Class,Shape,{,Val,a,,,b,:,Int,=,(,1,+,12,),,,3,*,5,;,},<EOF>",187))
    def test_random_mixing23(self):
        self.assertTrue(TestLexer.test(
        """
        In D96 programming language, there is only one type of comment: block comment. A block
        comment starts with ## and ignores all characters (except EOF) until it reaches the nearest
        ##. All characters in a block comment will be ignored.
        For example:
        ## This is a
        multi-line
        comment.
        ##
        ""","In,D96,programming,language,,,there,is,only,one,type,of,comment,:,block,comment,.,A,block,comment,starts,with,.,All,characters,in,a,block,comment,will,be,ignored,.,For,example,:,<EOF>",188))
    def test_random_mixing24(self):
        self.assertTrue(TestLexer.test(
        """
        123.e6 197.25 12e 13e12 12.3e6_9 e12.3 45
        ""","123.e6,197.25,12,e,13e12,12.3e6,_9,e12,.,3,45,<EOF>",189))
    def test_random_mixing25(self):
        self.assertTrue(TestLexer.test(
        """
        "string" "135.5e17" "/**/" "^^" "##" "##"
        ""","string,135.5e17,/**/,^^,##,##,<EOF>",190))
    def test_random_mixing26(self):
        self.assertTrue(TestLexer.test(
        """
        Foreach (i In 0 . . 12 By 3)
        ""","Foreach,(,i,In,0,.,.,12,By,3,),<EOF>",191))
    def test_random_mixing27(self):
        self.assertTrue(TestLexer.test(
        """
        0b1_000789abc
        0_1
        00_1
        ""","0b1000,789,abc,0,_1,00,_1,<EOF>",192))
    def test_random_mixing28(self):
        self.assertTrue(TestLexer.test(
        """
        "with some \\t \\z"
        ""","Illegal Escape In String: with some \\t \\z",193))
    def test_random_mixing29(self):
        self.assertTrue(TestLexer.test(
        """
        "my test \t case"
        ""","Unclosed String: my test ",194))
    def test_random_mixing30(self):
        self.assertTrue(TestLexer.test(
        """
        Class Test {
            Var myVar1: Boolean = !(2 > 3);
            Var myVar2: Boolean = (2 == 3) && (2 == 2);
        }
        ""","Class,Test,{,Var,myVar1,:,Boolean,=,!,(,2,>,3,),;,Var,myVar2,:,Boolean,=,(,2,==,3,),&&,(,2,==,2,),;,},<EOF>",195))
    def test_random_mixing31(self):
        self.assertTrue(TestLexer.test(
        """
        "string '"strong'" strength '"struck'""
        ""","""string '"strong'" strength '"struck'",<EOF>""",196))
    def test_random_mixing32(self):
        self.assertTrue(TestLexer.test(
        """
        0.156_ 352_13.4e10 56e12 725..33 257.6 55. 2
        ""","0.156,_,35213.4e10,56e12,725.,.,33,257.6,55.,2,<EOF>",197))
    def test_random_mixing33(self):
        self.assertTrue(TestLexer.test(
        """
        ### xyz ### #### kmn #### # abc #
        ""","Error Token #",198))
    def test_random_mixing34(self):
        self.assertTrue(TestLexer.test(
        """
        (0 _ 0) :))))) :() /./ /./ @ @
        ""","(,0,_,0,),:,),),),),),:,(,),/,.,/,/,.,/,Error Token @",199))
    def test_random_mixing35(self):
        self.assertTrue(TestLexer.test(
        """
        HAPPY NEW YEARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
        ""","HAPPY,NEW,YEARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR,<EOF>",200))