import json

import requests
from pdf_to_lca_materials.rlca_client.material import Material


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


def create_material(token: str, material: Material) -> requests.Response:
    # payload = json.loads(material.model_dump_json())
    test_payload = json.loads("""{
    "tenantId": "30f95646-f60f-4773-ab08-b64d5a60ba5e",
    "isPublic": false,
    "isCustom": true,
    "expectedLifespan": 60,
    "name": "MBAutoTest",
    "description": "Here's a description created by the API",
    "lciaResults": [
        {
            "moduleStatusEnum": 2,
            "moduleTypeEnum": 0,
            "indicators": [
                {
                    "type": "0",
                    "unit": "kg CO₂ eq.",
                    "value": 10
                }
            ]
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 1,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 2,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 3,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 4,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 5,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 6,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 7,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 8,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 9,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 10,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 11,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 12,
            "indicators": []
        },
        {
            "moduleStatusEnum": 2,
            "moduleTypeEnum": 13,
            "indicators": [
                {
                    "type": "0",
                    "unit": "kg CO₂ eq.",
                    "value": 10
                }
            ]
        },
        {
            "moduleStatusEnum": 2,
            "moduleTypeEnum": 14,
            "indicators": [
                {
                    "type": "0",
                    "unit": "kg CO₂ eq.",
                    "value": 1
                }
            ]
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 15,
            "indicators": []
        },
        {
            "moduleStatusEnum": 0,
            "moduleTypeEnum": 16,
            "indicators": []
        },
        {
            "moduleStatusEnum": 2,
            "moduleTypeEnum": 17,
            "indicators": [
                {
                    "type": "0",
                    "unit": "kg CO₂ eq.",
                    "value": 41
                }
            ]
        }
    ],
    "declaredUnit": {
        "declaredUnit": 4,
        "declaredValue": 1,
        "mass": 1,
        "massUnit": 1
    },
    "epdInfo": {
        "epdSpecificationForm": 0,
        "epdProductIndustryType": 1,
        "publicationDate": "2023-05-23",
        "validTo": "2027-05-23",
        "declarationOwnerId": "cbc10878-85b1-4190-a523-e47b25a6a86d",
        "sourceEpdUrl": "www.realtimelca.com",
        "dataSourceId": "cf1bca75-0e00-40f1-8666-a72e6b501e09",
        "fileEntityId": "",
        "epdVersion": "1",
        "declarationNumber": "1212-232132"
    },
    "tags": [
        "Belysning"
    ]
}""")

    response = make_request(
        url="https://api.realtimelca.com/epd/api/material/create",
        token=token,
        params=test_payload,
    )
    return response


if __name__ == "__main__":
    token = get_token("EMAIL", "PASSWORD")
    response = create_material(token)
