from modules.utils import json_response, update_headers
from services.get_url import get_id_by_param
from services.set_url import set_id_by_param
from services.redirect_url import redirect_url_by_param


def get_url(event, context):
    body, status_code = get_id_by_param(event, "queryStringParameters")
    return json_response(body, status_code)


def get_url_by_pathparam(event, context):
    body, status_code = get_id_by_param(event, "pathParameters")
    return json_response(body, status_code)


def set_url(event, context):
    body, status_code = set_id_by_param(event, "body")
    return json_response(body, status_code)


def redirect_url(event, context):
    header, body, status_code = redirect_url_by_param(event, "pathParameters")
    response = update_headers(header, json_response(body, status_code))
    return response
