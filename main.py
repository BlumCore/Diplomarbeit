from m5stack import *
from m5stack_ui import *
from uiflow import *
import wifiCfg
from IoTcloud.AWS import AWS
from hardware import sdcard
from libs.json_py import *
import imu
import unit


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

label0 = M5Label('label0', x=46, y=80, color=0x000, font=FONT_MONT_14, parent=None)
label1 = M5Label('', x=46, y=160, color=0x000, font=FONT_MONT_14, parent=None)
try :
  heart_0 = unit.get(unit.HEART, unit.PORTA)
  heart_0.setLedCurrent(0x04, 0x01)
  heart_0.setMode(0x03)
except:
  label1.set_text("Sensor isn't pluged in")


imu0 = imu.IMU()

sdcard.SDCard(20000000)
uart1 = machine.UART(2, tx=14, rx=13)

wifiCfg.doConnect('iPhone von Yannik', 'fudai9d3vh0fc')
uart1.init(9600, bits=8, parity=None, stop=1)
if wifiCfg.wlan_sta.isconnected():
  aws = AWS(things_name='diplomarbeit', host='a16mkdqb0xdd3y-ats.iot.eu-north-1.amazonaws.com', port=8883, keepalive=60, cert_file_path="/flash/res/27c0-certificate.pem.crt", private_key_path="/flash/res/27c0-private.pem.key")
  aws.start()
  with open('/sd/values.txt', 'r') as fs:
    label0.set_text("sending values to AWS")
    Lines = fs.readlines()
    for line in Lines:
         aws.publish(str('core2/data'),str(line))
         wait_ms(500)
    fs.close()
  clear = open("/sd/values.txt",'w')
  clear.close()
  label0.set_text("all values sended to AWS")
  wait_ms(500)

  while True:
    gps = str(uart1.read())
    gpssplit = gps.split(",")
    label0.set_text("Working")
    lat = "n/a"
    lon = "n/a"
    if len(gpssplit) > 5:
      lat = gpssplit[3]
      lon = gpssplit[5]
    aws.publish(str('core2/gps'),str(uart1.read()))
    aws.publish(str('core2/data'),str((py_2_json({'xacc':(imu0.acceleration[0]),'yacc':(imu0.acceleration[1]),'heartrate':str(heart_0.getHeartRate()), 'lat': str(lat), 'long': str(lon)}))))
    wait_ms(500)
else:
  screen.set_screen_bg_color(0xefff00)    
  while True:
    with open('/sd/values.txt', 'a') as fs:
      label0.set_text("Working")
      gps = str(uart1.read())
      gpssplit = gps.split(",")
      lat = "n/a"
      lon = "n/a"
      if len(gpssplit) > 5:
        lat = gpssplit[3]
        lon = gpssplit[5]

      fs.write(str((py_2_json({'xacc':(imu0.acceleration[0]),'yacc':(imu0.acceleration[1]),'heartrate':str(heart_0.getHeartRate()), 'lat': str(lat), 'long': str(lon)}))))
      fs.write("\n")
      wait_ms(500)
