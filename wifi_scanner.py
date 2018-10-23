from multiprocessing import Process
import os
import time


def start_tshark():
    os.system("sudo tshark -i wlan0 -T fields -e frame.time -e wlan.sa -e radiotap.channel.freq -e radiotap.dbm_antsignal > ~/Documents/$(date '+%Y_%m_%d_%H_%M_%S').txt")

def channel_hop():
    channels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    wait = 1
    i = 0
    while True:
        os.system('iw dev wlan0 set channel %d'%channels[i])
        i = (i+1)%len(channels)
        time.sleep(wait)

if __name__=='__main__':
    os.system('sudo ifconfig wlan0 down')
    os.system('sudo iwconfig wlan0 mode monitor')
    os.system('sudo ifconfig wlan0 up')
    p1 = Process(target=start_tshark)
    p1.start()
    p2 = Process(target=channel_hop)
    p2.start()
