t1 = 1, 2, 3, 4
a, b, c, d = t1
print(a, b, c, d)

x, *y, z = t1
print(x, y, z)

a, b, c = b, c, a
print(a, b, c, d)
