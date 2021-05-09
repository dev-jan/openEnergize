from ..app import app


def test_events_getall():
    """
    GIVEN the Flask REST Backend is configured for testing and running
    WHEN the /events endpoint is called (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        response = test_client.get('/api/events/')
        assert response.status_code == 200
        assert isinstance(response.json, list)
