import requests

#Imports the HTTPBasicAuth class, 
# which is used to handle HTTP Basic Authentication.
from requests.auth import HTTPBasicAuth

#Sends a GET request to the URL requiring basic authentication, 
# using the username "user" and password "pass".
response = requests.get("https://httpbin.org/basic-auth/user/pass",
                        auth=HTTPBasicAuth("user", "pass"))

#Prints the JSON response from the server, 
# which shows authentication status.
print (response.json())


