'''
Write a Python program to subtract five days from current date.
'''
import datetime

date = datetime.datetime.now()
renewdate = date - datetime.timedelta(5)
print(renewdate)