#coding: UTF-8

import sys

argv = sys.argv
if len(argv) != 4:
    print('Usage: # python %s x y z' % argv[0]) 
    quit()

def main(args):
    x = args[1]
    y = args[2]
    z = args[3]
    print(x+"時の"+y+"は"+z) 
    
if __name__ == '__main__':
    main(argv)
