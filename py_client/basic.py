import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint)  # ->application programming interface (API)
print(get_response.text)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON

{
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.28.1",
    "X-Amzn-Trace-Id": "Root=1-63479eb7-582cc9d12b46552d2f5b3227"
  },
  "json": null,
  "method": "GET",
  "origin": "125.160.102.154",
  "url": "https://httpbin.org/anything"
}
