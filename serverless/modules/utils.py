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


def validate_url_with_regex(url) -> bool:
    if not url:
        return False
    return re.match(
        r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",
        url,
    )


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

def quote_url(url: str) -> str:
    return parse.quote(url.strip())

def unquote_url(quoted_url: str) -> str:
    return parse.unquote(quoted_url)