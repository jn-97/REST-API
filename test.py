import requests # requests 라이브러리 사용

url = 'http://127.0.0.1:8000/api/auth'

response = requests.post(url, data = {'username': 'admin', 'password': '1234'})

print(response.text)

myToken = response.text

header = {'Authorization': 'Token e92eb884fa41054404bbf721a1b1f6baf8ea961d'}
response = requests.get('http://127.0.0.1:8000/api/student_list', headers=header)
print(response.text)