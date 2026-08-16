# Find the sum of numbers from 1 to n

total = 0
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)
