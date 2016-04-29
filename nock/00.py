i_line = raw_input()

#l1 = " ".join(i_line).split()

#l2 = list(reversed(l1))

#l3 = "".join(l2)

#print(l3)

# if 1-liner
l = "".join(list(reversed(" ".join(i_line).split())))

print(l)
