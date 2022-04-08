import requests

test_file = open("test_upload.txt", "rb")
test_url = "http://localhost:8000/upload/"

test_response = requests.post(test_url, files = {"file_uploaded": test_file})
print(test_response.json())
