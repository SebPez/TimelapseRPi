import subprocess
import datetime
import time

subprocess.call(['gphoto2','--auto-detect'])
subprocess.call(['gphoto2','--list-files'])
time.sleep(2)

status = ''

while True:
    
    currentTime = datetime.datetime.now()

    todayBeginingOfDay = currentTime.replace(hour=07, minute=00, second=00, microsecond=0)
    todayEndOfDay = currentTime.replace(hour=18, minute=00, second=00, microsecond=0)
    
    if currentTime < todayBeginingOfDay:
        status = 'Too Early'
        pass

    elif currentTime > todayEndOfDay:
        status = 'Too late'
        pass

    elif currentTime >= todayBeginingOfDay:
        status = 'Working time'
        subprocess.call(['gphoto2','--capture-image'])


    print status, currentTime 
    time.sleep(300)
