import requests

print(requests.__version__)

google_resp = requests.get("http://google.com/")
print(google_resp.text)

my_resp = requests.get("https://raw.githubusercontent.com/zihan001/lab1-CMPUT404/main/versionfinder.py")
print(my_resp.text)