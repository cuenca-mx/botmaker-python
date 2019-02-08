from botmaker.exc import BotmakerException


def test_exc_message():
    message = 'Error message'
    e = BotmakerException(message)
    assert e.message == message
    assert str(e) == message
