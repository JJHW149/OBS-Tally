import sys
import time
import board
import neopixel

import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, events

#EDIT Section
host = "192.168.0.91"
port = 4444
password = "secret"
numLED = 8
targetScene = "Camera 1"
#End of Edit

pixels = neopixel.NeoPixel(board.D18, numLED)


def production(message):
	if message.getSceneName().find(targetScene) != -1:
		pixels.fill((255,0,0))
	else:
		pixels.fill((0,0,0))

def preview(message):
	if message.getSceneName() == targetScene:
                pixels.fill((0,255,0))
	else:
		pixels.fill((0,0,0))


ws = obsws(host, port, password)
ws.register(production, events.SwitchScenes)
#ws.register(preview, events.PreviewSceneChanged)
ws.connect()
pixels.fill((0,0,100))
while True:
	time.sleep(0.001)

