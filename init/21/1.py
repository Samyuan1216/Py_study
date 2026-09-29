num = int(input("请输入一个整数："))
print(f"{num}在10-20之间", num >= 10 and num <= 20)
print(f"{num}在10-20之间", 10 <= num <= 20)
print(f"{num}在10-20之间", not(num < 10 or num > 20))

