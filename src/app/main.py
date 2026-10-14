def add(a: int, b: int) -> int:
    return a + b


def greet(name: str = "") -> str:
    name = name.strip()
    return f"Hello, {name}!" if name else "Hello, world!"


def farewell(name: str = "") -> str:
    name = name.strip()
    return f"Goodbye, {name}!" if name else "Goodbye, world!"


def shout(name: str = "") -> str:
    return greet(name).upper()


def whisper(name: str = "") -> str:
    return greet(" ".join(name.split())).lower()


if __name__ == "__main__":
    print(greet("LaneSync"))
