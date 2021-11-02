import requests
from credential import EXCHANGERATESAPI_ACCESSKEY
# from django_rest_framework.credential import EXCHANGERATESAPI_ACCESSKEY


def main():
    response = requests.get(f"http://api.exchangeratesapi.io/latest?access_key={EXCHANGERATESAPI_ACCESSKEY}")

    if response.status_code != 200:
        print("Status code : ", response.status_code)
        raise Exception("There was an error!")

    data = response.json()
    print("JSON data : ", data)


if __name__ == "__main__":
    main()