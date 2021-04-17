from ..app import app


def test_producer_getall():
    """
    GIVEN the Flask REST Backend is configured for testing and running
    WHEN the /producers endpoint is called (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/producers/')
        assert response.status_code == 200
        assert response.json[0]['name'] == 'Solarpanel 1'
        assert response.json[0]['id'] == 0
        assert response.json[0]['type'] == 'constant'
        assert response.json[0]['currentProductionInWatt'] == 2360.2
        assert response.json[1]['name'] == 'Solarpanel 2'


def test_producer_getById():
    """
    GIVEN the Flask REST Backend is configured for testing and running
    WHEN the /producers/:id endpoint is called with a valid producer ID
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/producers/1')
        assert response.status_code == 200
        assert response.json['id'] == 1
        assert response.json['name'] == 'Solarpanel 2'
        assert response.json['type'] == 'constant'
        assert response.json['currentProductionInWatt'] == 0.3


def test_producer_getById_invalid():
    """
    GIVEN the Flask REST Backend is configured for testing and running
    WHEN the /producers/:id endpoint is called with an invalid producer ID
    THEN check that the response is 404
    """
    with app.test_client() as test_client:
        response = test_client.get('/producers/999999')
        assert response.status_code == 404
