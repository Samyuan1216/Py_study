num = int(input())
check = int(input())

match num:
    case 0:
        print("zero")
    case 1 | 2:
        print("one or two")
    case 3 if check == 3:
        print("three")
    case _:
        print(f"{num} {check}")
