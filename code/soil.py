import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

from datetime import datetime

# Hardware SPI configuration
SPI_PORT    = 0
SPI_DEVICE  = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
print('soil.py is running...')

myFile = open("dataBase.txt","a")
Intervall = 3 # measured in seconds

while 42:
    try:
        time.sleep(Intervall) 
    except KeyboardInterrupt:
        myFile.close()
        break
    i = str(mcp.read_adc(7))
    t = str(datetime.now())
    if int(i) > 1000:
        print('IT IS GETTING DRY!!!\n ...Sending email...')
        #emailsender()
    s = t[:19] + ',' + i + '\t'
    myFile.write(s)

