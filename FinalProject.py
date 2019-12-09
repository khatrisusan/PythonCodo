import string as Location
import string as SensorName
Location="D3.14"
SensorName="Raspberry-pi"
from datetime import datetime
from sense_hat import SenseHat
sense = SenseHat()
BROADCAST_TO_PORT = 7000
import time
from socket import *
from datetime import datetime


s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 14593))     # (ip, port)
# no explicit bind: will bind to default IP + random port
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Sensor Name:" +str(SensorName) +" "+ "Location :" + str(Location)+" "+ "Date Time: "+ str(datetime.now()) +" " +"Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h) 
  #Displaying the message in console command prompt
  print(message)
  s.sendto(bytes(message, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
  
  # Display the scrolling message
  # sense.show_message(message, scroll_speed=0.05)
  time.sleep(1)
