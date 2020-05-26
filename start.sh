#!/bin/bash
until sudo python3 obstally.py; do
	echo "OBS TALLY has crashed Restarting"
	sleep 1
done
