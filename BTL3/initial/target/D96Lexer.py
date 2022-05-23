# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0253\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\5\2\u009c\n\2\3\3\3\3\3\3\3\3\3\3\5\3\u00a3")
        buf.write("\n\3\3\3\7\3\u00a6\n\3\f\3\16\3\u00a9\13\3\5\3\u00ab\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00b4\n\4\3\4\7\4\u00b7")
        buf.write("\n\4\f\4\16\4\u00ba\13\4\5\4\u00bc\n\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5\u00c5\n\5\3\5\7\5\u00c8\n\5\f\5\16\5")
        buf.write("\u00cb\13\5\5\5\u00cd\n\5\3\6\3\6\3\6\5\6\u00d2\n\6\3")
        buf.write("\6\7\6\u00d5\n\6\f\6\16\6\u00d8\13\6\5\6\u00da\n\6\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u00e0\n\7\3\7\3\7\3\b\3\b\3\b\5\b\u00e7")
        buf.write("\n\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00ef\n\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\5\t\u00f6\n\t\3\t\7\t\u00f9\n\t\f\t\16\t\u00fc")
        buf.write("\13\t\5\t\u00fe\n\t\3\n\3\n\6\n\u0102\n\n\r\n\16\n\u0103")
        buf.write("\5\n\u0106\n\n\3\13\3\13\5\13\u010a\n\13\3\13\6\13\u010d")
        buf.write("\n\13\r\13\16\13\u010e\3\f\3\f\3\r\3\r\7\r\u0115\n\r\f")
        buf.write("\r\16\r\u0118\13\r\3\r\3\r\3\r\7\r\u011d\n\r\f\r\16\r")
        buf.write("\u0120\13\r\3\r\3\r\3\r\7\r\u0125\n\r\f\r\16\r\u0128\13")
        buf.write("\r\7\r\u012a\n\r\f\r\16\r\u012d\13\r\3\r\7\r\u0130\n\r")
        buf.write("\f\r\16\r\u0133\13\r\3\r\3\r\3\r\3\16\3\16\5\16\u013a")
        buf.write("\n\16\3\17\3\17\3\17\3\20\3\20\3\20\5\20\u0142\n\20\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\38\38\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:")
        buf.write("\3:\3:\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3=\3")
        buf.write("=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3@\3")
        buf.write("A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3C\3")
        buf.write("C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3D\3D\3D\3D\3E\3E\3E\3F\3")
        buf.write("F\7F\u021b\nF\fF\16F\u021e\13F\3G\3G\6G\u0222\nG\rG\16")
        buf.write("G\u0223\3H\3H\3H\3H\7H\u022a\nH\fH\16H\u022d\13H\3H\3")
        buf.write("H\3H\3H\3H\3I\6I\u0235\nI\rI\16I\u0236\3I\3I\3J\3J\7J")
        buf.write("\u023d\nJ\fJ\16J\u0240\13J\3J\5J\u0243\nJ\3J\3J\3K\3K")
        buf.write("\7K\u0249\nK\fK\16K\u024c\13K\3K\3K\3K\3L\3L\3L\3\u022b")
        buf.write("\2M\3\3\5\2\7\2\t\2\13\2\r\4\17\5\21\2\23\2\25\2\27\2")
        buf.write("\31\6\33\2\35\2\37\2!\7#\b%\t\'\n)\13+\f-\r/\16\61\17")
        buf.write("\63\20\65\21\67\229\23;\24=\25?\26A\27C\30E\31G\32I\33")
        buf.write("K\34M\35O\36Q\37S U!W\"Y#[$]%_&a\'c(e)g*i+k,m-o.q/s\60")
        buf.write("u\61w\62y\63{\64}\65\177\66\u0081\67\u00838\u00859\u0087")
        buf.write(":\u0089;\u008b<\u008d=\u008f>\u0091?\u0093@\u0095A\u0097")
        buf.write("B\3\2\26\3\2\639\3\2\629\4\2ZZzz\4\2\63;CH\4\2\62;CH\4")
        buf.write("\2DDdd\3\2\63\63\3\2\62\63\3\2\63;\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\3\2))\7\2\n\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2^")
        buf.write("^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\7\3\n\f")
        buf.write("\16\17$$))^^\2\u026e\2\3\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u009b")
        buf.write("\3\2\2\2\5\u00aa\3\2\2\2\7\u00bb\3\2\2\2\t\u00cc\3\2\2")
        buf.write("\2\13\u00d9\3\2\2\2\r\u00df\3\2\2\2\17\u00ee\3\2\2\2\21")
        buf.write("\u00fd\3\2\2\2\23\u00ff\3\2\2\2\25\u0107\3\2\2\2\27\u0110")
        buf.write("\3\2\2\2\31\u0112\3\2\2\2\33\u0139\3\2\2\2\35\u013b\3")
        buf.write("\2\2\2\37\u0141\3\2\2\2!\u0143\3\2\2\2#\u0146\3\2\2\2")
        buf.write("%\u014a\3\2\2\2\'\u014d\3\2\2\2)\u014f\3\2\2\2+\u0151")
        buf.write("\3\2\2\2-\u0153\3\2\2\2/\u0155\3\2\2\2\61\u0157\3\2\2")
        buf.write("\2\63\u015a\3\2\2\2\65\u015d\3\2\2\2\67\u015f\3\2\2\2")
        buf.write("9\u0162\3\2\2\2;\u0165\3\2\2\2=\u0168\3\2\2\2?\u016b\3")
        buf.write("\2\2\2A\u016d\3\2\2\2C\u016f\3\2\2\2E\u0171\3\2\2\2G\u0173")
        buf.write("\3\2\2\2I\u0175\3\2\2\2K\u0177\3\2\2\2M\u0179\3\2\2\2")
        buf.write("O\u017b\3\2\2\2Q\u017d\3\2\2\2S\u017f\3\2\2\2U\u0181\3")
        buf.write("\2\2\2W\u0183\3\2\2\2Y\u0186\3\2\2\2[\u0188\3\2\2\2]\u018e")
        buf.write("\3\2\2\2_\u0197\3\2\2\2a\u019a\3\2\2\2c\u01a1\3\2\2\2")
        buf.write("e\u01a6\3\2\2\2g\u01ae\3\2\2\2i\u01b3\3\2\2\2k\u01b9\3")
        buf.write("\2\2\2m\u01bf\3\2\2\2o\u01c2\3\2\2\2q\u01c6\3\2\2\2s\u01cc")
        buf.write("\3\2\2\2u\u01d4\3\2\2\2w\u01db\3\2\2\2y\u01e2\3\2\2\2")
        buf.write("{\u01e7\3\2\2\2}\u01ed\3\2\2\2\177\u01f1\3\2\2\2\u0081")
        buf.write("\u01f5\3\2\2\2\u0083\u01fa\3\2\2\2\u0085\u0206\3\2\2\2")
        buf.write("\u0087\u0211\3\2\2\2\u0089\u0215\3\2\2\2\u008b\u0218\3")
        buf.write("\2\2\2\u008d\u021f\3\2\2\2\u008f\u0225\3\2\2\2\u0091\u0234")
        buf.write("\3\2\2\2\u0093\u023a\3\2\2\2\u0095\u0246\3\2\2\2\u0097")
        buf.write("\u0250\3\2\2\2\u0099\u009c\5g\64\2\u009a\u009c\5i\65\2")
        buf.write("\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c\4\3\2\2")
        buf.write("\2\u009d\u009e\7\62\2\2\u009e\u00ab\7\62\2\2\u009f\u00a0")
        buf.write("\7\62\2\2\u00a0\u00a7\t\2\2\2\u00a1\u00a3\7a\2\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00a6\t\3\2\2\u00a5\u00a2\3\2\2\2\u00a6\u00a9\3")
        buf.write("\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00ab")
        buf.write("\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u009d\3\2\2\2\u00aa")
        buf.write("\u009f\3\2\2\2\u00ab\6\3\2\2\2\u00ac\u00ad\7\62\2\2\u00ad")
        buf.write("\u00ae\t\4\2\2\u00ae\u00bc\7\62\2\2\u00af\u00b0\7\62\2")
        buf.write("\2\u00b0\u00b1\t\4\2\2\u00b1\u00b8\t\5\2\2\u00b2\u00b4")
        buf.write("\7a\2\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b5\3\2\2\2\u00b5\u00b7\t\6\2\2\u00b6\u00b3\3\2\2\2")
        buf.write("\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00ac")
        buf.write("\3\2\2\2\u00bb\u00af\3\2\2\2\u00bc\b\3\2\2\2\u00bd\u00be")
        buf.write("\7\62\2\2\u00be\u00bf\t\7\2\2\u00bf\u00cd\7\62\2\2\u00c0")
        buf.write("\u00c1\7\62\2\2\u00c1\u00c2\t\7\2\2\u00c2\u00c9\t\b\2")
        buf.write("\2\u00c3\u00c5\7a\2\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\t\t\2\2\u00c7")
        buf.write("\u00c4\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3")
        buf.write("\2\2\2\u00cc\u00bd\3\2\2\2\u00cc\u00c0\3\2\2\2\u00cd\n")
        buf.write("\3\2\2\2\u00ce\u00da\7\62\2\2\u00cf\u00d6\t\n\2\2\u00d0")
        buf.write("\u00d2\7a\2\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d3\3\2\2\2\u00d3\u00d5\t\13\2\2\u00d4\u00d1")
        buf.write("\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d7\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2")
        buf.write("\u00d9\u00ce\3\2\2\2\u00d9\u00cf\3\2\2\2\u00da\f\3\2\2")
        buf.write("\2\u00db\u00e0\5\5\3\2\u00dc\u00e0\5\7\4\2\u00dd\u00e0")
        buf.write("\5\t\5\2\u00de\u00e0\5\13\6\2\u00df\u00db\3\2\2\2\u00df")
        buf.write("\u00dc\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\u00e2\b\7\2\2\u00e2\16\3\2")
        buf.write("\2\2\u00e3\u00e4\5\21\t\2\u00e4\u00e6\5\23\n\2\u00e5\u00e7")
        buf.write("\5\25\13\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00ef\3\2\2\2\u00e8\u00e9\5\21\t\2\u00e9\u00ea\5\25\13")
        buf.write("\2\u00ea\u00ef\3\2\2\2\u00eb\u00ec\5\23\n\2\u00ec\u00ed")
        buf.write("\5\25\13\2\u00ed\u00ef\3\2\2\2\u00ee\u00e3\3\2\2\2\u00ee")
        buf.write("\u00e8\3\2\2\2\u00ee\u00eb\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f1\b\b\3\2\u00f1\20\3\2\2\2\u00f2\u00fe\7\62")
        buf.write("\2\2\u00f3\u00fa\t\n\2\2\u00f4\u00f6\7a\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7")
        buf.write("\u00f9\t\13\2\2\u00f8\u00f5\3\2\2\2\u00f9\u00fc\3\2\2")
        buf.write("\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fe")
        buf.write("\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00f2\3\2\2\2\u00fd")
        buf.write("\u00f3\3\2\2\2\u00fe\22\3\2\2\2\u00ff\u0105\5Y-\2\u0100")
        buf.write("\u0102\5\27\f\2\u0101\u0100\3\2\2\2\u0102\u0103\3\2\2")
        buf.write("\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0106")
        buf.write("\3\2\2\2\u0105\u0101\3\2\2\2\u0105\u0106\3\2\2\2\u0106")
        buf.write("\24\3\2\2\2\u0107\u0109\t\f\2\2\u0108\u010a\t\r\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010c\3\2\2\2")
        buf.write("\u010b\u010d\5\27\f\2\u010c\u010b\3\2\2\2\u010d\u010e")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\26\3\2\2\2\u0110\u0111\t\13\2\2\u0111\30\3\2\2\2\u0112")
        buf.write("\u0116\7$\2\2\u0113\u0115\5\33\16\2\u0114\u0113\3\2\2")
        buf.write("\2\u0115\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117")
        buf.write("\3\2\2\2\u0117\u012b\3\2\2\2\u0118\u0116\3\2\2\2\u0119")
        buf.write("\u011a\t\16\2\2\u011a\u011e\7$\2\2\u011b\u011d\5\33\16")
        buf.write("\2\u011c\u011b\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0121\u0122\t\16\2\2\u0122\u0126\7$\2\2")
        buf.write("\u0123\u0125\5\33\16\2\u0124\u0123\3\2\2\2\u0125\u0128")
        buf.write("\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u0119\3\2\2\2")
        buf.write("\u012a\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3")
        buf.write("\2\2\2\u012c\u0131\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u0130")
        buf.write("\5\33\16\2\u012f\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131")
        buf.write("\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134\3\2\2\2")
        buf.write("\u0133\u0131\3\2\2\2\u0134\u0135\7$\2\2\u0135\u0136\b")
        buf.write("\r\4\2\u0136\32\3\2\2\2\u0137\u013a\5\35\17\2\u0138\u013a")
        buf.write("\n\17\2\2\u0139\u0137\3\2\2\2\u0139\u0138\3\2\2\2\u013a")
        buf.write("\34\3\2\2\2\u013b\u013c\7^\2\2\u013c\u013d\t\20\2\2\u013d")
        buf.write("\36\3\2\2\2\u013e\u013f\7^\2\2\u013f\u0142\n\20\2\2\u0140")
        buf.write("\u0142\n\21\2\2\u0141\u013e\3\2\2\2\u0141\u0140\3\2\2")
        buf.write("\2\u0142 \3\2\2\2\u0143\u0144\7-\2\2\u0144\u0145\7\60")
        buf.write("\2\2\u0145\"\3\2\2\2\u0146\u0147\7?\2\2\u0147\u0148\7")
        buf.write("?\2\2\u0148\u0149\7\60\2\2\u0149$\3\2\2\2\u014a\u014b")
        buf.write("\7<\2\2\u014b\u014c\7<\2\2\u014c&\3\2\2\2\u014d\u014e")
        buf.write("\7-\2\2\u014e(\3\2\2\2\u014f\u0150\7/\2\2\u0150*\3\2\2")
        buf.write("\2\u0151\u0152\7,\2\2\u0152,\3\2\2\2\u0153\u0154\7\61")
        buf.write("\2\2\u0154.\3\2\2\2\u0155\u0156\7\'\2\2\u0156\60\3\2\2")
        buf.write("\2\u0157\u0158\7#\2\2\u0158\u0159\7?\2\2\u0159\62\3\2")
        buf.write("\2\2\u015a\u015b\7?\2\2\u015b\u015c\7?\2\2\u015c\64\3")
        buf.write("\2\2\2\u015d\u015e\7#\2\2\u015e\66\3\2\2\2\u015f\u0160")
        buf.write("\7(\2\2\u0160\u0161\7(\2\2\u01618\3\2\2\2\u0162\u0163")
        buf.write("\7~\2\2\u0163\u0164\7~\2\2\u0164:\3\2\2\2\u0165\u0166")
        buf.write("\7>\2\2\u0166\u0167\7?\2\2\u0167<\3\2\2\2\u0168\u0169")
        buf.write("\7@\2\2\u0169\u016a\7?\2\2\u016a>\3\2\2\2\u016b\u016c")
        buf.write("\7?\2\2\u016c@\3\2\2\2\u016d\u016e\7>\2\2\u016eB\3\2\2")
        buf.write("\2\u016f\u0170\7@\2\2\u0170D\3\2\2\2\u0171\u0172\7*\2")
        buf.write("\2\u0172F\3\2\2\2\u0173\u0174\7+\2\2\u0174H\3\2\2\2\u0175")
        buf.write("\u0176\7]\2\2\u0176J\3\2\2\2\u0177\u0178\7_\2\2\u0178")
        buf.write("L\3\2\2\2\u0179\u017a\7}\2\2\u017aN\3\2\2\2\u017b\u017c")
        buf.write("\7\177\2\2\u017cP\3\2\2\2\u017d\u017e\7=\2\2\u017eR\3")
        buf.write("\2\2\2\u017f\u0180\7<\2\2\u0180T\3\2\2\2\u0181\u0182\7")
        buf.write(".\2\2\u0182V\3\2\2\2\u0183\u0184\7\60\2\2\u0184\u0185")
        buf.write("\7\60\2\2\u0185X\3\2\2\2\u0186\u0187\7\60\2\2\u0187Z\3")
        buf.write("\2\2\2\u0188\u0189\7D\2\2\u0189\u018a\7t\2\2\u018a\u018b")
        buf.write("\7g\2\2\u018b\u018c\7c\2\2\u018c\u018d\7m\2\2\u018d\\")
        buf.write("\3\2\2\2\u018e\u018f\7E\2\2\u018f\u0190\7q\2\2\u0190\u0191")
        buf.write("\7p\2\2\u0191\u0192\7v\2\2\u0192\u0193\7k\2\2\u0193\u0194")
        buf.write("\7p\2\2\u0194\u0195\7w\2\2\u0195\u0196\7g\2\2\u0196^\3")
        buf.write("\2\2\2\u0197\u0198\7K\2\2\u0198\u0199\7h\2\2\u0199`\3")
        buf.write("\2\2\2\u019a\u019b\7G\2\2\u019b\u019c\7n\2\2\u019c\u019d")
        buf.write("\7u\2\2\u019d\u019e\7g\2\2\u019e\u019f\7k\2\2\u019f\u01a0")
        buf.write("\7h\2\2\u01a0b\3\2\2\2\u01a1\u01a2\7G\2\2\u01a2\u01a3")
        buf.write("\7n\2\2\u01a3\u01a4\7u\2\2\u01a4\u01a5\7g\2\2\u01a5d\3")
        buf.write("\2\2\2\u01a6\u01a7\7H\2\2\u01a7\u01a8\7q\2\2\u01a8\u01a9")
        buf.write("\7t\2\2\u01a9\u01aa\7g\2\2\u01aa\u01ab\7c\2\2\u01ab\u01ac")
        buf.write("\7e\2\2\u01ac\u01ad\7j\2\2\u01adf\3\2\2\2\u01ae\u01af")
        buf.write("\7V\2\2\u01af\u01b0\7t\2\2\u01b0\u01b1\7w\2\2\u01b1\u01b2")
        buf.write("\7g\2\2\u01b2h\3\2\2\2\u01b3\u01b4\7H\2\2\u01b4\u01b5")
        buf.write("\7c\2\2\u01b5\u01b6\7n\2\2\u01b6\u01b7\7u\2\2\u01b7\u01b8")
        buf.write("\7g\2\2\u01b8j\3\2\2\2\u01b9\u01ba\7C\2\2\u01ba\u01bb")
        buf.write("\7t\2\2\u01bb\u01bc\7t\2\2\u01bc\u01bd\7c\2\2\u01bd\u01be")
        buf.write("\7{\2\2\u01bel\3\2\2\2\u01bf\u01c0\7K\2\2\u01c0\u01c1")
        buf.write("\7p\2\2\u01c1n\3\2\2\2\u01c2\u01c3\7K\2\2\u01c3\u01c4")
        buf.write("\7p\2\2\u01c4\u01c5\7v\2\2\u01c5p\3\2\2\2\u01c6\u01c7")
        buf.write("\7H\2\2\u01c7\u01c8\7n\2\2\u01c8\u01c9\7q\2\2\u01c9\u01ca")
        buf.write("\7c\2\2\u01ca\u01cb\7v\2\2\u01cbr\3\2\2\2\u01cc\u01cd")
        buf.write("\7D\2\2\u01cd\u01ce\7q\2\2\u01ce\u01cf\7q\2\2\u01cf\u01d0")
        buf.write("\7n\2\2\u01d0\u01d1\7g\2\2\u01d1\u01d2\7c\2\2\u01d2\u01d3")
        buf.write("\7p\2\2\u01d3t\3\2\2\2\u01d4\u01d5\7U\2\2\u01d5\u01d6")
        buf.write("\7v\2\2\u01d6\u01d7\7t\2\2\u01d7\u01d8\7k\2\2\u01d8\u01d9")
        buf.write("\7p\2\2\u01d9\u01da\7i\2\2\u01dav\3\2\2\2\u01db\u01dc")
        buf.write("\7T\2\2\u01dc\u01dd\7g\2\2\u01dd\u01de\7v\2\2\u01de\u01df")
        buf.write("\7w\2\2\u01df\u01e0\7t\2\2\u01e0\u01e1\7p\2\2\u01e1x\3")
        buf.write("\2\2\2\u01e2\u01e3\7P\2\2\u01e3\u01e4\7w\2\2\u01e4\u01e5")
        buf.write("\7n\2\2\u01e5\u01e6\7n\2\2\u01e6z\3\2\2\2\u01e7\u01e8")
        buf.write("\7E\2\2\u01e8\u01e9\7n\2\2\u01e9\u01ea\7c\2\2\u01ea\u01eb")
        buf.write("\7u\2\2\u01eb\u01ec\7u\2\2\u01ec|\3\2\2\2\u01ed\u01ee")
        buf.write("\7X\2\2\u01ee\u01ef\7c\2\2\u01ef\u01f0\7n\2\2\u01f0~\3")
        buf.write("\2\2\2\u01f1\u01f2\7X\2\2\u01f2\u01f3\7c\2\2\u01f3\u01f4")
        buf.write("\7t\2\2\u01f4\u0080\3\2\2\2\u01f5\u01f6\7U\2\2\u01f6\u01f7")
        buf.write("\7g\2\2\u01f7\u01f8\7n\2\2\u01f8\u01f9\7h\2\2\u01f9\u0082")
        buf.write("\3\2\2\2\u01fa\u01fb\7E\2\2\u01fb\u01fc\7q\2\2\u01fc\u01fd")
        buf.write("\7p\2\2\u01fd\u01fe\7u\2\2\u01fe\u01ff\7v\2\2\u01ff\u0200")
        buf.write("\7t\2\2\u0200\u0201\7w\2\2\u0201\u0202\7e\2\2\u0202\u0203")
        buf.write("\7v\2\2\u0203\u0204\7q\2\2\u0204\u0205\7t\2\2\u0205\u0084")
        buf.write("\3\2\2\2\u0206\u0207\7F\2\2\u0207\u0208\7g\2\2\u0208\u0209")
        buf.write("\7u\2\2\u0209\u020a\7v\2\2\u020a\u020b\7t\2\2\u020b\u020c")
        buf.write("\7w\2\2\u020c\u020d\7e\2\2\u020d\u020e\7v\2\2\u020e\u020f")
        buf.write("\7q\2\2\u020f\u0210\7t\2\2\u0210\u0086\3\2\2\2\u0211\u0212")
        buf.write("\7P\2\2\u0212\u0213\7g\2\2\u0213\u0214\7y\2\2\u0214\u0088")
        buf.write("\3\2\2\2\u0215\u0216\7D\2\2\u0216\u0217\7{\2\2\u0217\u008a")
        buf.write("\3\2\2\2\u0218\u021c\t\22\2\2\u0219\u021b\t\23\2\2\u021a")
        buf.write("\u0219\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2")
        buf.write("\u021c\u021d\3\2\2\2\u021d\u008c\3\2\2\2\u021e\u021c\3")
        buf.write("\2\2\2\u021f\u0221\7&\2\2\u0220\u0222\t\23\2\2\u0221\u0220")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0221\3\2\2\2\u0223")
        buf.write("\u0224\3\2\2\2\u0224\u008e\3\2\2\2\u0225\u0226\7%\2\2")
        buf.write("\u0226\u0227\7%\2\2\u0227\u022b\3\2\2\2\u0228\u022a\13")
        buf.write("\2\2\2\u0229\u0228\3\2\2\2\u022a\u022d\3\2\2\2\u022b\u022c")
        buf.write("\3\2\2\2\u022b\u0229\3\2\2\2\u022c\u022e\3\2\2\2\u022d")
        buf.write("\u022b\3\2\2\2\u022e\u022f\7%\2\2\u022f\u0230\7%\2\2\u0230")
        buf.write("\u0231\3\2\2\2\u0231\u0232\bH\5\2\u0232\u0090\3\2\2\2")
        buf.write("\u0233\u0235\t\24\2\2\u0234\u0233\3\2\2\2\u0235\u0236")
        buf.write("\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238\u0239\bI\5\2\u0239\u0092\3\2\2\2")
        buf.write("\u023a\u023e\7$\2\2\u023b\u023d\5\33\16\2\u023c\u023b")
        buf.write("\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023f\u0242\3\2\2\2\u0240\u023e\3\2\2\2")
        buf.write("\u0241\u0243\t\25\2\2\u0242\u0241\3\2\2\2\u0243\u0244")
        buf.write("\3\2\2\2\u0244\u0245\bJ\6\2\u0245\u0094\3\2\2\2\u0246")
        buf.write("\u024a\7$\2\2\u0247\u0249\5\33\16\2\u0248\u0247\3\2\2")
        buf.write("\2\u0249\u024c\3\2\2\2\u024a\u0248\3\2\2\2\u024a\u024b")
        buf.write("\3\2\2\2\u024b\u024d\3\2\2\2\u024c\u024a\3\2\2\2\u024d")
        buf.write("\u024e\5\37\20\2\u024e\u024f\bK\7\2\u024f\u0096\3\2\2")
        buf.write("\2\u0250\u0251\13\2\2\2\u0251\u0252\bL\b\2\u0252\u0098")
        buf.write("\3\2\2\2(\2\u009b\u00a2\u00a7\u00aa\u00b3\u00b8\u00bb")
        buf.write("\u00c4\u00c9\u00cc\u00d1\u00d6\u00d9\u00df\u00e6\u00ee")
        buf.write("\u00f5\u00fa\u00fd\u0103\u0105\u0109\u010e\u0116\u011e")
        buf.write("\u0126\u012b\u0131\u0139\u0141\u021c\u0223\u022b\u0236")
        buf.write("\u023e\u0242\u024a\t\3\7\2\3\b\3\3\r\4\b\2\2\3J\5\3K\6")
        buf.write("\3L\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEAN_LITERAL = 1
    INTEGER_LITERAL = 2
    FLOAT_LITERAL = 3
    STRING_LITERAL = 4
    STR_CONCAT = 5
    STR_COMPARE = 6
    SCOPE_OP = 7
    ADD = 8
    SUB = 9
    MUL = 10
    DIV = 11
    MOD = 12
    NOT_EQUAL = 13
    EQUAL_TO = 14
    NOT = 15
    AND = 16
    OR = 17
    LTE = 18
    GTE = 19
    ASSIGN = 20
    LT = 21
    GT = 22
    LP = 23
    RP = 24
    LSB = 25
    RSB = 26
    LCB = 27
    RCB = 28
    SEMI = 29
    COLON = 30
    COMMA = 31
    DOTDOT = 32
    DOT = 33
    BREAK = 34
    CONTINUE = 35
    IF = 36
    ELSEIF = 37
    ELSE = 38
    FOREACH = 39
    TRUE = 40
    FALSE = 41
    ARRAY = 42
    IN = 43
    INT = 44
    FLOAT = 45
    BOOLEAN = 46
    STRING = 47
    RETURN = 48
    NULL = 49
    CLASS = 50
    VAL = 51
    VAR = 52
    SELF = 53
    CONSTRUCTOR = 54
    DESTRUCTOR = 55
    NEW = 56
    BY = 57
    ID = 58
    DOLLAR_ID = 59
    BLOCK_COMMENT = 60
    WS = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+.'", "'==.'", "'::'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!='", "'=='", "'!'", "'&&'", "'||'", "'<='", "'>='", "'='", 
            "'<'", "'>'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", 
            "':'", "','", "'..'", "'.'", "'Break'", "'Continue'", "'If'", 
            "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
            "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", 
            "'Null'", "'Class'", "'Val'", "'Var'", "'Self'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN_LITERAL", "INTEGER_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
            "STR_CONCAT", "STR_COMPARE", "SCOPE_OP", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "NOT_EQUAL", "EQUAL_TO", "NOT", "AND", "OR", "LTE", 
            "GTE", "ASSIGN", "LT", "GT", "LP", "RP", "LSB", "RSB", "LCB", 
            "RCB", "SEMI", "COLON", "COMMA", "DOTDOT", "DOT", "BREAK", "CONTINUE", 
            "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
            "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
            "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "ID", "DOLLAR_ID", "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BOOLEAN_LITERAL", "OCTAL_INTEGER", "HEXA_INTEGER", "BIN_INTEGER", 
                  "NORMAL_INTEGER", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                  "FLOAT_PART1", "FLOAT_PART2", "FLOAT_PART3", "DIGIT", 
                  "STRING_LITERAL", "STR_REG", "ESC_SEQ", "ESC_ILLEGAL", 
                  "STR_CONCAT", "STR_COMPARE", "SCOPE_OP", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT_EQUAL", "EQUAL_TO", "NOT", "AND", 
                  "OR", "LTE", "GTE", "ASSIGN", "LT", "GT", "LP", "RP", 
                  "LSB", "RSB", "LCB", "RCB", "SEMI", "COLON", "COMMA", 
                  "DOTDOT", "DOT", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", 
                  "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", 
                  "VAL", "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "ID", "DOLLAR_ID", "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.INTEGER_LITERAL_action 
            actions[6] = self.FLOAT_LITERAL_action 
            actions[11] = self.STRING_LITERAL_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def FLOAT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		myStr = str(self.text)
            		self.text = myStr[1:len(myStr)-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	myStr = str(self.text)
            	lastChar = ['\b', '\f', '\n', '\r', '\t', '"', "'", '\\']
            	if myStr[-1] in lastChar:
            		raise UncloseString(myStr[1:-1])
            	else:
            		raise UncloseString(myStr[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		myStr = str(self.text)
            		raise IllegalEscape(myStr[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


