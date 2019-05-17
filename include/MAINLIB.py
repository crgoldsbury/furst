


class FurstInterpreter:
    def __init__(self,text):
        self.text=text;#input string
        self.pos=0; #position in characters

        self.current_token=None;#current token
        self.current_char=self.text[self.pos]

    def advance(self): #go forward one position
        self.pos+=1;
        if self.pos==len(self.text):
            self.current_char=None;
        self.current_char=self.text[self.pos]

    def peek(self): #like advance but returns the next char
        peekpos=len(self.text)
        peekpos+=1;
        if self.pos==len(self.text):
            return None;
        return self.text[peekpos]
