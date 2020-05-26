OBS Tally for raspberry pi: 
  
Runs with OBS Websocket:  
https://github.com/Palakis/obs-websocket/releases

Requires user: pi  
#Can be changed in the tally.service file  

Wiring:  
RPi     -> NeoPixel  
5v      -> 4 - 7VDC  
Gnd     -> Gnd  
GPIO 18 -> Data In  

Install:  
Clone files in to pi home directory  

Setup Adafruit Neopixel Support raspberry pi:  
  https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring  
  sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel  

Setup obs-websocket-python libary:  
  https://github.com/Elektordi/obs-websocket-py  
  sudo pip3 install obs-websocket-py  

In obstally.py change information in edit section to match your setup  
  #EDIT Section  
  host = "192.168.0.91"  
  port = 4444  
  password = "secret"  
  numLED = 8  
  targetScene = "Camera 1"  
  #End of Edit  

Move service to system services:  
  sudo cp tally.service /etc/systemd/system/tally.service  

Then enable the service:  
  sudo systemctl enable tally  
  
To check status:  
  systemctl status tally  
