from app.main import add, cheer, farewell, greet, shout, wave, whisper


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


def test_feat_22_shout():
    assert shout("Ana") == "HELLO, ANA!"
    assert shout() == "HELLO, WORLD!"


def test_feat_36_whisper():
    assert whisper("Ana") == "hello, ana!"
    assert whisper() == "hello, world!"


def test_feat_41_wave():
    assert wave("Ana") == "\N{WAVING HAND SIGN} Hello, Ana!"


def test_feat_49_cheer():
    assert cheer("Ana") == "Hello, Ana! \N{PARTY POPPER}"
    assert cheer() == "Hello, world! \N{PARTY POPPER}"
