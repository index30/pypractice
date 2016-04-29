#coding: UTF-8

p = u"パトカー"
t = u"タクシー"
l = []

for i in range(len(p)):
    s = p[i] + t[i]
    l.append(s)

print("".join(l))
