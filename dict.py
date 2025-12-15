mark ={
    "mahato":55,
    "ktm":65,
    "nepal":75,
}

# print (mark["satish"])
# print(mark.keys())
# print(mark.values())
# print (mark.items())
# mark.update({"satish":67, "dhele":78})
# print(mark)
# mark.pop("satish")
# print(mark)

# print(mark.get("satish"))
# print(mark["satish"])

langage = {
    "English":"Hello",
    "Nepali":"Namaste",
    "Spanish":"Hola",
}
# country  = langage.keys()
# print(country)
# greeting = langage.values()
# print(greeting)
# print(langage.keys())

chooseCountry = input("Enter the country: ")

print (langage[chooseCountry])

number = {}

number1 = input("Enter the number 1: ")
number.append(number1)
number2 = input("Enter the number 2: ")
number.append(number2)
number3 = input("Enter the number 3: ")
number.append(number3)
number4 = input("Enter the number 4: ")
number.append(number4)
number5 = input("Enter the number 5: ")
number.append(number5)

print(number)
