import pytest
from requests import HTTPError


@pytest.mark.vcr
def test_client_404(client):
    with pytest.raises(HTTPError):
        client.get('/xxx')
