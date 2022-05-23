// ID: 1915350
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: classdecl+ EOF;
classdecl: CLASS ID inheritance_from? LCB  inside_decls RCB;
inheritance_from: COLON ID;

// // additional rules for the inside of the class
// inside_decls_with_main: manydecl_wm*;
// manydecl_wm: main_decl | vardecl | funcdecl;
// main_decl: 'main' LP RP block_stmt;

inside_decls: manydecl*;
manydecl: vardecl | funcdecl;
// funcdecls: funcdecl funcdecls | funcdecl;
funcdecl:  funcdecl1 | funcdecl2;
funcdecl1: CONSTRUCTOR LP listparam_with_type? RP block_stmt | DESTRUCTOR LP RP block_stmt;
funcdecl2: (ID | DOLLAR_ID) LP listparam_with_type? RP block_stmt;

// old
// listparam_with_type: (listparam COLON typ) (SEMI listparam COLON typ)*;
// listparam: ID (COMMA ID)*;

listparam_with_type: (listparam) (SEMI listparam)*;
listparam: ID (COMMA ID)* COLON typ;

// vardecls: vardecl vardecls | vardecl;
vardecl: (VAR | VAL) listvar (ASSIGN init_list)? SEMI; // test
// init_list: INTEGER_LITERAL (COMMA INTEGER_LITERAL)*; // test
init_list: (exp | array_decl) (COMMA (exp | array_decl))*; // real

// vardecl: ((VAR | VAL) listvar COLON typ SEMI) | ((VAR | VAL) vardecl_ele SEMI);

// real
// vardecl: (VAR | VAL) (listvar | vardecl_ele) SEMI;
// vardecl_ele: onevar COMMA vardecl_ele COMMA (exp | array_decl) | onevar COLON typ ASSIGN (exp | array_decl);

array_decl: ARRAY LP exps_list? RP;

onevar: ID | DOLLAR_ID;
listvar: onevar (COMMA onevar)* COLON typ;

// statement
stmt
	: vardecl_stmt
	| assign_stmt
	| if_stmt 
	| for_stmt
	| break_stmt
	| continue_stmt
	| ret_stmt
	| member_access_stmt
	| block_stmt
	;

// var decl no dollar stmt

vardecl_stmt: (VAR | VAL) listvar_no_dollar (ASSIGN init_list)? SEMI; // test

// vardecl_no_dollar: ((VAR | VAL) listvar_no_dollar COLON typ SEMI) | ((VAR | VAL) vardecl_no_dollar_ele SEMI);
// vardecl_no_dollar_ele: ID COMMA vardecl_no_dollar_ele COMMA (exp | array_decl) | ID COLON typ ASSIGN (exp | array_decl);
listvar_no_dollar: ID (COMMA ID)* COLON typ;

// member access (instance/static method invocation) // only for static methods
member_access_stmt: (SELF | exp) DOT (ID | DOLLAR_ID) LP exps_list? RP SEMI | ID SCOPE_OP (ID | DOLLAR_ID) LP exps_list? RP SEMI;

assign_stmt: exp ASSIGN exp SEMI;

// if smst chua fix
if_stmt: IF LP exp RP block_stmt else_part? | IF LP exp RP block_stmt (ELSE block_stmt);
else_part: (ELSEIF LP exp RP block_stmt) else_part | (ELSEIF LP exp RP block_stmt) (ELSE block_stmt)?;
// else_part: (ELSEIF LP exp RP block_stmt)* (ELSE block_stmt)?;

for_stmt: FOREACH LP ID IN exp DOTDOT exp (BY exp)? RP block_stmt;


break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

ret_stmt: RETURN SEMI | RETURN exp SEMI;


// Block stmt
block_stmt: LCB stmts_list RCB; // luon chua { }, co the khong co lenh
stmts_list: stmt*;



/*exp
	: operands
	| <assoc=right> NEW ID LP exps_list? RP
	| ID SCOPE_OP DOLLAR_ID  | ID SCOPE_OP DOLLAR_ID LP exps_list? RP // dollar for static methods
	| SELF DOT ID // o dau ?
	| exp DOT ID | exp DOT ID LP exps_list? RP
	| exp index_operators
	| <assoc=right> (SUB | NOT) exp
	| exp ( MUL | DIV | MOD ) exp
	| exp ( ADD | SUB ) exp
	| exp ( AND | OR ) exp
	| exp ( EQUAL_TO | NOT_EQUAL | LT | GT | LTE | GTE ) exp
	| exp ( STR_CONCAT | STR_COMPARE ) exp
	;

operands
	: literal
	| array_decl
	| (ID | DOLLAR_ID)
	| LP exp RP
	;
*/


exp: stringExp | stringExp (STR_CONCAT | STR_COMPARE) stringExp;

stringExp: logicExp | logicExp (EQUAL_TO | NOT_EQUAL | LT | GT | LTE | GTE) logicExp;

logicExp: logicExp (AND | OR) addExp | addExp;

addExp: addExp (ADD | SUB) mulExp| mulExp;

mulExp: mulExp ( MUL | DIV | MOD ) unaryLogicExp | unaryLogicExp;

unaryLogicExp: NOT unaryLogicExp | unarySignExp;

unarySignExp: SUB unarySignExp | indexExp;

indexExp: indexExp index_operators | callExp1;

callExp1: callExp1 DOT (ID | DOLLAR_ID) | callExp1 DOT (ID | DOLLAR_ID) LP exps_list? RP | selfExp;

selfExp: SELF DOT ID | SELF DOT ID LP exps_list? RP | callExp2;

callExp2: ID SCOPE_OP (ID | DOLLAR_ID)  | ID SCOPE_OP (ID | DOLLAR_ID) LP exps_list? RP | newExp; // dollar for static methods

newExp: NEW ID LP exps_list? RP | lastExpr;


lastExpr: literal | array_decl | (ID | DOLLAR_ID) | LP exp RP;


// index operators
// element_expression: exp index_operators;
index_operators: LSB exp RSB index_operators | LSB exp RSB;

literal: INTEGER_LITERAL | FLOAT_LITERAL | BOOLEAN_LITERAL | STRING_LITERAL | NULL;
exps_list: exp (COMMA exp)*;




// type
typ: arr_type | INT | FLOAT | BOOLEAN | STRING | ID;
// array type
arr_type: ARRAY LSB typ COMMA arr_size RSB;
arr_size: INTEGER_LITERAL;







/*================ Literals ===================*/
// boolean
BOOLEAN_LITERAL: TRUE | FALSE;

// integer
fragment OCTAL_INTEGER: '00' | '0'[1-7] ('_'? [0-7])*;
fragment HEXA_INTEGER: '0' [xX] '0'| '0'[xX][1-9A-F] ('_'? [0-9A-F])*;
fragment BIN_INTEGER: '0' [bB] '0' | '0'[bB][1] ('_'? [0-1])*;
fragment NORMAL_INTEGER: '0' | [1-9] ('_'? [0-9])*;
INTEGER_LITERAL: (OCTAL_INTEGER | HEXA_INTEGER | BIN_INTEGER | NORMAL_INTEGER) {self.text = self.text.replace('_', '')};


// float
FLOAT_LITERAL: (FLOAT_PART1 FLOAT_PART2 FLOAT_PART3? | FLOAT_PART1 FLOAT_PART3 | FLOAT_PART2 FLOAT_PART3) {self.text = self.text.replace('_', '')};
fragment FLOAT_PART1: '0' | [1-9] ('_'? [0-9])*;
fragment FLOAT_PART2: DOT (DIGIT+)?;
fragment FLOAT_PART3: [eE][+-]?DIGIT+;

fragment DIGIT: [0-9];

// string
STRING_LITERAL: '"' STR_REG* (['] '"' STR_REG* ['] '"' STR_REG*)* STR_REG* '"'
{
		myStr = str(self.text)
		self.text = myStr[1:len(myStr)-1]
};
fragment STR_REG: ESC_SEQ | ~[\b\f\n\r\t"'\\];
fragment ESC_SEQ: '\\' [bfrnt'\\];
fragment ESC_ILLEGAL: '\\' ~[bfrnt'\\] | ~'\\' ;



/*================ Operator ===================*/
STR_CONCAT: '+.';
STR_COMPARE: '==.';
SCOPE_OP: '::';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%'; // Number Remainder ?
NOT_EQUAL: '!=';
EQUAL_TO: '==';
NOT: '!';
AND: '&&';
OR: '||';
LTE: '<=';
GTE: '>=';
ASSIGN: '=';
LT: '<';
GT: '>';
// and operator New ????


/*================ Seperators ===================*/
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';

SEMI: ';';
COLON: ':';
COMMA: ',';
DOTDOT: '..';
DOT: '.';

/*================ Key word ===================*/
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
SELF: 'Self';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';

// ID
ID: [_a-zA-Z][_a-zA-Z0-9]*;
DOLLAR_ID: '$' [_a-zA-Z0-9]+; // khac voi ID ?



// skip comments inside ## ##
BLOCK_COMMENT: '##' .*? '##' -> skip;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


UNCLOSE_STRING: '"' STR_REG* ([\b\f\n\r\t"'\\] | EOF) {
	myStr = str(self.text)
	lastChar = ['\b', '\f', '\n', '\r', '\t', '"', "'", '\\']
	if myStr[-1] in lastChar:
		raise UncloseString(myStr[1:-1])
	else:
		raise UncloseString(myStr[1:])
};
ILLEGAL_ESCAPE: '"' STR_REG* ESC_ILLEGAL {
		myStr = str(self.text)
		raise IllegalEscape(myStr[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};