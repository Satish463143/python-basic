from tkinter.constants import E


s= {1,2,3,4,5}
print(type(s))

e = set()
print(type(e))

e.add(1)
e.add(2)
e.add("satish")
e.add(2)
e.add(6)

# len(e)
# print(len(e))
# print(e.remove(2))
# print(e)
print (s.union(e))
print (s.intersection(e))
print (e.issuperset({1,2,5})) #flase
print (s.issubset({1,2,3,4,5,6})) #true
print ({1,6}.issuperset(s)) #flase