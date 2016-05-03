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
'''
def word_count(l):
    count = 0 
    for ele in l:
        count += len(ele)
    return count
''' 
    
def main(args):
    x = args[1]
    sum_count = 0
    for line in open(x,'r'):
        s = line[:-1].split("\t")
        remove_empty(s)
        sum_count += 1
    print(sum_count)

if __name__ == '__main__':
    main(argv)

