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
    split = int(max_l / num)
    length = range(max_l)
    count = 0
    
    for c1 in range(num):
        filename = "file"+str(c1)
        wf = open(filename, 'w')
        for c2 in range(split*c1,split*(c1+1)):
            wf.write(l[c2]+"\n")
        wf.close()
    
    f.close()

    
if __name__ == '__main__':
    main(argv)
