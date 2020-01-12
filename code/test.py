import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration
SPI_PORT    = 0
SPI_DEVICE  = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

print('soil.py is running...')
while True:
    print(mcp.read_adc(0))
    time.sleep(1)