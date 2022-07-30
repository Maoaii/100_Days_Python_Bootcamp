# Automated with PythonAnywhere
import requests
import os
from twilio.rest import Client

# Open Weather API
api_key = os.environ.get("OWM_API_KEY")
OMW_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# Twilio API
twilio_sid = "AC27e7ac6c4c4cf53c623fa5de6e4a0d35"
twilio_auth_token = os.environ.get("TWLLIO_AUTH_TOKEN")
twilio_phone_number = "+18042584302"


weather_parameters = {
    "lat": 38.722252,
    "lon": -9.139337,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# Get weather info
response = requests.get(OMW_endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

# 12 hours weather data
hourly_weather_data = weather_data["hourly"][:11]

will_rain = False
for hour in hourly_weather_data:
    weather_condition_code = hour["weather"][0]["id"]
    if weather_condition_code < 700:
        will_rain = True

# Send SMS if it's going to rain
if will_rain:
    client = Client(twilio_sid, twilio_auth_token)

    message = client.messages.create(
        body="Bring an ☔️",
        from_=twilio_phone_number,
        to="+351960364668",
    )

    print(message.status)
