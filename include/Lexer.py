

class Operators:
     EQUAL,DOSENTEQUAL,EQUALS,ADD,SUB,DIVIDE,MULITPLY,MOD,SEMICOLON="=","!=","==","+","-","/","*","%",";";
class types:
     j_function,j_var,j_string,j_char,j_int,j_float="FUNCTION","VAR","STRING","CHAR","INT","FLOAT";
class Token:
    jtype=None;
    value=None;
    def __init__(self,jtype,value):
        self.jtype=jtype
        self.value=value
    tok="Token("+jtype+","+value+")";
    def get(self):
        return self.tok;
