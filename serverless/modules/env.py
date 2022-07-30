import json
from bson import json_util
import pipes
from os import getenv, environ, path


def init_json_env() -> None:
    """
    init env from json file
    if env not exist, pass it
    """
    try:
        secrets = path.join(path.dirname(path.dirname(__file__)), "config.json")
        with open(secrets, "r") as json_file:
            for k, v in json.load(json_file).items():
                k = pipes.quote(k)
                v = pipes.quote(v)
    except FileNotFoundError:
        return None

init_json_env()

REDIS = {
    'host': getenv("REDIS_HOST"),
    'port': getenv("REDIS_PORT"),
    'user': getenv("REDIS_USER"),
    'password': getenv("REDIS_PASSWORD"),
}