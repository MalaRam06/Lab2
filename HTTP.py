import requests  # Import the requests library for HTTP requests

# Send GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print("Status Code:", response.status_code)
print("Headers:", response.headers)
print("Body:", response.text)

# Send POST request
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print("POST Status Code:", response.status_code)
print("Response Body:", response.json())
