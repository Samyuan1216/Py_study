d1 = {}
print(d1)

d1["a"] = 1;
print(d1)

print(d1.pop("a"))

d1["b"] = 2;
print(d1)

d2 = d1
print(d2)

del d1["b"]
print(d1)
print(d2)

d1["a"] = 2
print(d1.get("a"))

d2["b"] = 3
print(d1.keys())
print(d1.values())
print(d2.items())
