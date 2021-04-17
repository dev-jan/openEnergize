from ..app import app


def test_storages_getall():
    """
    GIVEN the Flask REST Backend is configured for testing and running
    WHEN the /totals endpoint is called (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/totals/')
        assert response.status_code == 200
        assert response.json['totalEnergyProduction'] == 2360.5
        assert response.json['totalEnergyConsumption'] == 1544.16
        assert response.json['energySum'] == 816.3399999999999
