from modules.utils import json_response
from services.get_url import get_id_by_param_name


def get_url(event, context):
    body, status_code = get_id_by_param_name(event, "queryStringParameters")
    return json_response(body, status_code)


def get_url_by_pathparam(event, context):
    body, status_code = get_id_by_param_name(event, "pathParameters")
    return json_response(body, status_code)


def set_url(event, context):
    return json_response({"message": "Not Implemented"})
