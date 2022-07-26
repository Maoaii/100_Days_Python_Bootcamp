import requests
from datetime import datetime
import smtplib
import time

MY_DATA = {
    "email": "abcd@gmail.com",
    "password": "abcdefg"
}

MY_LAT = 38.664242  # Your latitude
MY_LONG = -9.076660  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if iss_latitude >= MY_LAT - 5 or iss_latitude <= MY_LAT + 5 and iss_longitude >= MY_LONG - 5 or iss_longitude <= MY_LONG + 5:
        return True


def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset <= time_now <= sunrise:
        return True


if is_iss_overhead() and is_night_time():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_DATA["email"], MY_DATA["password"])
    connection.sendmail(
        from_addr=MY_DATA["email"],
        to_addrs=MY_DATA["email"],
        msg="Subject:Look up!\n\nThe ISS is above you right now!"
    )
