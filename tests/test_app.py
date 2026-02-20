def test_root_endpoint(client):
    # Arrange
    expected_status = 200
    expected_response = {"message": "Hello, World!"}  # Adjust based on your app's response

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == expected_status
    assert response.json() == expected_response

def test_404_endpoint(client):
    # Arrange
    nonexistent_path = "/nonexistent"
    expected_status = 404

    # Act
    response = client.get(nonexistent_path)

    # Assert
    assert response.status_code == expected_status