# This is the furst interpreter for javascript. Created 5/16/2019
from include.MAINLIB import *
from sys import *
import io
import Lexer

#CRG: Prior to opening the file; we'll create a Lexer.  We'll need it later.
decisionmaker = Lexer()

#CRG: First Step...open the source file and read each line.  
# We do line for line read to be efficient with memory.  
# Some .js files can be very large and using something like 
# contents = file.read()  would result in high memory utilization and slow
# performance.


file = open("source.js")
for line in file:
    #For each line in the file we want to pass it to a class 
    #that will decide what to do with the line.
    Lexer(line)

#CRG: Can't forget to close the file.
file.close()

#CRG: This is owen's original code.  I've kept, but commented out.
#if __name__ == '__main__':
 #   args = argv[1]
  #  file = io.open(args)
   # p = FurstInterpreter(file.read())
    #p.start()
    #file.close()




