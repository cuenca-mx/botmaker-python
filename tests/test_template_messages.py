import pytest


@pytest.mark.vcr
def test_template_message(client):
    tm = client.template_messages.create(
        '5215500000000', '5215522222222', 'phone_number_verification',
        codigo_de_6_digitos='123456')
    assert tm.id
    assert tm == tm
    assert repr(tm)
    assert str(tm)
