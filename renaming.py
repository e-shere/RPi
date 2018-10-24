import os
for filename in os.listdir('/root/RPi/h264/'):
    date = os.popen('date -r "/root/RPi/h264/'+filename+'" "+%Y_%m_%d_%H_%M_%S"').read().strip("\n")
    os.system("ffmpeg -r 30 -y -i /root/RPi/h264/"+filename+" -c copy /root/RPi/mp4/"+date+".mp4 > /dev/null 2>&1")


