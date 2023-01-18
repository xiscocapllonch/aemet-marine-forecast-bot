import json
from pathlib import Path

from utils import _translate_date, _get_warning, _get_situation, _get_forecast, _get_trend, format_coastal_forecast

absolute_path = Path(__file__).parent.resolve()

with open(f'{absolute_path}/test_assets/coastal_response_sample.json') as sample_data:
    data = json.load(sample_data)

with open(f'{absolute_path}/test_assets/expected_sample.txt') as expected_text:
    expected_output = expected_text.read()


def test_translate_date():
    output_date = _translate_date('2022-11-21T20:00:00')
    assert output_date == 'lunes, 21 de noviembre del 2022 a las 20:00'


def test_get_warning():
    response = _get_warning(data[0])
    expected_warning = expected_output[0:175]
    assert response == expected_warning


def test_get_situation():
    response = _get_situation(data[0])
    expected_situation = expected_output[175:605]
    assert response == expected_situation


def test_get_forecast():
    response = _get_forecast(data[0])
    expected_forecast = expected_output[605:2951]
    assert response == expected_forecast


def test_get_trend():
    response = _get_trend(data[0])
    expected_forecast = expected_output[2951:3326]
    assert response == expected_forecast


def test_format_coastal_forecast():
    forecast = format_coastal_forecast(data)
    assert forecast == expected_output
