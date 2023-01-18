from datetime import datetime
from babel import dates


def _translate_date(input_date: str) -> str:
    input_date_format = "%Y-%m-%dT%H:%M:%S"
    input_date = datetime.strptime(input_date, input_date_format)
    output_date_format = "EEEE, dd 'de' MMMM 'del' yyyy 'a las' HH:mm"
    return dates.format_datetime(input_date, format=output_date_format, locale='es')


def _format_heading_1(input_str: str) -> str:
    return f'<u><b>{input_str}</b></u>\n\n'


def _format_heading_2(input_str: str) -> str:
    return f'<b>{input_str}</b>\n\n'


def _format_heading_3(input_str: str) -> str:
    return f'• <b>{input_str}</b>'


def _get_warning(forecast: dict) -> str:
    warning = forecast.get('aviso')
    end_date = warning.get('fin')
    end_date_msg = _translate_date(end_date)
    heading_1 = _format_heading_1(f'Avisos válidos hasta el {end_date_msg} hora oficial')
    text = warning.get('texto')
    return heading_1 + text + '\n\n\n'


def _get_situation(forecast: dict) -> str:
    situation = forecast.get('situacion')
    heading_1 = _format_heading_1(situation.get('nombre'))
    start_date = f'Fecha de inicio: {_translate_date(situation.get("inicio"))} hora oficial\n'
    end_date = f'Fecha de fin: {_translate_date(situation.get("fin"))} hora oficial\n\n'
    text = situation.get('texto')
    return heading_1 + start_date + end_date + text + '\n\n\n'


def _get_zone(zone: dict) -> str:
    heading_2 = _format_heading_2(zone.get('nombre'))
    subzones_list = zone.get('subzona')

    if len(subzones_list) == 1:
        text = subzones_list[0].get('texto')
        return heading_2 + text + '\n\n'
    else:
        subzones_text = ''
        for subzone in subzones_list:
            subzone_name = _format_heading_3(subzone.get('nombre'))
            subzone_text = subzone.get('texto')
            subzones_text = subzones_text + subzone_name + ': ' + subzone_text + '\n\n'

        return heading_2 + subzones_text


def _get_forecast(forecast: dict) -> str:
    forecast = forecast.get('prediccion')
    heading_1 = _format_heading_1('Predicción')
    start_date = f'Fecha de inicio: {_translate_date(forecast.get("inicio"))} hora oficial\n'
    end_date = f'Fecha de fin: {_translate_date(forecast.get("fin"))} hora oficial\n\n'
    zone_list = forecast.get('zona')
    zones_forecast = ''.join([_get_zone(zone) for zone in zone_list])

    return heading_1 + start_date + end_date + zones_forecast + '\n'


def _get_trend(forecast: dict) -> str:
    trend = forecast.get('tendencia')
    heading_1 = _format_heading_1('Tendencia')
    start_date = f'Fecha de inicio: {_translate_date(trend.get("inicio"))} hora oficial\n'
    end_date = f'Fecha de fin: {_translate_date(trend.get("fin"))} hora oficial\n\n'
    text = trend.get('texto')

    return heading_1 + start_date + end_date + text + '\n\n\n'


def format_coastal_forecast(forecast_list: list) -> str:
    forecast_dict = forecast_list[0]
    warning = _get_warning(forecast_dict)
    situation = _get_situation(forecast_dict)
    forecast = _get_forecast(forecast_dict)
    trend = _get_trend(forecast_dict)
    return warning + situation + forecast + trend + '© AEMET\n'
