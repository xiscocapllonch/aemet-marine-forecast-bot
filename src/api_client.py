import requests

from config import API_CONFIG

API_ERRORS = {
    401: 'Unauthorized',
    404: 'Not Found',
    429: 'Too Many Requests'
}


def _get_request_json_data(url: str) -> dict:
    response = requests.get(url)
    json_response = response.json()
    return json_response


def get_request(url: str, headers: dict = None, params: dict = None) -> dict:
    headers = headers if headers else dict()
    params = params if params else dict()

    api_headers = {
        'api_key': API_CONFIG['API_KEY']
    }
    api_headers.update(headers)

    response = requests.get(
        API_CONFIG['BASE_URL'] + url,
        headers=api_headers,
        params=params,
    )

    if response.status_code == 200:
        response_dict = response.json()

        meta_data = _get_request_json_data(response_dict['metadatos'])
        data = _get_request_json_data(response_dict['datos'])

        return {
            'status_code': response.status_code,
            'description': response_dict['descripcion'],
            'data': data,
            'meta_data': meta_data
        }

    if response.status_code in API_ERRORS.keys():
        return {
            'status_code': response.status_code,
            'description': API_ERRORS[response.status_code]
        }

    else:
        return {
            'status_code': 500,
            'description': 'Unknown Error'
        }
