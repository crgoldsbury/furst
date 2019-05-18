
from include.Lexer import *



class FurstInterpreter:
    def __init__(self,text):
        self.text=text;#input string
        self.pos=0; #position in characters

        self.current_token=None;#current token
        self.current_char=self.text[self.pos]

    done = False;

    def advance(self): #go forward one position
        self.pos+=1;
        if self.pos==len(self.text):
            self.current_char=None;
        self.current_char=self.text[self.pos]

    def peek(self,index): #like advance but returns the next char
        peekpos=len(self.text)
        peekpos+=index;
        if self.pos==len(self.text):
            return None;
        return self.text[peekpos]
    def peekback(self,index):
        peekpos = len(self.text)
        peekpos -= index;
        if self.pos == len(self.text):
            return None;
        return self.text[peekpos]
    

    advance()

    def start(self):
        ops = Operators();
        while self.done==False:
            if self.current_char=="!":
                if self.peek(1)=="=":
                    self.current_token=ops.DOSENTEQUAL
            if self.current_char=="=":
                if self.peek(1)=="=":
                    self.current_token=ops.EQUALS;
                if self.peek(1)!="=":
                    self.current_token=ops.EQUAL;
            if self.current_char=="+":
                self.current_token=ops.ADD;
            if self.current_char=="/":
                self.current_token=ops.DIVIDE;
            if self.current_char==";":
                self.current_token=ops.SEMICOLON;
            if self.current_char=="%":
                self.current_token=ops.MOD;
            if self.current_char=="-":
                self.current_token=ops.SUB;
            if self.current_char=="*":
                self.current_token=ops.MULITPLY;

