import copy
from data import kit_body, user_body, NAME_511_CHARS, NAME_512_CHARS
from sender_stand_request import post_new_user, post_new_client_kit


def get_new_user_token():
    response = post_new_user(user_body)
    assert response.status_code == 201
    return response.json()["authToken"]


def get_kit_body(name):
    new_body = copy.copy(kit_body)
    new_body["name"] = name
    return new_body


def positive_assert(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400


def test_name_min_length():
    token = get_new_user_token()
    body = get_kit_body("a")
    positive_assert(body, token)


def test_name_max_length_511():
    token = get_new_user_token()
    body = get_kit_body(NAME_511_CHARS)
    positive_assert(body, token)


def test_name_empty():
    token = get_new_user_token()
    body = get_kit_body("")
    negative_assert_code_400(body, token)


def test_name_too_long_512():
    token = get_new_user_token()
    body = get_kit_body(NAME_512_CHARS)
    negative_assert_code_400(body, token)


def test_name_special_characters():
    token = get_new_user_token()
    body = get_kit_body("№%@")
    positive_assert(body, token)


def test_name_with_spaces():
    token = get_new_user_token()
    body = get_kit_body(" A Aaa ")
    positive_assert(body, token)


def test_name_numbers():
    token = get_new_user_token()
    body = get_kit_body("123")
    positive_assert(body, token)


def test_name_field_missing():
    token = get_new_user_token()
    body = {}
    negative_assert_code_400(body, token)


def test_name_wrong_type():
    token = get_new_user_token()
    body = get_kit_body(123)
    negative_assert_code_400(body, token)