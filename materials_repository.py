import requests


def get_token(email: str, password: str) -> str:
    url: str = "https://auth.realtimelca.com/frontegg/identity/resources/auth/v1/user"
    headers: dict = {"frontegg-vendor-host": "auth.realtimelca"}
    data: dict = {"email": email, "password": password}

    response: requests.Response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        token: str = response.json().get("accessToken")
        if not token:
            raise Exception("No access token found in response")
        return token
    else:
        raise Exception(f"Request failed with status code {response.status_code}")


def make_request(url: str, token: str, params: dict = {}) -> requests.Response:
    return requests.get(
        url, headers={"Authorization": f"Bearer {token}"}, params=params
    )


if __name__ == "__main__":
    token = get_token("martinbernstorff@gmail.com", "DA-falk7vau")
    response = make_request(
        "https://api.realtimelca.com/epd/api/Material/Search",
        token,
        params={"search": "MBTest"},
    )
    pass
