from modules import redis
from datetime import timedelta
from modules.utils import quote_url


def redirect_url_by_param(event, param_name):
    if not event.get(param_name):
        return ({"message": "Not Found"}, 404)
    if not event[param_name].get("id"):
        return ({"message": "Short ID Not Found"}, 404)

    short_id = event[param_name]["id"]
    unquoted_url = redis.get(short_id)

    if not unquoted_url:
        return ({"message": "No origin url"}, 404)

    redis.extend_expire(unquoted_url, ttl=timedelta(days=7))
    redis.extend_expire(short_id, ttl=timedelta(days=7))

    last_slash_index = unquoted_url.rfind('/')
    last_info = unquoted_url[last_slash_index + 1:]
    url = '/'.join([unquoted_url[:last_slash_index],quote_url(last_info)])
    headers = {"Location": url}
    body = {}

    return headers, body, 301
