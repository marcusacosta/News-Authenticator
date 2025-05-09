import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_health(client):
    resp = client.get('/health')
    assert resp.status_code == 200
    assert b'Flask API working!' in resp.data

def test_authenticate(client):
    payload = {'source':'example.com','text':'Test text'}
    resp = client.post('/authenticate', json=payload)
    assert resp.status_code == 200

    data = resp.get_json()
    # Ensure both raw and final prediction fields are present
    for key in (
        'raw_prediction',
        'raw_confidence',
        'source_score',
        'final_prediction',
        'final_confidence'
    ):
        assert key in data, f"Missing key: {key}"
