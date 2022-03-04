'''
Write a Python program to calculate two date difference in seconds.
'''
import datetime
today = datetime.datetime.now()
random_date = today -  datetime.timedelta(days = 204, seconds = 124142, microseconds = 7)
seconds = (today - random_date).seconds
print(seconds)