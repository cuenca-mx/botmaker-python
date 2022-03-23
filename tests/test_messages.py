import pytest

from botmaker.exc import InvalidPhoneNumber


@pytest.mark.vcr
def test_message(client):
    tm = client.messages.create(
        '5215500000000',
        '+55 1 55 1234 5678',
        message_text='message test',
    )
    assert tm.id
    assert tm == tm
    assert repr(tm)
    assert str(tm)
    assert tm.to == '5515512345678'


@pytest.mark.vcr
def test_invalid_whatsapp_number_message(client):
    with pytest.raises(InvalidPhoneNumber):
        client.messages.create(
            '5215500000000',
            '123',
            check_phone=True,
            message_text='message test',
        )
