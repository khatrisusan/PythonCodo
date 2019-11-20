 BROADCAST_TO_PORT = 7000
import time
from socket import *
from datetime import datetime
from sense_hat import SenseHat
sense = SenseHat()


s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 14593))     # (ip, port)
# no explicit bind: will bind to default IP + random port
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
	data = "Current time " + str(datetime.now())
	s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
	print(data)
	time.sleep(1)
  # Take readings from all three sensors
  t = sense.get_temperature()
  t = round(t, 1)
  message = "Temperature: " + str(t)
  sense.show_message(message, scroll_speed=0.05)
 
