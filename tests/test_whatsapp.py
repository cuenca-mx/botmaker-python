import pytest

from botmaker.exc import BotmakerException


@pytest.mark.vcr
def test_check_whatsapp_contact(client):
    phone_number = '+55 1 55 1234 5678'
    checked_contact = '5515512345678'
    assert checked_contact == client.check_whatsapp_contact(
        '5215500000000', phone_number
    )


@pytest.mark.vcr
def test_invalid_whatsapp_contact(client):
    assert client.check_whatsapp_contact('5215500000000', '123') is None


@pytest.mark.vcr
def test_check_whatsapp_contacts(client):
    contacts = ['+55 1 55 1234 5678', '123']
    result = client.check_whatsapp_contacts('5215500000000', contacts)
    assert '+55 1 55 1234 5678' in result  # whatsapp
    assert result['+55 1 55 1234 5678'] == '5515512345678'
    assert '123' not in result  # no whatsapp


@pytest.mark.vcr
def test_invalid_channel(client):
    with pytest.raises(BotmakerException):
        client.check_whatsapp_contacts('52 55 1234 5678', ['123'])
