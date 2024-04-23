import requests # requests 라이브러리 사용

url = 'http://127.0.0.1:8000/api/student_list'

response = requests.get(url)

print(response.text)