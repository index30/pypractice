import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

l = s.split(" ")

for i in range(len(l)):
    l[i] = l[i].split(",")[0]
    l[i] = l[i].split(".")[0]
    l[i] = l[i].split(":")[0]
    
def random_line(length,r_list,com):
    if com == length:
        return r_list
    else:
        rand = random.randint(0,length)
        if rand in r_list:
            random_line(length,r_list,com)
        else:
            r_list[com] = rand
            random_line(length,r_list,com+1)

def random_display(d):
    return "test"
            
def random_sort(l):
    f_l = []
    for a in range(len(l)):
        ch = []
        d = {}
        le = len(l[a])-2
        if len(l[a]) > 4:
            r = [0]*le
            random_line(le,r,0)
            for b in range(1,len(l[a])-1):
                d.update({l[a][b]:r[b-1]})
            for k,v in sorted(d.items(),key=lambda x:x[1]):
                ch.append(k)
            cha = "".join(ch)
            n_l = l[a][0] + cha + l[a][len(l[a])-1]
            l[a] = n_l
        if len(l[a]) != 0:
            f_l.append(l[a])    
    print(f_l)

random_sort(l)

