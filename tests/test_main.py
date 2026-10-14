from app.main import add, greet


def test_feat_1_add():
    assert add(2, 3) == 5


def test_feat_1_greeter():
    assert greet("World") == "Hello, World!"


def test_feat_2_greet_blank_name():
    assert greet("  ") == "Hello, world!"
    assert greet() == "Hello, world!"
