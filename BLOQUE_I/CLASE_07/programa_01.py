a = True
b = False
c = a.__and__(b)
print(c)
d = a and b
print(d)
print(not(d))
e = not((a > b) and (b != a))
print(e)