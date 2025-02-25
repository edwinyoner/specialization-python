r = open("datos.txt", 'r')
print(r.read())
r.close()
print("***********")
with open("datos.txt", 'r') as r:
    print(r.read())