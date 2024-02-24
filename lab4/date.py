#ex1 
from datetime import datetime, timedelta
currentd = datetime.now()
newd = currentd - timedelta(days = 5)

print("The current date:", currentd)
print("Date after minus five days:", newd)

#ex2
from datetime import datetime, timedelta

current_data = datetime.now()
date_yesterday = current_data - timedelta(days = 1)
date_tomorrow = current_data + timedelta(days = 1)

print("The current data:", current_data)
print("Yesterday:", date_yesterday)
print("Tomorrow:", date_tomorrow)

#ex3
from datetime import datetime

current_data = datetime.now()
new_data = current_data.replace(microsecond = 0)

print(current_data)
print(new_data)

#ex4
from datetime import datetime

current_data = datetime.now()
my_data = datetime(2024, 8, 11, 15, 1, 0)
difference_sec = (current_data - my_data).total_seconds()

print(difference_sec)