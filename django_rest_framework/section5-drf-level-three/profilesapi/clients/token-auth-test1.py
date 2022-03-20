import requests


def client():
    # 토큰 발급
    # credentials = {"username": "admin", "password": "admin"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    # 토큰 미 전달 시 서버 응답 확인하기
    # response = requests.get("http://127.0.0.1:8000/api/profiles/")
    # 결과 - Status Code : 403
    # 결과 - {'detail': 'Authentication credentials were not provided.'}

    # 토큰 전달 시 서버 응답 확인하기
    headers = {"Authorization": "Token cf12b6bba6311e50144a9868d5dd1aeac0708143"}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
    # 결과 - Status Code : 200 결과 - [{'id': 1, 'user': 'admin', 'avatar':
    # 'http://127.0.0.1:8000/media/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3
    # %E1%86%BA_2022-02-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_1.41.32_QnrV8ei.png', 'bio': 'Site
    # Administrator', 'city': 'Testland2'}, {'id': 2, 'user': 'random', 'avatar': None, 'bio': '', 'city': ''}]

    print(f"Status Code : {response.status_code}")
    print(response.json())


if __name__ == "__main__":
    client()