import requests

def send_get_request(endpoint):
    response = requests.get(endpoint)
    return response

def send_post_request(endpoint, data):
    response = requests.post(endpoint, json=data)
    return response
