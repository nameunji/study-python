import requests

def client():
    # sign up
    # credentials = {
    #     "username": "resttest2",
    #     "password1": "changeme1234",
    #     "password2": "changeme1234",
    #     "email": "rest2@test.com",
    # }
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=credentials)

    # profile test
    headers = {"Authorization": "Token df251b3cdf084cbbb150dc440872494e5fcb0c0a"}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print(f"Status Code : {response.status_code}")
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()