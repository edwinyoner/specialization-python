for i in range(4):
    print("* " * (i + 1))

print(" ")

n = 4
for i in range(n):
    print("* " * (n))
    n -= 1

print(" ")

n = 4
for i in range(n):
    print("  " * (n - i) + "* " * (i + 1))

print(" ")

n = 3
for i in range(n):
    print("  " * (n - i) + "  * " * (i + 1))

print(" ")

n = 5
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)