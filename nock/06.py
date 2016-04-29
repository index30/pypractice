#coding: UTF-8
import sys
import collections
'''
argv = sys.argv
if len(argv) != 2:
    print 'Usage: # python %s str or list' % argv[0]
    quit()
'''


def strsplit(s):
    sen = s.split(" ")
    for ele in range(len(sen)):
        sen[ele] = sen[ele].split(",")[0]
        sen[ele] = sen[ele].split(".")[0]
    return sen

def make_line(l,n):
    return [l[i: i+n] for i in range(0,len(l),n)]

def make_word_gram(g_seq,n):
    return collections.Counter(g_seq)

def make_char_gram(g_seq,n):
    d = {}
    count = 1
    c_seq = "".join(g_seq)
    l = make_line(c_seq,n)

    return collections.Counter(l)

def main():
    x = "paraparaparadise"
    y = "paragraph"
    gram_num = 2

    c_x = make_char_gram(x,gram_num)
    c_y = make_char_gram(y,gram_num)
    X = set(c_x.items())
    Y = set(c_y.items())
    #和集合
    same_set = X.union(Y)
    print(same_set)
    #差集合
    print(X.difference(Y))
    if 'se' in c_x or 'se' in c_y:
        print "true"

if __name__ == '__main__':
    main()
