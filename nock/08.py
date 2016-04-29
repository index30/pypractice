#coding: UTF-8

import sys

argv = sys.argv
if len(argv) != 2:
    print('Usage: # python %s x' % argv[0]) 
    quit()

s_list = []

def cipher(x):
    for i in range(len(x)):
        v = ord(x[i])
        if v > 96:
            v = 219 - v
        s_list.append(chr(v))
    return "".join(s_list) 

def main(args):
    x = args[1]
    print(cipher(x))
    
if __name__ == '__main__':
    main(argv)
