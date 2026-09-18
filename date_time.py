import datetime

today = datetime.date.today()
print("Today's date:", today)

now = datetime.datetime.now()
date_string = now.strftime("%A, %B %d, %Y")

print("Today's date:", date_string)