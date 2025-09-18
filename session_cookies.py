import requests

#Creates a new session object. A session allows you to persist certain parameters (like cookies) across multiple requests.
session = requests.Session()

#Sends a GET request to httpbin.org to set a cookie named sessioncookie with the value 123 in the session.
session.get("https://httpbin.org/cookies/set/sessioncookie/123")

#Sends another GET request to retrieve all cookies currently stored in the session.
response = session.get("https://httpbin.org/cookies")

#Prints the JSON response, which shows the cookies stored in the session (including the one you just set).
print(response.json())

