total = 10000

password = input("请输入你的密码：")
print(f"密码正确，{password}")

num = input("请输入你的取款金额：")

print(f"取款后银行卡余额为：{total - int(num)}")
