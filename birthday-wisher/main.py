
#Check if today matches a birthday in the birthdays.csv
# today = (today_month, today_day)
import datetime as dt
from unicodedata import name
import pandas as pd
import random
import smtplib

EMAIL = 'tolearnpython13@gmail.com'
PASSWORD = 'Py.12345'

date = dt.datetime.today()
today = (date.month, date.day)

birthday_msgs = pd.read_csv('birthdays.csv')

# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
birthdays_dict = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in birthday_msgs.iterrows()}


#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela ,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

# if (today_month, today_day) in birthdays_dict:
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
#If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path, 'r') as file:
        message = file.read()
        message = message.replace("[NAME]", birthday_person["name"])

#Send the letter generated in step 3 to that person's email address.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(EMAIL, PASSWORD)
    server.sendmail(
                        from_addr=EMAIL,
                        to_addrs=EMAIL,
                        msg=f'Subject:Happy Birthday\n\n{message}'
    )
