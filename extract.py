print()

f_in = open('in.txt', 'r')
f_out = open('out.txt', 'w')
list = []


for line in f_in:
    list.append(line.strip())
    print(line, end='\n')


for line in f_in:
    if 'http' in line:
        list.append(line.split())


n1 = 0
n2 = 0

for thing in list:
    n1 += 1

for thing in list:
    if 'http' in thing[1]:
        n2 += 1
        f_out.write(thing[1]+'\n')
    else:
        print(thing)

print(n1, ' = ', n2)



f_in.close()
f_out.close()
