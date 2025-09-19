import requests

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title":"New Post", "body":"hello world", "userId":1}
)

print(response.json())

print()

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())