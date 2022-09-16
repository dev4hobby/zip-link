import json
import re
from random import choice
from string import ascii_letters, digits
from urllib import parse

API_SERVER_URL = "https://a.z1p.link"

STRING_SET = list(ascii_letters + digits)
# Random string generator, limit 6
def generate_random_string(string_set: str, length=6) -> str:
    return "".join(choice(string_set) for i in range(length))


def remove_http_prefix(url: str) -> str:
    url = re.sub(r"^https?://", "", url)
    return url


def sanitize_url(url) -> str:
    url = parse.unquote(url.strip())
    url = parse.unquote(url.strip())
    url = remove_http_prefix(url)
    return url


def json_response(
    body,
    status_code=200,
    headers={
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    },
) -> dict:
    return {
        "headers": headers,
        "statusCode": status_code,
        "body": json.dumps(body),
    }


def update_headers(headers: dict, response: dict) -> dict:
    if response.get("headers"):
        if headers:
            response["headers"].update(headers)
    else:
        response["headers"] = headers
    return response
