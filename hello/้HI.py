def say_hello(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print(say_hello("GitHub"))
    result = add(5, 7)
    print(f"5 + 7 = {result}")
