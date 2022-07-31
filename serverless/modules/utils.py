import json
import re
from random import choice
from string import ascii_letters, digits

# Random string generator, limit 6
def generate_random_string(length=6) -> str:
    return "".join(choice(ascii_letters + digits) for i in range(length))


def validate_url_with_regex(url) -> bool:
    if not url:
        return False
    return re.match(
        r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",
        url,
    )


def json_response(body, status_code=200) -> dict:
    return {
        "statusCode": status_code,
        "body": json.dumps(body),
    }


def update_headers(headers: dict, response: dict) -> dict:
    if response.get("headers"):
        if headers:
            response.update("headers", headers)
    return response
