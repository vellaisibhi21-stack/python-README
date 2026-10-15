def add(a: int, b: int) -> int:
    return a + b


def greet(name: str | None = "") -> str:
    name = (name or "").strip()
    return f"Hello, {name}!" if name else "Hello, world!"


def farewell(name: str | None = "") -> str:
    name = (name or "").strip()
    return f"Goodbye, {name}!" if name else "Goodbye, world!"


def shout(name: str = "") -> str:
    return greet(name).upper()


def whisper(name: str = "") -> str:
    # Lower-case letters only; emoji and other symbols in the name are kept as given.
    return "".join(c.lower() if c.isalpha() else c for c in greet(name))


def wave(name: str = "") -> str:
    return f"\N{WAVING HAND SIGN} {greet(name)}"


def cheer(name: str = "") -> str:
    return f"{greet(name)} \N{PARTY POPPER}"


if __name__ == "__main__":
    print(greet("LaneSync"))
