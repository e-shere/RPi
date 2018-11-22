import os
import time
import subprocess
import signal

while True:
    cmd1 = 'python ~/RPi/wifi_scanner.py'
    p1 = subprocess.Popen(cmd1, shell=True,preexec_fn=os.setsid)

    cmd2 = 'python ~/RPi/pimotion.py'
    p2 = subprocess.Popen(cmd2, shell=True,preexec_fn=os.setsid)

    time.sleep(60) # collect data over 1 minute - the time period can be varied
    os.killpg(os.getpgid(p1.pid),signal.SIGTERM)
    os.killpg(os.getpgid(p2.pid),signal.SIGTERM)
    p1.wait()
    p2.wait()
    print('time up')
    os.system('python ~/RPi/renaming.py')
    os.system('scp ~/RPi/mp4/*.mp4 user@laptop:~/videos/ > /dev/null 2>&1')
    os.system('scp ~/Documents/* user@laptop:~/documents/ > /dev/null 2>&1')
    os.system('rm -rf ~/RPi/h264/*')
    os.system('rm -rf ~/RPi/mp4/*')
    os.system('rm -rf ~/Documents/*')




