from modules import redis
from datetime import timedelta


def go_to_zip_by_param(event, param_name):
    headers = {"Location": "https://my.z1p.link"}
    body = {}
    return headers, body, 301
