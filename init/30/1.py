msg = input()

for c in msg:
    print(f"c: {c}")
    if c == '-':
        break
else:
    print("Fin")

total = 0
for i in range(1, 101, 2):
    total += i

print(total)
