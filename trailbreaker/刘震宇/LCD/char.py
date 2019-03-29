from machine import Pin
from micropython import const
import time
import ustruct
import framebuf

from pyb import Pin

png=[#第一次初始化
	"00000000",
	"",
	"",
	"",
	"",
	"",
	"",
	""
]

Letter=[#第一次初始化
		[[1,2,3,4,5,6,7,8],[[0,0,0,0,0,0,0,0,],[],[],[],[],[],[],[],]],
		[[1,2,3,4,5,6,7,8],[[0,0,0,0,0,0,0,0,],[],[],[],[],[],[],[],]],
		[[1,2,3,4,5,6,7,8],[[0,0,0,0,0,0,0,0,],[],[],[],[],[],[],[],]],
		[[1,2,3,4,5,6,7,8],[[0,0,0,0,0,0,0,0,],[],[],[],[],[],[],[],]],
		[[1,2,3,4,5,6,7,8],[[0,0,0,0,0,0,0,0,],[],[],[],[],[],[],[],]],
		[[1,2,3,4,5,6,7,8],[[0,0,0,0,0,0,0,0,],[],[],[],[],[],[],[],]],
		[[1,2,3,4,5,6,7,8],[[0,0,0,0,0,0,0,0,],[],[],[],[],[],[],[],]],
		[[1,2,3,4,5,6,7,8],[[0,0,0,0,0,0,0,0,],[],[],[],[],[],[],[],]]
		]
l=0

def char( char, x, y, color=0xffff, background=0x0000):#取frame画图
	global png
	global Letter
	global l
	w = 16
	buffer = bytearray(int(w*w/8))
	framebuffer = framebuf.FrameBuffer(buffer, w, w, framebuf.MONO_HLSB)
	print(char, bytearray(char))
	print("buf before", buffer)
	framebuffer.text(char, 0, 0)
	print("buf after", buffer)
	k=1
	for i in range(13):
		if i%2==0:
			print("buf ", i, buffer[i])
			a=(bin( buffer[i]))[2:]
			b=7-len(a)
			print(b)
			c='0'
			for i in range(b):#补0
				c=c+'0'
			a=c+a
			#print(a)
			
			png[k]=png[k]+a
			k=k+1
	

def show_png(a):#改为line函数使用的格式
	global Letter
	global l
	temp=list(a)
	b=a[0]
	a=[]
	for i in range(8):
		for j in range(8):
			if temp[i][j]=="1":
				Letter[l][1][i].append(j)
	l=l+1