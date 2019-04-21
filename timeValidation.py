import subprocess
import datetime
import time

subprocess.call(['gphoto2','--auto-detect'])
subprocess.call(['gphoto2','--list-files'])
time.sleep(2)

status = ''

while True:
    
    currentTime = datetime.datetime.now()

    todayBeginingOfDay = currentTime.replace(hour=00, minute=35, second=00, microsecond=0)
    todayEndOfDay = currentTime.replace(hour=00, minute=37, second=30, microsecond=0)

    if currentTime < todayBeginingOfDay:
        status = 'Too Early'
        pass

    elif currentTime > todayEndOfDay:
        status = 'Too late'
        pass

    elif currentTime >= todayBeginingOfDay:
        status = 'Working time'
        # subprocess.call(['gphoto2','--capture-image'])


    print status, currentTime 
    time.sleep(30)

    # time.sleep(600)









# status = ''
# while True:

#   if currentTime < todayBeginingOfDay:
#     status = 'Too Early'
#     pass

#   elif currentTime > todayEndOfDay:
#     status = 'Too late'
#     pass

#   elif currentTime >= todayBeginingOfDay:
#     status = 'Working time'

#   print status, currentTime 
#   time.sleep(10)

