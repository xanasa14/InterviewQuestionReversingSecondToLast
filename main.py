lista =[0,1,2,3,4,5,6,7,8,9]
e = []
o = []
for i in range(len(lista)):
    if i%2 == 0:
        e.append(lista[i])
    else: 
        o.append(lista[i])
answer = []
RE = e[::-1]
RO = o[::-1]
for i in range(len(RE)):
    answer.append(RE[i])
    answer.append(RO[i])
print(answer)
