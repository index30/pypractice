#!/usr/bin/env python3

import sys

argv = sys.argv
if len(argv) != 3:
    print('Usage: # python %s f num' % argv[0]) 
    quit()
    
def remove_empty(l):
    if l.count("")>0:
        l.remove("")
        remove_empty(l)
    else:
        return l

def main(args):
    x = args[1]
    num = range(int(args[2]))

    for l,n in zip(open(x,'r'),num):
        s = l[:-1].split("\t")
        remove_empty(s)
        st = "\t".join(s)
        print(st)


    
if __name__ == '__main__':
    main(argv)
