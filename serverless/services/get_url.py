from modules import redis
from typing import Tuple
from datetime import timedelta


def get_id_by_param(event, param_name) -> Tuple[dict, int]:
    if not event.get(param_name):
        return ({"message": "Not Found"}, 404)
    if not event[param_name].get("id"):
        return ({"message": "Short ID Not Found"}, 404)

    short_id = event[param_name]["id"]
    origin_url = redis.get(short_id)

    if not origin_url:
        return ({"message": "No origin url"}, 404)

    redis.extend_expire(origin_url, ttl=timedelta(days=7))
    redis.extend_expire(short_id, ttl=timedelta(days=7))

    body = {
        "short_id": short_id,
        "origin_url": origin_url,
    }
    return (body, 200)
