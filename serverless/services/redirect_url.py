from modules import redis
from datetime import timedelta


def redirect_url_by_param(event, param_name):
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

    if not origin_url.startswith("http"):
        origin_url = "https://" + origin_url

    headers = {"Location": origin_url}

    body = {}

    return headers, body, 301
