import json
import re
from random import choice
from string import ascii_letters, digits

# Random string generator, limit 6
def generate_random_string(length=6):
    return "".join(choice(ascii_letters + digits) for i in range(length))


def validate_url_with_regex(url):
    if not url:
        return False
    return re.match(
        r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",
        url,
    )


def json_response(body, status_code=200):
    return {
        "statusCode": status_code,
        "body": json.dumps(body),
    }
