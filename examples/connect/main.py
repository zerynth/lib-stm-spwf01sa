import streams

from wireless import wifi
from stm.spwf01sa import spwf01sa as wifi_driver

streams.serial()

SSID = "<SSID>"
PASSWORD = "<PASSWORD>"

try:
   # Wifi 4 Click on slot B (specify which serial port will be used and which RST pin
    wifi_driver.init(SERIAL1,D16, baud=9600)
except Exception as e:
    print(e)for i in range(0,5):
    try:
        # connect to the wifi network (Set your SSID and password below)
        wifi.link(SSID , wifi.WIFI_WPA2, PASSWORD)
        print("Connect")
        break
    except Exception as e:
        print("Can't link",e)
else:
    print("Impossible to link!")
    while True:
        sleep(1000)
