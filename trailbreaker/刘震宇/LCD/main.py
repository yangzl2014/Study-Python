


import lcd_show
from lcd_show import *
import pyb
from pyb import Pin
u1=Pin('X9',Pin.IN,Pin.PULL_UP)
u2=Pin('X10',Pin.IN,Pin.PULL_UP)
#LCD
usrspi = USR_SPI(scl=Pin('X6',Pin.OUT_PP), sda=Pin('X7', Pin.OUT),dc=Pin('X8', Pin.OUT))
disp = DISPLAY(usrspi,cs=Pin('X5', Pin.OUT),res=Pin('X4', Pin.OUT),led_en=Pin('X3', Pin.OUT))


disp.clr(disp.WHITE)
disp.putChinese(50,50,Chinese,disp.BLACK)


print(123456)















