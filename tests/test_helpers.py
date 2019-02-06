from botmaker.helpers import sanitize_phone_number


def test_sanitize_phone_number():
    assert sanitize_phone_number('+1 (650).555-1234') == '16505551234'
