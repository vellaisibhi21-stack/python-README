from app.main import add, farewell, greet


def test_feat_1_add():
    assert add(2, 3) == 5


def test_feat_1_greeter():
    assert greet("World") == "Hello, World!"


def test_feat_2_greet_blank_name():
    assert greet("  ") == "Hello, world!"
    assert greet() == "Hello, world!"


def test_feat_12_farewell():
    assert farewell("World") == "Goodbye, World!"
    assert farewell(" ") == "Goodbye, world!"
