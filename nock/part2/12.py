#!/usr/bin/env python3

import sys

argv = sys.argv
if len(argv) != 2:
    print('Usage: # python %s x' % argv[0]) 
    quit()
    
def remove_empty(l):
    if l.count("")>0:
        l.remove("")
        remove_empty(l)
    else:
        return l
    
def main(args):
    x = args[1]
    f1 = open('col1.txt','w')
    f2 = open('col2.txt','w')
    for line in open(x,'r'):
        s = line[:-1].split("\t")
        remove_empty(s)
        #st = " ".join(s)
        f1.write(s[0] + "\n")
        f2.write(s[1] + "\n")
    f1.close()
    f2.close()
    
if __name__ == '__main__':
    main(argv)
