# 1
a=[]
print (type(a))

b= ()
print (type(b))

# 2
int = [1,2,3,4,5]

# 3
c = [1, 2, 3]
c.append(4)
print (c)

# 4
d= [10, 20, 30, 40]
d.pop(3)
print (d)

#5
e = [5, 10, 15, 20, 25]
e.pop(2)
print (e)

#6
t = (1, 2, 3, 4)
# tuple is immutable cant add 5 

# 7
f = [3, 6, 9, 12]
f.insert[2:10]
print (f)

# 8
g= [1, 2, 3, 4, 5, 6]
even = (g%2 ==0)
print (even)

#9

t = (2, 4, 6, 8)
list = list(t)
list.append(10)
print (list)

#10
h = [1, 2, 3, [4, 5]]
h[3][1] = 50
print(h)

#11
i = [1, 2, 2, 3, 4, 2]
i.remove(2)
print(i)

#12
a = [[1, 2]] * 2
a[1][0] = 99
print(a)

#13
t = (1, [2, 3], 4)
# cnat change tuple

#14
j = [10, 20, 30, 40, 50]
j.remove[1:3]
print(j)

#15
a = [1, 2, 3, 4, 5]
square = [a**2 for a in a]
print(square)
