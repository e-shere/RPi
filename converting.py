import os
for filename in os.listdir('~/dated/'):
    new_name = filename.split(".")[0]
    os.system("ffmpeg -r 30 -y -i ~/dated/"+filename+" -c copy ~/mp4/"+new_name+".mp4 > /dev/null 2>&1")


