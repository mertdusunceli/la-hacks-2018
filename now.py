import datetime 

now = datetime.datetime.now()
hour = now.hour
minute = now.minute
stringtime = str(hour) + str(minute)
print(stringtime)