s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

l = s.split(" ")

for i in range(len(l)):
    l[i] = l[i].split(",")[0]
    l[i] = l[i].split(".")[0]

count = []

for el in l:
    count.append(len(el))

print(count)

