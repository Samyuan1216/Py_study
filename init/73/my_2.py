__all__ = ["f"]

num: int = 10
def f(x: int) -> int:
    return x ** 2

if __name__ == '__main__':
    print(f"in my_2: {f(10)}")
