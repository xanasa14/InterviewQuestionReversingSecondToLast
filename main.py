lista =[0,1,2,3,4,5]
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
if (len(RE) <= len(RO)):
    for i in range(len(RE)):
        answer.append(RE[i])
        answer.append(RO[i])
else:
    for i in range(len(RE)-1):
        answer.append(RE[i])
        answer.append(RO[i])
    answer.append(RE[-1])
    
print(answer)
