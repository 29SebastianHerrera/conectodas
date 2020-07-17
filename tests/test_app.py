from app import *
import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_index_pages_works(client):
    response = client.get('/')
    assert response.status_code == 200




