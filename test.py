word = ['abc', 'df',7, 8]

# word2 = ['efg', 'hij',10,11]

# word2.extend("word") # here word act as a sting 
# word2.extend(word) # here word is defined list 
# word2.append(word) 
# word2.append("word")
# print(word2)

# even = []

# for i in range (2,101, 2):
#     even.append(i)

# print(even)


# # multipple of 11 1000 times

# for i in range (11,1001,11):
#     print(i)





# try:
#     word.remove('ab5')  
#     print(word)
# except: print('no such data')


number = [2,3,4,6,7,8,4,3,2,4,"4"]


# evenNumber  = [item for item in number   if item %2 ==0]
cube = [item ** 3 for item in number ]

# for i in number:
#     if i % 2 == 0:
#         evenNumber.append(i)

print(cube)