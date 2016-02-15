from sense_hat import SenseHat
import time
import random
from picamera import PiCamera
from twython import Twython

#CONSUMER_KEY = 
#CONSUMER_SECRET = 
#ACCESS_KEY = 
#ACCESS_SECRET = in your code put the twitter codes here (without the comments).  I keep them elsewhere for safe keeping though ;)
from secretcodes import *

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

sense = SenseHat()

Y = [random.randint(50,255),random.randint(50,255),random.randint(50,255)]
N = [0,0,0]

happy = [
N,N,N,N,N,N,N,N,
N,Y,Y,N,N,Y,Y,N,
N,Y,Y,N,N,Y,Y,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,Y,N,N,N,N,Y,N,
N,Y,Y,Y,Y,Y,Y,N,
N,N,N,N,N,N,N,N
]

sad = [
N,N,N,N,N,N,N,N,
N,Y,Y,N,N,Y,Y,N,
N,Y,Y,N,N,Y,Y,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,Y,Y,Y,Y,Y,Y,N,
N,Y,N,N,N,N,Y,N,
N,N,N,N,N,N,N,N
]

laugh = [
N,N,N,N,N,N,N,N,
N,Y,Y,N,N,Y,Y,N,
N,Y,Y,N,N,Y,Y,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,Y,Y,Y,Y,Y,Y,N,
N,N,Y,Y,Y,Y,N,N,
N,N,N,N,N,N,N,N
]

meh = [
N,N,N,N,N,N,N,N,
N,Y,Y,N,N,Y,Y,N,
N,Y,Y,N,N,Y,Y,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,Y,Y,Y,Y,Y,Y,N,
N,N,N,N,N,N,N,N
]

wink = [
N,N,N,N,N,N,N,N,
N,Y,Y,N,N,N,N,N,
N,Y,Y,N,N,Y,Y,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,Y,N,N,N,N,Y,N,
N,Y,Y,Y,Y,Y,Y,N,
N,N,N,N,N,N,N,N
]

reset = [
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N
]

faces = [happy, sad, laugh, meh, wink]

sense.set_pixels(random.choice(faces))
#sense.set_pixels(reset)

with PiCamera() as camera:
	#camera.start_preview()
	#time.sleep(1)
	camera.capture('/home/pi/image.jpg')
	time.sleep(5)
	sense.set_pixels(reset)
	#camera.stop_preview()
	
	photo = open('/home/pi/image.jpg', 'rb')
	response = twitter.upload_media(media=photo)
	message = "Here's a selfie for the internet #RaspberryPi"
	twitter.update_status(status=message, media_ids=[response['media_id']])

Y = [0,255,0]
sense.set_pixels([
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,Y,N,
N,N,N,N,N,Y,Y,N,
N,Y,N,N,Y,Y,N,N,
N,Y,Y,Y,Y,N,N,N,
N,N,Y,Y,N,N,N,N,
N,N,N,N,N,N,N,N
])
time.sleep(10)
sense.set_pixels(reset)
