import requests
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH


def post_new_user(user_body):
    return requests.post(f"{URL_SERVICE}{CREATE_USER_PATH}", json=user_body)


def post_new_client_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    return requests.post(f"{URL_SERVICE}{KITS_PATH}", json=kit_body, headers=headers)