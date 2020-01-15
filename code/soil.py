import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

from datetime import datetime
from random import seed
from random import randint
seed(1)

# Hardware SPI configuration
SPI_PORT    = 0
SPI_DEVICE  = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
print('soil.py is running...')

myFile = open("dataBase.txt","a")
Intervall = 3 # measured in seconds

while 42:
    try:
        #print("soil.py has enetered try")
        time.sleep(Intervall) 
    except KeyboardInterrupt:
        #print("KeyboardInterrupt has been caught.")
        myFile.close()
        break
    i = str(mcp.read_adc(0))
    t = str(datetime.now())
    #print(i)
    #print(t)
    if int(i) > 400:
        print('IT IS GETTING DRY!!!\n ...Sending email...')
        #send_mail()
    s = t[:19] + ',' + i + '\t'
    myFile.write(s)

