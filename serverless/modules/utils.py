import json
from random import choice
from string import ascii_letters, digits

# Random string generator, limit 6
def generate_random_string(length=6):
    return "".join(choice(ascii_letters + digits) for i in range(length))


def json_response(body, status_code=200):
    return {
        "statusCode": status_code,
        "body": json.dumps(body),
    }
