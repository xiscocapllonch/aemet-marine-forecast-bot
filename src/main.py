import os
import asyncio
import telegram

from dotenv import load_dotenv

from api_client import get_request
from config import API_CONFIG
from utils import format_coastal_forecast

load_dotenv()


async def main():
    telegram_token = os.getenv('TELEGRAM_TOKEN', '')
    coast_code = os.getenv('MAR_FORECAST_COASTAL_CODE', '')
    chat_id = os.getenv('MAR_FORECAST_COASTAL_CHAT_ID', '')
    bot = telegram.Bot(telegram_token)
    async with bot:
        coastal_config = API_CONFIG.get('ENDPOINTS').get('MARITIME_FORECAST').get('COASTAL')
        response = get_request(coastal_config.get('url') + coastal_config.get('coast_codes').get(coast_code))
        forecast_dict = response.get('data')
        forecast_text = format_coastal_forecast(forecast_dict)

        await bot.send_message(
            text=forecast_text,
            parse_mode='HTML',
            chat_id=chat_id
        )


if __name__ == '__main__':
    asyncio.run(main())
