from starlette import status


def test_create(db, client):
    client.post("/auth/signup", json=dict(username="test", password="testpwd"))
    login_resposne = client.post(
        "/auth/login", json=dict(username="test", password="testpwd")
    ).json()
    response = client.post(
        "/users/user",
        json=dict(name="Jane Doe"),
        headers={"Authorization": f"Bearer {login_resposne['access_token']}"},
    )
    assert response.status_code == status.HTTP_200_OK


def test_list(db, client):
    client.post("/auth/signup", json=dict(username="test", password="testpwd"))
    login_resposne = client.post(
        "/auth/login", json=dict(username="test", password="testpwd")
    ).json()
    response = client.get(
        "/users/user?user_id=1",
        headers={"Authorization": f"Bearer {login_resposne['access_token']}"},
    )
    assert response.status_code == status.HTTP_200_OK


def test_update(db, client):
    client.post("/auth/signup", json=dict(username="test", password="testpwd"))
    login_resposne = client.post(
        "/auth/login", json=dict(username="test", password="testpwd")
    ).json()
    response = client.put(
        "/users/user?user_id=1",
        json=dict(name="John Doe"),
        headers={"Authorization": f"Bearer {login_resposne['access_token']}"},
    )
    assert response.status_code == status.HTTP_200_OK

    list_response = client.get(
        "/users/user?user_id=1",
        headers={"Authorization": f"Bearer {login_resposne['access_token']}"},
    ).json()

    assert list_response == [
        {"id": 1, "name": "John Doe", "active": True, "username": "test"}
    ]


def test_delete(db, client):
    client.post("/auth/signup", json=dict(username="test", password="testpwd"))
    login_resposne = client.post(
        "/auth/login", json=dict(username="test", password="testpwd")
    ).json()
    client.post(
        "/users/user",
        json=dict(name="Jane Doe"),
        headers={"Authorization": f"Bearer {login_resposne['access_token']}"},
    )
    response = client.delete(
        "/users/user?user_id=2",
        headers={"Authorization": f"Bearer {login_resposne['access_token']}"},
    )
    assert response.status_code == status.HTTP_200_OK

    list_response = client.get(
        "/users/user?user_id=2",
        headers={"Authorization": f"Bearer {login_resposne['access_token']}"},
    )

    assert list_response.status_code == status.HTTP_404_NOT_FOUND
    assert list_response.json() == {"detail": "User not found"}
