# list 

# friend = ["satish", 24, 57.5, "mahato", "ktm", True ]

# chnageIndex = friend[3]= "satish mahato"

# # print (friend)

# number = ["2","5","1","9","6","3","4","7","8"]

# number.sort()
# number.reverse()
# number.append("12")
# number.insert (4,"11")
# pop = number.pop(5)
# print(pop)

# number.remove(5)
# number.clear()
# number.insert(0,"10")
# print(number)

# practicefruits = []
# fruits = []
# f1 = input("Enter the fruit 1: ")
# fruits.append(f1)
# f2 = input("Enter the fruit 2: ")
# fruits.append(f2)
# f3 = input("Enter the fruit 3: ")
# fruits.append(f3)
# f4 = input("Enter the fruit 4: ")
# fruits.append(f4)
# f5 = input("Enter the fruit 5: ")
# fruits.append(f5)
# f6 = input("Enter the fruit 6: ")
# fruits.append(f6)
# print(fruits)

# mark1 = []
# m1 = int(input("enter the mark 1: "))
# mark1.append(m1)
# m2 = int(input("enter the mark 2: "))
# mark1.append(m2)
# m3 = int(input("enter the mark 3: "))
# mark1.append(m3)
# m4 = int(input("enter the mark 4: "))5

# mark1.append(m4)
# m5 = int(input("enter the mark 5: "))
# mark1.append(m5)

# mark1.sort()  # sorts the list in-place
# print(mark1)  # prints the sorted list

# list = []
# n1 = int(input("enter the number 1: "))
# list.append(n1)
# n2 = int(input("enter the number 2: "))
# list.append(n2)
# n3 = int(input("enter the number 3: "))
# list.append(n3)
# n4 = int(input("enter the number 4: "))
# list.append(n4)

# sum = n1 + n2 + n3 + n4
# print(sum)

list =[22,45,32,34]
# This throws an error because Python lists do not have a 'map' method,
# and the syntax 'perv => prev + curr' is invalid in Python.
# To sum the elements of a list in Python, use the built-in sum() function:
sum = sum(list)
print(sum)