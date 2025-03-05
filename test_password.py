import requests
import passwords
URL = "http://httpbin.org/basic-auth/russ/test"

response = requests.get(URL, auth=(passwords.TEST_USER, passwords.TEST_PASS))
print(response.text)
