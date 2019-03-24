#!/bin/bash

while true; do
	./wifi_scanner.py &
	export scanner_pid=$!
	./pimotion.py &
	export camera_pid=$!
	./piaudio.py > /dev/null 2>&1 &
	export audio_pid=$!

	sleep 60
	kill $scanner_pid
	kill $camera_pid
	kill $audio_pid
	echo("time up")

	./renaming.py

	scp ~/RPi/dated/*.h264 user@laptop:~/dated/ > /dev/null 2>&1
	scp ~/Documents/* user@laptop:~/documents/ > /dev/null 2>&1
	scp ~/RPi/audio/*.wav user@laptop:~/audio/ > /dev/null 2>&1

	rm -rf ~/RPi/h264/*
	rm -rf ~/RPi/dated/*
	rm -rf ~/Documents/*
	rm -rf ~/RPi/audio/*

done
