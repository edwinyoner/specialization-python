import numpy as np
#help(np.array)
#array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,like=None)
a = [2, 3, 4]
b = [
        [4, 6, 3, 4],
        [1, 2, 7, 2],
        [9, 4, 7, 1],
        [6, 4, 0, 2]
    ]
v = np.array(a, dtype=np.int16)
print(v)
m = np.array(b, dtype=np.uint8)
print(m)
#Atributos
print(v, v.ndim, v.shape, v.dtype)
print(m, m.ndim, m.shape, m.dtype)
print(a[1], a[-2])

#Indexaciòn
print(b[0][1], b[3][0])
print(m[0, 1], m[3, 0])

#Slacing
print(m[1:2, 1:3])

print(m[1:4, 1:3])

print(m[0:, 1:])

print(m[3:, 1:2])


