# AEMET MARINE FORECAST BOT

Repository to get [©AEMET](https://www.aemet.es/en/eltiempo/prediccion/maritima?opc1=0&opc2=martot&opc3=1&area=bal1)
weather predictions and publish them on telegram channels
(E.g. [Balearic Islands Channel](https://web.telegram.org/z/#-1412714734)). Why? To be able to access this information
in areas of low or sporadic mobile coverage.

## INSTALL

```bash
pipenv install
```

## TEST

```bash
pipenv run pytest .
```

## RUN

You must create a file called `.env` in the root folder with this environment vars or set those vars when you call the
script:

```dotenv
AEMET_API_KEY=54653MY.Aemet.455845API.key
TELEGRAM_TOKEN=6352785479:MyTelegram-TOken
MAR_FORECAST_COASTAL_CHAT_ID=-10054478265423
MAR_FORECAST_COASTAL_CODE=ILLES_BALEARS
```

#### AEMET_API_KEY

The API REST developed by AEMET needs an api key. You can request it here:
[https://opendata.aemet.es/centrodedescargas/altaUsuario](https://opendata.aemet.es/centrodedescargas/altaUsuario)

#### TELEGRAM_TOKEN

You will need a token for the telegram bot that writes the messages. Learn more about it here:
[https://core.telegram.org/bots/api#authorizing-your-bot](https://core.telegram.org/bots/api#authorizing-your-bot)

#### MAR_FORECAST_COASTAL_CHAT_ID

The telegram channel where the messages will be published and in which your bot must have admin write permissions, has
an id similar to ```-10054478265423```.

#### MAR_FORECAST_COASTAL_CODE

You can see the available ```coast_codes``` in the following configuration file:
[src/config.py](src/config.py)

```bash
pipenv run python  src/main.py
```