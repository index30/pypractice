s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

l = s.split(" ")

for i in range(len(l)):
    l[i] = l[i].split(",")[0]
    l[i] = l[i].split(".")[0]

count = 1
d = {}

first = [1,5,6,7,8,9,15,16,19]

for j in l:
    if count in first:
        d.update({j[0]:count})
    else:
        d.update({j[0:2]:count})
    count = count + 1

print(d)
