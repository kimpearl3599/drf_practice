# 1주차
# immutable, mutable?

# immutable : str, tuple
# mutable : num, list, dict

# postman 을 사용해서 장고에 쿼리 날려보기
# 장고에서 원하는 값 response 해주기

import requests

url = "http://127.0.0.1:8000/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
