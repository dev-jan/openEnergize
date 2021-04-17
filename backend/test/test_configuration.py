from ..app import app


def test_configuration_getall():
    """
    GIVEN the Flask REST Backend is configured for testing and running
    WHEN the /configuration endpoint is called (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/configuration/')
        assert response.status_code == 200
        assert 'Solarpanel 1' in response.json['raw']
        assert 'check_every: 60' in response.json['raw']
