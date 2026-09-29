s1 = {5, 4, 3, 2, 1, 10, 11, -1}
print(s1)
print(type(s1))

s2 = set()
print(s2)
print(type(s2))

s2.add(10)
print(s2)

s2.remove(10)
print(s2)

for i in range(5, 11):
    s2.add(i)

print(s2)

print(s2.pop())
print(s2)

print(s2 - s1)
print(s2.difference(s1))

print(s2 | s1)
print(s2.union(s1))

print(s2 & s1)
print(s2.intersection(s1))

print({i for i in range(1, 11) if i % 2 == 0})
