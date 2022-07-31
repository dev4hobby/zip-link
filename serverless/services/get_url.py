from modules import redis
from typing import Tuple


def get_id_by_param_name(event, param_name) -> Tuple[dict, int]:
    if not event.get(param_name):
        return ({"message": "Not Found"}, 404)
    if not event[param_name].get("id"):
        return ({"message": "Short ID Not Found"}, 404)

    short_id = event[param_name]["id"]
    origin_url = redis.get(short_id)

    if not origin_url:
        return ({"message": "No origin url"}, 404)

    body = {
        "short_id": short_id,
        "origin_url": origin_url,
    }
    return (body, 200)
