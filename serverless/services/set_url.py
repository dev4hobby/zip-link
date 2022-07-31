
import json
from modules import redis
from typing import Tuple
from datetime import timedelta
from modules.utils import generate_random_string, validate_url_with_regex


def set_id_by_param(event, param_name) -> Tuple[dict, int]:
    if not event.get(param_name):
        return ({"message": "Not Found"}, 404)

    body = json.loads(event[param_name])

    if not body.get("url"):
        return ({"message": "No url"}, 400)

    url = body["url"]
    
    if not validate_url_with_regex(url):
        return ({"message": "Invalid url"}, 400)

    short_id = redis.get(url)
    if short_id:
        redis.extend_expire(url, ttl=timedelta(days=7))
        return (
            {"message": "URL expire extended", "url": url, "short_id": short_id},
            200,
        )

    new_short_id = generate_random_string()
    while redis.get(new_short_id):
        new_short_id = generate_random_string()
    redis.setex(url, new_short_id, ttl=timedelta(days=7))
    result = redis.setex(new_short_id, url, ttl=timedelta(days=7))

    body = {"url": f"https://z1p.link/r/{new_short_id}"}
    return (body, 200)
