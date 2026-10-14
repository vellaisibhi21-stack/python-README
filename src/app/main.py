def add(a: int, b: int) -> int:
    return a + b


def greet(name: str = "") -> str:
    name = name.strip()
    return f"Hello, {name}!" if name else "Hello, world!"


if __name__ == "__main__":
    print(greet("LaneSync"))
