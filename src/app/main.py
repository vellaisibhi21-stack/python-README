def add(a: int, b: int) -> int:
    return a + b


def greet(name: str | None = "") -> str:
    name = (name or "").strip()
    return f"Hello, {name}!" if name else "Hello, world!"


def farewell(name: str = "") -> str:
    name = name.strip()
    return f"Goodbye, {name}!" if name else "Goodbye, world!"


def shout(name: str = "") -> str:
    return greet(name).upper()


def whisper(name: str = "") -> str:
    return greet(name).lower()


def wave(name: str = "") -> str:
    return f"\N{WAVING HAND SIGN} {greet(name)}"


def cheer(name: str = "") -> str:
    return f"{greet(name)} \N{PARTY POPPER}"


if __name__ == "__main__":
    print(greet("LaneSync"))
