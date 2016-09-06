import datetime
import random

# generates random codes function
def codigo(caracteres):
    today = datetime.date.today()
    year = today.year
    day = today.day
    month = today.month

    code = (str(year) + str(month) + str(day)) + "".join(random.choice(caracteres) for i in range(4))
    return code
