import requests
import configuration
import data

def post_new_user (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user (data.user_body)
print(response.status_code)

response_json = response.json()
auth_token = response_json["authToken"]
print(f"Token obtenido: {auth_token}")

def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )