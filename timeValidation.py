import datetime

currentTime = datetime.datetime.now()
# currentTime = datetime.datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)

todayBeginingOfDay = currentTime.replace(hour=7, minute=0, second=0, microsecond=0)
todayEndOfDay = currentTime.replace(hour=18, minute=0, second=0, microsecond=0)

status = ''

if currentTime < todayBeginingOfDay:
  status = 'Too Early'

elif currentTime > todayEndOfDay:
  status = 'Too late'

elif currentTime >= todayBeginingOfDay:
  status = 'Working time'

print status 

