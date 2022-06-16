# while loop
num = 1
while num < 101:
    print(num, end=" ")
    num += 1

print()

# for loop
for i in range(3, 101, 3):
    print(i, end=" ")

print()

# print out the first 10 numbers
for i in range(10):
    print(i, end=" ")

print()

# challenge: print the word "AUM" 108 times

for i in range(1, 109):
    print(str(i) + " AUM")

# challenge: print out number 10 to 1 in reverse order

for i in range(10, 0, -1):
    print(i)

for char in "Bipul Chaudhary":
    print(char)


# use of break

while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is {num1 + num2}")
    should_continue = input("Would you like to continue? Y/N: ")
    if should_continue.upper() == "N":
        break




