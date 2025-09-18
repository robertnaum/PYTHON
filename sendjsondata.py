import requests

response = requests.post("https://jsonplaceholder.typicode.com/posts", 
                         json = {"title":"JSON Post", 
                                 "body":"Data",
                                 "userId":2})

print(response.json())
