import pytest

@pytest.mark.parametrize("activity,email", [
    ("basketball", "aluno1@email.com"),
    ("robotics", "aluno2@email.com")
])
def test_signup_success(client, activity, email):
    # Arrange
    payload = {"email": email}
    # Act
    response = client.post(f"/activities/{activity}/signup", json=payload)
    # Assert
    assert response.status_code == 200
    assert email in response.json()["participants"]

def test_signup_activity_not_found(client):
    # Arrange
    payload = {"email": "aluno@email.com"}
    # Act
    response = client.post("/activities/naoexiste/signup", json=payload)
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_signup_duplicate(client):
    # Arrange
    payload = {"email": "aluno@email.com"}
    client.post("/activities/basketball/signup", json=payload)
    # Act
    response = client.post("/activities/basketball/signup", json=payload)
    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()
