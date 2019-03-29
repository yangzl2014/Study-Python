from pyb import Pin

r=[Pin(i, Pin.OUT_PP) for i in ['X2','X1','X3','X4','X5','X6','X8','X7']]
for i in range (8):
	r[i].high()

c=[Pin(i, Pin.OUT_PP) for i in ['Y2','Y1','Y3','Y4','Y5','Y6','Y8','Y7']]
for i in range (8):
	c[i].high()
Letter=[
		[#I
			[1,2,3,4,5,6,7,8],
			[[],
			[2,3,4],
			[3],
			[3],
			[3],
			[3],
			[2,3,4],
			[]]
		],
		[#xin
			[1,2,3,4,5,6,7, 8],
			[[],
			[1,2,4,5],
			[0,3,6],
			[0,6],
			[1,5],
			[2,4],
			[3],
			[]]
		],
		[#N
			[1,2,3,4,5,6,7, 8],
			[[],
			[2,6],
			[2,3,6],
			[2,4,6],
			[2,4,6],
			[2,5,6],
			[2,6],
			[]]
		],
		[#E
			[1,2,3,4,5,6,7, 8],
			[[],
			[2,3,4,5],
			[2],
			[2,3,4,5],
			[2],
			[2],
			[2,3,4,5],
			[]]
		],
		[#U
			[1,2,3,4,5,6,7, 8],
			[[],
			[1,6],
			[1,6],
			[1,6],
			[1,6],
			[1,6],
			[2,3,4,5],
			[]]
		]
		]

def line(row,colDisp):
	r[row-1].low() #打开某行
	for j in colDisp: 
		if (j>=0 and j<=7):
			c[j].low()#开启
			pyb.delay(1)
			c[j].high()#熄灭
	r[row-1].high()#关闭行

def show_LED(temp_show):
	#temp = Letter[]
	for k in range(50):
		for i in range(len(temp_show)):
			for l in range(8):
			#for j in range(len(temp[1][i])):
				#print(temp_show[i][0][l],temp_show[i][1][l])
				line(temp_show[i][0][l],temp_show[i][1][l])
		
		
def reset():
	global Letter
	Letter=[
		[#I
			[1,2,3,4,5,6,7,8],
			[[],
			[2,3,4],
			[3],
			[3],
			[3],
			[3],
			[2,3,4],
			[]]
		],
		[#xin
			[1,2,3,4,5,6,7, 8],
			[[],
			[1,2,4,5],
			[0,3,6],
			[0,6],
			[1,5],
			[2,4],
			[3],
			[]]
		],
		[#N
			[1,2,3,4,5,6,7, 8],
			[[],
			[1,2,7],
			[1,3,7],
			[1,4,7],
			[1,4,7],
			[1,5,7],
			[1,6,7],
			[]]
		],
		[#E
		[1,2,3,4,5,6,7, 8],
		[[],
		[2,3,4,5],
		[2],
		[2,3,4,5],
		[2],
		[2],
		[2,3,4,5],
		[]]
		],
		[#U
			[1,2,3,4,5,6,7, 8],
			[[],
			[1,6],
			[1,6],
			[1,6],
			[1,6],
			[1,6],
			[2,3,4,5],
			[]]
		]
		]

def init():
	global Letter
	temp=Letter
	#更改数组内的值并赋给temp
	for i in range(len(temp)):# 2 loops 选择字母
		for j in range(8):#8 loops 选择行
			for k in range(len(temp[i][1][j])):#每行的每个点加8
				temp[i][1][j][k]=temp[i][1][j][k]+8*i
	#值更改完毕，开始左移，每显示一个，左移一个单位，即所有的数字减一
	#还需加上判断，小于0则灭，等于0为亮，大于7位灭，等于7位亮
def move():
	global Letter
	temp=Letter
	for i in range(len(temp)):# 2 loops 选择字母
		for j in range(8):#8 loops 选择行
			for k in range(len(temp[i][1][j])):
				temp[i][1][j][k]=temp[i][1][j][k]-1
				#一个循环后，某行的所有的点向左移动一位
		#8个循环后，一个字母的所有点向左一位
	#show_LED(temp)
	
			
		
while True:
	init()
	for i in range(len(Letter)*8+4):
		move()
		show_LED(Letter)
		pyb.delay(25)
	reset()
