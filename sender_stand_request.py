import requests
import configuration
import data


def post_new_user(user_body):
    full_url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    return requests.post(
        url=full_url,
        json=user_body,
        headers=data.headers,

    )
def get_users_table():
    full_url = configuration.URL_SERVICE + configuration.USERS_TABLE_PATH
    return requests.get(
        url=full_url,
        headers=data.headers,
    )
