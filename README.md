# RPi
## What I have done:
### pimotion.py
This records video to a circular buffer, 10 seconds long, while simultaneously analysing the video to detect motion. When motion is detected video is recorded to a file in the folder h264 in h264 format.

### renaming.py
This loops through all the video files in h264, renames them to the date and time of their creation in the format '%Y_%m_%d_%H_%M_%S'. Finally it saves them into the dated folder.

### converting.py
This loops through all the video files in dated on the computer storing the video files and converts them into mp4 format. (Should be run on the computer)

### wifi_scanner.py
This simultaneously runs two processes:
- TShark. Captures a list of the MAC addresses of packets that it sniffs and records data in this order:
  Time of capture, Source MAC address, Frequency on which it was captured, Relative signal strength
- Channel hopping. Loops through channels 1-14 of the 2.4GHz frequency, needed so that TShark can capture all the devices around it not just the ones on a single channel.

### start_all.sh
Single script that:
- Launches pimotion.py and wifi_scanner.py
- Every set time period (eg 2 min, or 5 hours) it:
  - Kills the above programs
  - Runs renaming.py
  - Sends all h264 files and all wifi data files by scp to specified computer
  - Deletes all h264 videos, and deletes all wifi data files (to prevent using up all space on SD card)
  - Starts all over again

## Things I had to do to make it work:
I've been running this on [Kali for RPi](https://www.offensive-security.com/kali-linux-arm-images/) (choosing "Kali Linux RaspberryPi 2 and 3") because TShark seems to work slightly better on Kali. This means that a lot of the things I had to do will not be necessary on Raspbian as they come by default.

### To use the RPi camera and picamera module in python:
- Downloaded [Re4son-Pi-Kernel](https://re4son-kernel.com/re4son-pi-kernel/)
- Installed the following two python modules:
```python
  pip install picamera
  pip install numpy
```
- To the file /boot/config.txt, added these two lines:
  - start_x=1 <= camera is prepared during boot
  - gpu_mem=128 <= minimum GPU memory for the camera, a higher number can be set
- To the file /etc/modules, added this:
  - bcm2835-v4l2 <= the driver for the RPi camera
- Ran ```raspistill -v``` and rebooted

### To convert h264 into mp4
- Installed ffmpeg on computer/server which stores the video and data files:
```sudo apt-get install ffmpeg```

### To allow scp from the RPi to my laptop
- Enabled SSH without a password, from RPi to laptop:
```
ssh-keygen
ssh-copy-id user@laptop
```
- Edited settings on RPi and laptop so that they don't go to 'sleep'

### Ensuring that the USB dongle has a static name (even after reboot)
- Many of the useful files such as tc/udev/rules.d/70-persistent-net.rules or 75-persistent-net-generator.rules are missing, so the easiest way to get around this is to create the file /etc/udev/rules.d/76-netnames.rules, and add this line to it:
```
SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="us:bm:ac:ad:dr:ss", NAME="customname"
```
And then reboot the RPi.

## What I still need to do:
- Figure out why sometimes TSHark captures packets without a source MAC address. Why does this happen? Filter out all lines from wifi_data files that don't contain a MAC address
