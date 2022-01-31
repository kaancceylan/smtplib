import smtplib
import datetime as dt
import random

EMAIL = 'tolearnpython13@gmail.com'
PASSWORD = 'Py.12345'

now = dt.datetime.now()
day = now.weekday()

if day == 0: #If it's Monday
    with open('quotes.txt', 'r') as f:
        quotes = f.readlines()
        quote = random.choice(quotes)

    
    #with smtplib.SMTP('smtp.gmail.com') as connection:
        #connection.starttls() #For a safe connection
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(EMAIL, PASSWORD)
    print('logged in')
    server.sendmail(
                        from_addr=EMAIL,
                        to_addrs=EMAIL,
                        msg=f'Subject:Motivational Quote\n\n{quote}'
    )