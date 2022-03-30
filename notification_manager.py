import requests
import os
from twilio.rest import Client

class NotificationManager:
    # TWILIO_ACCOUNT_SID = "AC2ebf1800e3ef4d2e3211e227bc96e04b"
    # TWILIO_AUTH_TOKEN = "4ab07e79e03f068471cfef379e1f4586"
    # account_sid = os.environ[f'{TWILIO_ACCOUNT_SID}']
    # auth_token = os.environ[f'{TWILIO_AUTH_TOKEN}']


    account_sid = "AC2ebf1800e3ef4d2e3211e227bc96e04b"
    auth_token = "4ab07e79e03f068471cfef379e1f4586"

    OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
    api_key2 = os.getenv("OWM_API_KEY")
    api_key = "e70d8ff6f0aeabfbfad58d6fd57c8e43"

    print(api_key)
    print(api_key2)


    weather_params = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "exclude": "current,minutely,daily",
        "appid": api_key,
    }

    response = requests.get(OWM_Endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()

    rain = False
    for n in range(48):
        id_weather = weather_data["hourly"][n]["weather"][0]["id"]
        if id_weather < 700:
            rain = True

    if rain:
        message_text = "Bring an umbrella"
    else:
        message_text = "Leave an umbrella"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_text,
        from_='+19124933441',
        to='+79160585921',
    )
    print(message.status)

