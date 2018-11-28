from multiprocessing import Process
import os
import time

wlan_name = "mywifi"
def start_tshark():
    os.system('sudo ifconfig '+wlan_name+' down')
    os.system('sudo iwconfig '+wlan_name+' mode monitor')
    os.system('sudo ifconfig '+wlan_name+' up')
    os.system("sudo tshark -i "+wlan_name+" -T fields -e frame.time -e wlan.sa -e radiotap.channel.freq -e radiotap.dbm_antsignal > ~/Documents/$(date '+%Y_%m_%d_%H_%M_%S').txt > /dev/null 2>&1")

def channel_hop():
    channels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    wait = 1
    i = 0
    while True:
        os.system('iw dev '+wlan_name+' set channel %d'%channels[i])
        i = (i+1)%len(channels)
        time.sleep(wait)

if __name__=='__main__':
    p1 = Process(target=start_tshark)
    p1.start()
    p2 = Process(target=channel_hop)
    p2.start()
    while True:
        if p1.is_alive() == False:
            p1.terminate()
            time.sleep(0.1)
            p1 = Process(target=start_tshark)
            p1.start()
        if p2.is_alive() == False:
            p2.terminate()
            time.sleep(0.1)
            p2 = Process(target=channel_hop)
            p2.start()
