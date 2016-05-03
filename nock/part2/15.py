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

def file_to_list(f,l):
    for c in f:
        s = c[:-1].split("\t")
        remove_empty(s)
        st = "\t".join(s)
        l.append(st)
    return l
    
def main(args):
    x = args[1]
    num = int(args[2])
    f = open(x,'r')
    l = []

    fl = file_to_list(f,l)
    max_l = len(l)
    length = range(max_l)
    
    for ele,n in zip(l,length):
        if (max_l - 1 - num) < n:
            print(ele)

    f.close()

    
if __name__ == '__main__':
    main(argv)
