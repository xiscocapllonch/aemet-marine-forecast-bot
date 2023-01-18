import pytest

from api_client import get_request
from config import API_CONFIG


def test_get_request(requests_mock):
    status_code = 200

    description = 'test_description'

    metadata_test_url = 'https://test.com/metadata/item'
    metadata_test_response = {'format': 'json'}

    data_test_url = 'https://test.com/data/item'
    data_test_response = {'data': 'too cloudy'}

    aemet_request_response = {
        'descripcion': description,
        'metadatos': metadata_test_url,
        'datos': data_test_url,
    }

    url_sample = 'test-url/foo'
    requests_mock.get(
        API_CONFIG['BASE_URL'] + url_sample,
        status_code=status_code,
        json=aemet_request_response
    )

    requests_mock.get(
        metadata_test_url,
        json=metadata_test_response
    )

    requests_mock.get(
        data_test_url,
        json=data_test_response
    )

    response = get_request(url_sample)

    assert response == {
        'status_code': status_code,
        'description': description,
        'data': data_test_response,
        'meta_data': metadata_test_response
    }


@pytest.mark.parametrize(
    'status_code,description',
    [
        (401, 'Unauthorized'),
        (404, 'Not Found'),
        (429, 'Too Many Requests'),
        (500, 'Unknown Error')
    ]
)
def test_get_request_errors(requests_mock, status_code, description):
    url_sample = 'test-url/foo'
    requests_mock.get(API_CONFIG['BASE_URL'] + url_sample, status_code=status_code)
    response = get_request(url_sample)

    assert response == {
        'status_code': status_code,
        'description': description
    }
