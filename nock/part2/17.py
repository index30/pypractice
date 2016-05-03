#!/usr/bin/env python3

import sys

argv = sys.argv
if len(argv) != 2:
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
        st = "".join(s[0].decode('utf-8'))
        l.append(st)
    return l
    
def main(args):
    x = args[1]
    f = open(x,'r')
    l = []
    sl = []

    file_to_list(f,l)
    
    for ele in l:
        sl.append(ele)
    print(sl)

    
if __name__ == '__main__':
    main(argv)
