name = "Bipul Chaudhary"
address = "Toronto Canada"

print(name)
print(address)

# slicing
print(name[0])
print(name[-1])
print(name[0:7])
print(name[::])
print(name[::-1])
print(name[::2])
print(name[-8:-1])
print(name[-9:])
print(name[-9:-1])


print(name.upper())
print(name.lower())
dob = int(input("Year of birth: "))
age = 2022 - dob
print(f"{name} was born in {dob}. So he is now {age}")
name2 = name.replace("B", "T")
print(name2)
name3 = "             Madhu"
print(name3.strip())
print(len(name3.strip()))
print(name3.count("M"))
print(name.find('a'))
