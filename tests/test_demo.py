from rest_framework import status


def test_demo_view(api_client):
    """Just to demo testing api."""
    res = api_client.get('/demo/')
    assert res.status_code == status.HTTP_200_OK
    assert res.data == 'Hello!'


def test_demo_view_post(api_client):
    """Just to demo testing api."""
    payload = {
        "msg": "Hello again!"
    }
    res = api_client.post('/demo/', payload)
    assert res.status_code == status.HTTP_200_OK
    assert res.json() == payload
