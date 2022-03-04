'''
Write a Python program to print yesterday, today, tomorrow.
'''
import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(1)
tomorrow = today + datetime.timedelta(1)
print("yestarday:",yesterday)
print("today:",today)
print("tomorrow:",tomorrow)