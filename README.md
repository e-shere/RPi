# RPi
## What I have done:
### pimotion.py
This records video to a circular buffer, 10 seconds long, while simultaneously analysing the video to detect motion. When motion is detected video is recorded to a file in the folder h264 in h264 format.

### renaming.py
This loops through all the video files in h264, renames them to the date and time of their creation in the format '%Y_%m_%d_%H_%M_%S', and converts them into mp4 format. Finally it saves them into the mp4 folder.

### wifi_scanner.py
This simultaneously runs two processes:
- TShark. Captures a list of the MAC addresses of pacets that it sniffs and records data in this order:
  Time of capture, Source MAC address, Frequency on which it was captured, Relative signal strength
- Channel hopping. Loops through channels 1-14 of the 2.4GHz frequency, needed so that TShark can capture all the devices around it not just the ones on a single channel.

### start_all.py
Single script that:
- Launches pimotion.py and wifi_scanner.py
- Every set time period (eg 2 min, or 5 hours) it:
  - Kills the above programs
  - Runs renaming.py
  - Sends all mp4 files and all wifi data files by scp to specified computer
  - Deletes all h264 and mp4 videos, and deletes all wifi data files (to prevent using up all space on SD card)
  - Starts all over again

## Things I had to do to make it work:

## What I still need to do:

