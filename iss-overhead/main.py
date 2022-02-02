import requests
from datetime import datetime
import smtplib

MY_LAT = 38.423733 # Your latitude
MY_LONG = 27.142826 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

if -5 < (MY_LAT - iss_latitude) < 5 or -5 < (MY_LONG - iss_longitude) < 5:

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

    #If the ISS is close to my current position ✅
    # and it is currently dark
    if time_now > sunset:
        
        EMAIL = 'tolearnpython13@gmail.com'
        PASSWORD = 'Py.12345'
            
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(EMAIL, PASSWORD)
        print('logged in')
        server.sendmail(
                            from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f'Subject:ISS Notification\n\nLook up! ISS Overhead!'
        )



