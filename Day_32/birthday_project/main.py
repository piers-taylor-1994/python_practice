import pandas
from datetime import *
import random
import smtplib
PATH = "Day_32/birthday_project"
EMAIL = "pierstheprogrammer@gmail.com"
PASSWORD = "fkkf blby pieq nbra"

#---------------ALTERNATIVE -----------------#
# todays_date = datetime.now()
# today_tuple = (todays_date.month, todays_date.day)
# with open(f"{PATH}/birthdays.csv") as file:
#     birthdays = pandas.read_csv(file)
#     birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in birthdays.iterrows()}
#     if today_tuple in birthdays_dict:
#         birthday = birthdays_dict[today_tuple]
#         with open(f"{PATH}/letter_templates/letter_{random.randint(1, 3)}.txt") as file:
#             letter_text = file.read()
#             letter_text = letter_text.replace("[NAME]", birthday["name"])
#         with smtplib.SMTP("smtp.gmail.com") as connection:
#             connection.starttls()
#             connection.login(EMAIL, PASSWORD)
#             connection.sendmail(
#                 EMAIL, 
#                 "piers.taylorr@gmail.com", 
#                 msg=f"Subject:Happy Birthday!\n\n{letter_text}".encode("utf-8")
#             )
#     else:
#         print("No birthdays today")

#---------------My solution -----------------#
todays_date = datetime.now()
with open(f"{PATH}/birthdays.csv") as file:
    birthdays = pandas.read_csv(file)
    birthday = birthdays[(birthdays['month'] == todays_date.month) & (birthdays["day"] == todays_date.day)]
    if len(birthday) > 0:
        with open(f"{PATH}/letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            letter_text = file.read()
            letter_text = letter_text.replace("[NAME]", birthday.name.item())
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                EMAIL, 
                "piers.taylorr@gmail.com", 
                msg=f"Subject:Happy Birthday!\n\n{letter_text}".encode("utf-8")
            )
    else:
        print("No birthdays today")
