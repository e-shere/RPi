import os
for filename in os.listdir('/root/Videos/'):
    date = os.popen('date -r "/root/Videos/'+filename+'" "+%Y_%m_%d_%H_%M_%S"').read().strip("\n")
    os.system("ffmpeg -r 30 -i /root/Videos/"+filename+" -c copy /root/Videos/"+date+".mp4")


