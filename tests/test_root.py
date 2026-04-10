def test_root_redirects_to_static(client):
    # Arrange: client já fornecido pela fixture
    # Act
    response = client.get("/")
    # Assert
    assert response.status_code in (200, 307, 302)
    assert "/static/index.html" in str(response.url) or response.headers.get("location", "").endswith("/static/index.html")
