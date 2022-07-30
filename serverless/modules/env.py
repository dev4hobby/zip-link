import json
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
            # get env from json file
            secrets = json.load(json_file)
            for key, value in secrets.items():
                if getenv(key) is None:
                    # set env from json file
                    environ[key] = str(value)
    except FileNotFoundError:
        return None


init_json_env()

REDIS_CONFIG = {
    "host": getenv("REDIS_HOST"),
    "port": getenv("REDIS_PORT"),
    "user": getenv("REDIS_USER"),
    "password": getenv("REDIS_PASSWORD"),
}
