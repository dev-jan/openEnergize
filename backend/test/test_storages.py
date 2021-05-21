from ..app import app


def test_storages_getall():
    """
    GIVEN the Flask REST Backend is configured for testing and running
    WHEN the /storages endpoint is called (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/api/storages/')
        assert response.status_code == 200
        assert response.json[0]['name'] == 'Basement Battery'
        assert response.json[0]['id'] == 0
        assert response.json[0]['type'] == 'constant'
        assert response.json[0]['currentStorageCapacityInPercent'] == 98.0
        assert response.json[1]['name'] == 'Roof Battery'
        assert response.json[1]['currentStorageCapacityInPercent'] == 13
