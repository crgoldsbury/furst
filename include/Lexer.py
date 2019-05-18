

class Lexer:
    #CRG:  this isa custom initializer for the class.
    def __init__(self,codeline):
        self.codeline = codeline
        self.listofcodestrings = list()
        
    #CRG:  This function will make a decision on what to do with each line.
    def interpretLine():
        #CRG: clean up the codeline nad trim the spaces on front or back.
        #this will lead to greater efficiency.
        self.codeline = self.codeline.trim()
                #CRG: if the line is empty we don't want to do anything. 
        # we can skip it.  This will reduce errors and speed up the
        # interpretation.
        
        if self.codeline.length >0:            
           #CRG: ok...now split the codeline into a character array.
           # this will make it easier to iterate through each character.
           # spaces will be delimiters and tell us  
           self.listofcodestrings = self.codeline.split()
           #CRG:  Ok..now we need to iterate through each string
           # in the list and determine what it is.  It could be:
           # 1. A value.
           # 2. A keyword.
           # 3. An opreator
           # 4. a variable.
           # We'll have to pass the string to each function below and determine
           # which one it is.
        
        
    def IsAValue(self):
        #CRG: function should return true if it's a user defined value.
    
    def IsAKeyword(self):
        #CRG: function should return true if it's a keyword.
        
    
    def IsAnOperator(self):
        #CRG: funciton should return true if it's an operator.
    
    def IsAVariable(self):
        #CRG:  function should return true if it's a variable.
    
