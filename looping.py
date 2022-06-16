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

for _ in range(1, 109):
    print(str(_) + " AUM")


