import pytest

from botmaker import Client
from botmaker.exc import InvalidAuth


@pytest.mark.vcr
def test_invalid_auth():
    invalid_access_token = 'xxx'
    client = Client(invalid_access_token)
    with pytest.raises(InvalidAuth):
        client.get('/auth/credentials')


@pytest.mark.vcr
def test_valid_auth(client):
    resp = client.get('/auth/credentials')
    expected_resp_key = {'accessToken', 'clientId', 'refreshToken', 'secretId'}
    assert set(resp.keys()) == expected_resp_key
