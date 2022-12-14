import json
from modules import redis
from typing import Tuple
from urllib import parse
from datetime import timedelta
from modules.utils import (
    sanitize_url,
    generate_random_string,
    STRING_SET,
    API_SERVER_URL,
)


def set_id_by_param(event, param_name) -> Tuple[dict, int]:
    if not event.get(param_name):
        return ({"message": "Not Found"}, 404)

    body = json.loads(event[param_name])

    if not body.get("url"):
        return ({"message": "No url"}, 400)

    url = sanitize_url(body["url"])

    splited_url = [_ for _ in url.split("/") if _]
    head = "/".join(splited_url[:-1])
    tail = parse.quote(splited_url[-1])
    url = f"{head}/{tail}"

    short_id = redis.get(url)
    if short_id:
        redis.extend_expire(url, ttl=timedelta(days=7))
        return (
            {"message": "URL expire extended", "url": f"{API_SERVER_URL}/r/{short_id}"},
            200,
        )

    db_size = redis.dbsize()
    size_per_string_set = len(STRING_SET)
    random_string_size = 2
    new_short_id = generate_random_string(STRING_SET, random_string_size)
    while redis.get(new_short_id):
        if db_size >= size_per_string_set**random_string_size:
            random_string_size += 1
            continue
        new_short_id = generate_random_string(STRING_SET, random_string_size)
    redis.setex(url, new_short_id, ttl=timedelta(days=7))
    result = redis.setex(new_short_id, url, ttl=timedelta(days=7))

    body = {"message": "New url added", "url": f"{API_SERVER_URL}/r/{new_short_id}"}
    return (body, 200)
