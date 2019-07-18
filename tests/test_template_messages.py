import pytest

from botmaker.exc import InvalidPhoneNumber


@pytest.mark.vcr
def test_template_message(client):
    tm = client.template_messages.create(
        '5215500000000',
        '+55 1 55 1234 5678',
        'phone_number_verification',
        codigo_de_6_digitos='123456',
    )
    assert tm.id
    assert tm == tm
    assert tm.to == '5515512345678'


@pytest.mark.vcr
def test_invalid_whatsapp_number(client):
    with pytest.raises(InvalidPhoneNumber):
        client.template_messages.create(
            '5215500000000',
            '123',
            'phone_number_verification',
            codigo_de_6_digitos='123456',
        )
