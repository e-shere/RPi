import os
for filename in os.listdir('/root/RPi/h264/'):
    date = os.popen('date -r "/root/RPi/h264/'+filename+'" "+%Y_%m_%d_%H_%M_%S"').read().strip("\n")
    os.system("cp /root/RPi/h264/"+filename+" /root/RPi/dated/"+date+".h264")


