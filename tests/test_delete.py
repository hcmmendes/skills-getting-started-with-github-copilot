def test_delete_participant_success(client):
    # Arrange
    activity = "Chess Club"
    email = "deleteuser@mergington.edu"
    client.post(f"/activities/{activity}/signup?email={email}")
    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 200
    assert "message" in response.json()


def test_delete_participant_not_found(client):
    # Arrange
    activity = "Chess Club"
    email = "nonexistent@mergington.edu"
    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found in activity"
