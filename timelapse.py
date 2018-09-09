import subprocess
import time

subprocess.call(['gphoto2','--auto-detect'])
subprocess.call(['gphoto2','--list-files'])
time.sleep(2)

while True:
	subprocess.call(['gphoto2','--capture-image'])
	time.sleep(600)

