from ..app import app


def test_consumers_getall():
    """
    GIVEN the Flask REST Backend is configured for testing and running
    WHEN the /consumers endpoint is called (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/api/consumers/')
        assert response.status_code == 200
        assert response.json[0]['name'] == 'Washing Machine'
        assert response.json[0]['id'] == 0
        assert response.json[0]['type'] == 'fakeControllable'
        assert response.json[0]['currentConsumptionInWatt'] == 111.0
        assert response.json[0]['isControllable']
        assert response.json[0]['status'] == 'READY'
        assert response.json[1]['name'] == 'Car'


def test_consumers_getById():
    """
    GIVEN the Flask REST Backend is configured for testing and running
    WHEN the /consumers/:id endpoint is called with a valid consumer ID
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/api/consumers/2')
        assert response.status_code == 200
        assert response.json['name'] == 'Outdoor Light'
        assert response.json['id'] == 2
        assert response.json['type'] == 'constant'
        assert response.json['currentConsumptionInWatt'] == 0.0
        assert not response.json['isControllable']
        assert response.json['status'] == 'UNKNOWN'


def test_consumers_getById_invalid():
    """
    GIVEN the Flask REST Backend is configured for testing and running
    WHEN the /consumers/:id endpoint is called with an invalid producer ID
    THEN check that the response is 404
    """
    with app.test_client() as test_client:
        response = test_client.get('/api/consumers/999999')
        assert response.status_code == 404
