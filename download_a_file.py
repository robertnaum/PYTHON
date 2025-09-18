import requests

url = "https://httpbin.org/image/png"
response = requests.get(url)
with open("download.png", "wb") as f:
    f.write(response.content)
print("File downloaded as download.png")
