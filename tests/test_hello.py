from hello import make_message

def test_make_message_world():
    assert make_message("world") == "Hello, world!"

def test_make_message_name():
    assert make_message("Aono") == "Hello, Aono!"