import pytest
import requests

@pytest.fixture
def unitTest():
    response = requests.get("http://localhot:520")
    assert response.status_code == 200