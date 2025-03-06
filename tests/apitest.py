import requests
import json

# Base URL of the sample API
BASE_URL = "https://jsonplaceholder.typicode.com/"

# Helper function to print formatted response
def print_response(response):
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {json.dumps(response.json(), indent=4)}")
    print("-" * 50)

# 1. GET Request: Fetch a single post
def get_post(post_id):
    url = f"{BASE_URL}posts/{post_id}"
    response = requests.get(url)
    print_response(response)
    assert response.status_code == 200, f"Failed to fetch post {post_id}"

# 2. POST Request: Create a new post
def create_post(title, body, user_id):
    url = f"{BASE_URL}posts"
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(url, json=data)
    print_response(response)
    assert response.status_code == 201, "Failed to create post"

# 3. PUT Request: Update a post
def update_post(post_id, title, body, user_id):
    url = f"{BASE_URL}posts/{post_id}"
    data = {
        "id": post_id,
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.put(url, json=data)
    print_response(response)
    assert response.status_code == 200, "Failed to update post"

# 4. DELETE Request: Delete a post
def delete_post(post_id):
    url = f"{BASE_URL}posts/{post_id}"
    response = requests.delete(url)
    print_response(response)
    assert response.status_code == 200, f"Failed to delete post {post_id}"

# 5. Running the tests
if __name__ == "__main__":
    # 1. Test GET request
    get_post(1)
    
    # 2. Test POST request
    create_post("Test Post Title", "This is the body of the post", 1)
    
    # 3. Test PUT request
    update_post(1, "Updated Title", "This is the updated body", 1)
    
    # 4. Test DELETE request
    delete_post(1)