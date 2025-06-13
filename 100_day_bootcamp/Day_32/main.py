from enum import Enum
from datetime import *
import random
import smtplib

email = "pierstheprogrammer@gmail.com"
password = "fkkf blby pieq nbra"

class Day_of_week(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

todays_date = datetime.now()
if (todays_date.weekday() == Day_of_week.Friday.value):
    with open("Day_32/quotes.txt") as file:
        quotes_list = file.read().split("\n")
        quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            email, 
            "piers.taylorr@gmail.com", 
            msg=f"Subject:{Day_of_week.Friday.name} Motivation\n\n{quote}".encode("utf-8")
        )