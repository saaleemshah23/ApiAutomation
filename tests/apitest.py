import requests
from unittest.mock import patch
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# Test GET Request with Mocking
@patch('requests.get')
def test_get_post(mock_get):
    # Setup the mock response
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "title": "Mocked Post", "body": "This is a mocked post", "userId": 1}

    # Call the function
    response = requests.get(f"{BASE_URL}/posts/1")

    # Assertions
    assert response.status_code == 200
    assert 'title' in response.json()
    assert response.json()['title'] == "Mocked Post"

# Test POST Request with Mocking
@patch('requests.post')
def test_create_post(mock_post):
    # Setup the mock response
    mock_response = mock_post.return_value
    mock_response.status_code = 201
    mock_response.json.return_value = {"id": 101, "title": "Mocked New Post", "body": "This is a new post", "userId": 1}

    # Test data
    new_post = {
        "title": "New Post Title",
        "body": "This is a new post body.",
        "userId": 1
    }

    # Call the function
    response = requests.post(f"{BASE_URL}/posts", json=new_post)

    # Assertions
    assert response.status_code == 201
    assert response.json()['title'] == "Mocked New Post"
    assert 'userId' in response.json()
