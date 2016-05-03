#!/usr/bin/env python3

import sys

argv = sys.argv
if len(argv) != 3:
    print('Usage: # python %s f1 f2' % argv[0]) 
    quit()
    
def remove_empty(l):
    if l.count("")>0:
        l.remove("")
        remove_empty(l)
    else:
        return l
    
def main(args):
    x1 = args[1]
    x2 = args[2]
    f = open('col_merge.txt','w')

    for l1,l2 in zip(open(x1,'r'),open(x2, 'r')):
        s1 = l1[:-1].split("\t")
        s2 = l2[:-1].split("\t")
        remove_empty(s1)
        remove_empty(s2)
        st1 = " ".join(s1)
        st2 = " ".join(s2)
        f.write(st1 + "\t" + st2 + "\n")
    f.close()

    
if __name__ == '__main__':
    main(argv)
