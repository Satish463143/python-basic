

a = (45,55,66,33,66,False,222,"Satish",678)
b = (1,2,3,0,4,5,6,0,7,0,8,0,9,10)

print (type(a))

# //methood of tuple

# print(a.count(66))

i = a.index(33)
# print(i)

ConcatenateTuple = a + b
# print(ConcatenateTuple)

repeat = a *2
# print(repeat)
print(max(b))
print(min(b))

print(b.count(0))
b[3]=100
print(b)