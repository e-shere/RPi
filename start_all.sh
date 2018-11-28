!/bin/bash

while true; do
	python ~/RPi/wifi_scanner.py &
	export scanner_pid=$!
	python ~/RPi/pimotion.py &
	export camera_pid=$!

	sleep 60
	kill $scanner_pid
	kill $camera_pid
	echo("time up")

	python ~/RPi/renaming.py

	scp ~/RPi/dated/*.h264 user@laptop:~/dated/ > /dev/null 2>&1
	scp ~/Documents/* user@laptop:~/documents/ > /dev/null 2>&1

	rm -rf ~/RPi/h264/*
	rm -rf ~/RPi/dated/*
	rm -rf ~/Documents/*

done
