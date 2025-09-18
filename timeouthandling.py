import requests
try:
    response = requests.get("https://httpbin.org/delay/3"
                            , timeout=2)
    print(response.text)
except requests.exceptions.Timeout:
    print("Request timed out!")

