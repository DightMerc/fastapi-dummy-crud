from starlette import status


def test_login(db, client):
    response = client.post(
        "/auth/login", json=dict(username="test", password="testpwd")
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_sign_up(db, client):
    response = client.post(
        "/auth/signup", json=dict(username="test", password="testpwd")
    )
    assert response.status_code == status.HTTP_200_OK
