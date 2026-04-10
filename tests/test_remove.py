import pytest

def test_remove_success(client):
    # Arrange
    email = "aluno@email.com"
    client.post("/activities/basketball/signup", json={"email": email})
    # Act
    response = client.delete(f"/activities/basketball/remove?email={email}")
    # Assert
    assert response.status_code == 200
    assert email not in response.json()["participants"]

def test_remove_activity_not_found(client):
    # Arrange
    email = "aluno@email.com"
    # Act
    response = client.delete(f"/activities/naoexiste/remove?email={email}")
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_remove_participant_not_found(client):
    # Arrange
    email = "naoexiste@email.com"
    # Act
    response = client.delete(f"/activities/basketball/remove?email={email}")
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
