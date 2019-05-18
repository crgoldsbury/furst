# This is the furst interpreter for javascript. Created 5/16/2019
from include.MAINLIB import *
from sys import *
import io
if __name__ == '__main__':
    args = argv[1]
    file = io.open(args)
    p = FurstInterpreter(file.read())
    p.start()
    file.close()




