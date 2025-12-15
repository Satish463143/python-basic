# basic python program to import a module
import pyjokes
# print ("hello b")

# joke = pyjokes.get_joke()
# print(joke)

# operators

# a= 10
# b=21

# print (b/a)

############## type conveersion
a = "satish"
b = type(a)
print(b)

c = 23
d = float(c)
t = type(d)
print(t)

############## input function
# e = int (input ("enter first number: "))
# # f = int(input ("enter second number: "))

############ square of a number
# print ((e**2))

############ string slicing
name= "satish mahato"
length = len(name)
shortName = name[-5:-4]
middlevalue = name[1:9:2]
print(middlevalue)

############## string methods
# name = "satish kuamr"
# print (name.endswith("mar"))
# print (name.capitalize())

letter = '''Hello <name> 
 how are  you?
 you are a good boy
 <sign>
 '''

print ((letter.replace("<name>", "satish")).replace("<sign>", "mahato"))

findLetetr = letter.find("o")
print(findLetetr)

rp = letter.replace("o", "z")
print(rp)

sentence = "This a good langauge python. \n\t This is easy to learn. And very efficient"

print (sentence)


