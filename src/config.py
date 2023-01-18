import os

from dotenv import load_dotenv

load_dotenv()


def get_api_key() -> str:
    api_key = os.getenv('AEMET_API_KEY', '')
    if not api_key:
        raise Exception('Please follow the README.md instructions to add a valid AEMET API KEY')
    else:
        return api_key


API_CONFIG = {
    'API_KEY': get_api_key(),
    'BASE_URL': 'https://opendata.aemet.es/opendata/api/',
    'ENDPOINTS': {
        'MARITIME_FORECAST': {
            'COASTAL': {
                'url': 'prediccion/maritima/costera/costa/',  # {coast_code}
                'coast_codes': {
                    'GALICIA': '40',
                    'ASTURIAS_CANTABRIA_PAIS_VASCO': '41',
                    'ANDALUCIA_OCCIDENTAL_CEUTA': '42',
                    'ISLAS_CANARIAS': '43',
                    'ILLES_BALEARS': '44',
                    'CATALUNYA': '45',
                    'VALENCIA_MURCIA': '46',
                    'ANDALUCIA_ORIENTAL_MELILLA': '47'
                }
            }
        }
    }
}
