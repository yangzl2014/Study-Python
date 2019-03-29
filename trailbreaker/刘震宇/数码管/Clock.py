
#import music
#from music import *
#from led8seg import *


import pyb
from pyb import Pin,Timer
#import time

L1=262 # c 
L2=294 # d 
L3=330 # e 
L4=349 # f 
L5=392 # g 
L6=440 # a1 
L7=494 # b1 

# 定义中音音名
M1=523 # c1 
M2=587 # d1 
M3=659 # e1 
M4=698 # f1
M5=784 # g1 
M6=880 # a2 
M7=988 # b2 

# 定义高音音名
H1=1047 # c2 
H2=1175 # d2 
H3=1319 # e2 
H4=1397 # f2 
H5=1568 # g2 
H6=1760 # a3 
H7=1976 # b3 

# 定义时值单位，决定演奏速度（数值单位：ms） 
T=3600 

MyScore = [[L3, T/4], [L5, T/8+T/16], [L6, T/16], [M1, T/8+T/16], [M2, T/16], [L6, T/16], [M1, T/16],[L5, T/8], [M5, T/8+T/16], [H1, T/16],[M6, T/16], [M5, T/16], [M3, T/16], [M5, T/16], [M2, T/2], [ 1, 1] ]
# 省略后续乐曲数据，请感兴趣的读者补充完整
# 结束 
from struct import pack
rtc = pyb.RTC()
rtc.datetime((2014, 5, 1, 4, 13, 15, 13, 0))
print(rtc.datetime())
class USR_SPI:
    def __init__(self,scl,sda):
        self.scl = scl
        self.sda = sda

    def write_data(self,buf):
        for data in buf:
            print(data)
            pyb.delay(1)
            for i in range (8): #send data
                self.scl(0)
                if data & (0x01):
                    self.sda(1)
                else:
                    self.sda(0)
                self.scl(1)
                data = data >> 1 

class AIP1638:
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs

    def _data(self, data):
        self.cs(0)
        pyb.delay(1)
        self.spi.write_data(data)
        pyb.delay(1)
        self.cs(1)

    def disp_on(self):
        self._data(b"\x8d")

    def disp_off(self):
        self._data(b"\x80")

Number=[#0                
	[1,1,1,1, 1 , 1 , 0 ,0 ],
	#1
	[ 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ],
	#2
	[ 01 , 01 , 00 , 01 , 01 , 00 , 01 , 00 ],
	#3
	[ 01 , 01 , 01 , 01 , 00 , 00 , 01 , 00 ],
	#4
	[ 00 , 01 , 01 , 00 , 00 , 01 , 01 , 00 ],
	#5
	[ 01 , 00 , 01 , 01 , 00 , 01 , 01 , 00 ],
	#6
	[ 01 , 00 , 01 , 01 , 01 , 01 , 01 , 00 ],
	#7
	[ 01 , 01 , 01 , 00 , 00 , 00 , 00 , 00 ],
	#8
	[ 01 , 01 , 01 , 01 , 01 , 01 , 01 , 00 ],
	#9
	[ 01 , 01 , 01 , 01 , 00 , 01 , 01 , 00 ]
]



result=[0,0,0,0,0,0,0,0]
def show(h,m,s):#将时间转化为可以写入寄存器的形式
	global Number,result
	result=[0,0,0,0,0,0,0,0]
	time=Number
  #初始化时分秒的各位与十位
	time_hH=[[0 for col in range(8)] for row in range(10)]#小时的十位
	time_hL=[[0 for col in range(8)] for row in range(10)]#小时的个位
	time_mH=[[0 for col in range(8)] for row in range(10)]#分钟的十位
	time_mL=[[0 for col in range(8)] for row in range(10)]#分钟的个位
	time_sH=[[0 for col in range(8)] for row in range(10)]#秒钟的十位
	time_sL=[[0 for col in range(8)] for row in range(10)]#秒钟的个位
  #转换为String类型
	h_s=str(h)
	m_s=str(m)
	s_s=str(s)
  #输出log，用于测试（已注释掉）
	#print(len(h_s))
	#print(8-len(h_s))
	#print(int((h_s)[0]))
	for i in range(8):
		if len(h_s)>1:#小时数是两位
			time_hH[int((h_s)[0])][i]=time[int((h_s)[0])][i] << (6)#小时的十位应显示在上一行的第三个位置，数据需要左移6位
			time_hL[int((h_s)[1])][i]=time[int((h_s)[1])][i] << (7)#小时的个位应显示在上一行的第四个位置，数据需要左移7位
      #赋值给result变量
			result[i]=result[i]+time_hH[int((h_s)[0])][i]
			result[i]=result[i]+time_hL[int((h_s)[1])][i]
		else :#小时数是一位，处理方式和上面差不多
			time_hL[int((h_s)[0])][i]=time[int((h_s)[0])][i] << (7)
			result[i]=result[i]+time_hL[int((h_s)[0])][i]

		if len(m_s)>1:#分钟数是两位
			time_mH[int((m_s)[0])][i]=time[int((m_s)[0])][i] << 0#分钟的十位显示在第二行的第一个位置，数据不需左移
			time_mL[int((m_s)[1])][i]=time[int((m_s)[1])][i] << 1#分钟的个位显示在第二行的第二个位置，数据需要左移1位
      #赋值给result变量
			result[i]=result[i]+time_mH[int((m_s)[0])][i]
			result[i]=result[i]+time_mL[int((m_s)[1])][i]
		else :#分钟数是一位，处理方式和上面差不多
			time_mL[int((m_s)[0])][i]=time[int((m_s)[0])][i]<<1
			result[i]=result[i]+time_mL[int((m_s)[0])][i]
		if len(s_s)>1:#秒钟数是两位
			time_sH[int((s_s)[0])][i]=time[int((s_s)[0])][i]<<(2)#秒钟的十位显示在第二行的第三个位置，数据需要左移2位
			time_sL[int((s_s)[1])][i]=time[int((s_s)[1])][i]<<(3)#秒钟的个位显示在第二行的第四个位置，数据需要左移3位
      #赋值给result变量
			result[i]=result[i]+time_sH[int((s_s)[0])][i]
			result[i]=result[i]+time_sL[int((s_s)[1])][i]
		else:#秒钟数是一位，处理方式和上面差不多
			time_sL[int((s_s)[0])][i]=time[int((s_s)[0])][i]<<(3)
			result[i]=result[i]+time_sL[int((s_s)[0])][i]
#输出log，用于测试
	for i in range(8):
		print(bin(result[i]))
spi = USR_SPI(scl=Pin('X1',Pin.OUT_PP), sda=Pin('X3',Pin.OUT_PP))
display = AIP1638(spi,cs=Pin('X2',Pin.OUT_PP))
#设定开始的时间
rtc = pyb.RTC()
rtc.datetime((2014, 5, 1, 4, 13, 15, 21, 0))
#检查是否设定成功
print(rtc.datetime())
a=rtc.datetime()
#获取最开始的时间
clk_hours=a[4]
clk_minutes=a[5]
clk_seconds=a[6]
#设定闹钟，单位：秒
clk=5

i=0

while True:
	#每次开始循环都需要获取当前时间
	a=rtc.datetime()
	hours=a[4]
	minutes=a[5]
	seconds=a[6]
	print(hours,minutes,seconds)
	show(hours,minutes,seconds)
  
  #开始向寄存器中写入数据
	display.disp_on()
	display._data(b"\x40")#设为开始输入数据
	s=(b"\xC0")
	for  i in  range(8):#把result内的数据写入s内，s为需要写入的数据
		s+=pack('<H', result[i])
	print(s)
	display._data(s)
	display.disp_on()#数据写入完毕
  #计算是否到设定的时间
	temp=(hours-clk_hours)*3600+(minutes-clk_minutes)*60+(seconds-clk_seconds)*1
	if temp==clk:#闹钟开始
  #设定引脚以及定时器
		x1 = Pin('X4',Pin.OUT_PP)
		tm3=Timer(2, freq=MyScore[i][0])
		led3=tm3.channel(4, Timer.PWM, pin=x1,pulse_width_percent=50)
		for i in range(16):
    #读取时间，用于更新显示
			b=rtc.datetime()
			b_hours=b[4]
			b_minutes=b[5]
			b_seconds=b[6]
			print(b_hours,b_minutes,b_seconds)
      #改变频率用以播放音乐
			tm3.freq(MyScore[i][0])
			show(b_hours,b_minutes,b_seconds)#时间转化为result
      #写入寄存器
			display.disp_on()
			display._data(b"\x40")#设为开始输入数据
			clock_s=(b"\xC0")
			for  i in  range(8):
				clock_s+=pack('<H', result[i])
			display._data(clock_s)
			display.disp_on()
			pyb.delay(int(MyScore[i][1]))
	pyb.delay(1000)#延时一秒钟







