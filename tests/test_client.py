import pytest
from requests import HTTPError


def test_client_404(client):
    with pytest.raises(HTTPError):
        client.get('/xxx')
