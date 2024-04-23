import requests # requests 라이브러리 사용

url = 'http://127.0.0.1:8000/api/auth/'

response = requests.post(url, data = {'username': 'admin', 'password': '1234'})

print(response.text)

myToken = response.text