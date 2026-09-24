s = [1, 2, 3, 4, "AB", "H", True]
print(type(s))

print(s[0])
print(s[-7])

print(s)
s[2] = "3"
print(s)

del s[2]
print(s)

for x in s:
    print(x)

