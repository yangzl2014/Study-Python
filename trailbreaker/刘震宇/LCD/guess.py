
import lcd_show
from lcd_show import *
import pyb
from pyb import Pin
from font import *
u1=Pin('X9',Pin.IN,Pin.PULL_UP)
u2=Pin('X10',Pin.IN,Pin.PULL_UP)
#LCD
usrspi = USR_SPI(scl=Pin('X6',Pin.OUT_PP), sda=Pin('X7', Pin.OUT),dc=Pin('X8', Pin.OUT))
disp = DISPLAY(usrspi,cs=Pin('X5', Pin.OUT),res=Pin('X4', Pin.OUT),led_en=Pin('X3', Pin.OUT))
x1 = Pin('X4',Pin.OUT_PP)
R=[Pin('X9',Pin.OUT_PP),Pin('X10',Pin.OUT_PP),Pin('Y3',Pin.OUT_PP),Pin('Y4',Pin.OUT_PP)]
C=[Pin('Y5',Pin.IN,Pin.PULL_UP),Pin('Y6',Pin.IN,Pin.PULL_UP),Pin('Y7',Pin.IN,Pin.PULL_UP),Pin('Y8',Pin.IN,Pin.PULL_UP)]
round=1
player1=0
player2=0
choose1=0
choose2=0
score1=0
score2=0
res=0
disp.clr(disp.WHITE)
#disp.putChinese(50,50,Chinese,disp.BLACK)
#disp.show_number(50,50,0,disp.BLACK)
#初始化界面

def init():
  global round
  #胜者为
  disp.putChinese(0,64,UI_1,disp.BLACK)
  #乙
  disp.putChinese(0,0,UI_3,disp.BLACK)
  #甲
  disp.putChinese(0,144,UI_2,disp.BLACK)
  #得分：
  disp.putChinese(80,72,UI_4,disp.BLACK)
  disp.putChinese(80,56,UI_5,disp.BLACK)
  #甲：
  disp.putChinese(96,88,UI_2,disp.BLACK)
  disp.putChinese(96,72,UI_5,disp.BLACK)
  #乙:
  disp.putChinese(112,88,UI_3,disp.BLACK)
  disp.putChinese(112,72,UI_5,disp.BLACK)
  #局数
  disp.show_number(40,66,round,disp.BLACK)
  round=round +1
  
def detect():
  global player1,player2,choose1,choose2,R,C,res
  if choose1==0 :
    for i in range(0,4):
      R[i].low()
      for k in range(0,4):
        if k!=i:
          R[k].high()
      for j in range(0,4):
        if i==0 and j==0 and C[j].value()==0:
          pyb.delay(30)
          if C[j].value()==0:
            player1=1
        elif i==3 and j==0 and C[j].value()==0:
          pyb.delay(30)
          if C[j].value()==0:
            res=1
  if  choose2==0:
    for i in range(0,4):
      R[i].low()
      for k in range(0,4):
        if k!=i:
          R[k].high()
      for j in range(0,4):
        if i==0 and j==2 and C[j].value()==0:
          pyb.delay(30)
          if C[j].value()==0:
            player2=1
        elif i==3 and j==0 and C[j].value()==0:
          pyb.delay(30)
          if C[j].value()==0:
            res=1
            
            
init()


while True:
  
  disp.scissor(64,64,0x0000)
  detect()
  if player1==1:#选择剪刀
    choose1=1
    disp.scissor(56,128,0x0000)#甲下方显示剪刀
    player1=0
  if player2==1:
    choose2=1
    disp.scissor(56,0,0x0000)#乙下方显示剪刀
    player2=0
  disp.putrect(64,64,16,32,0xffff)
  disp.stone(64,64,0x0000)
  detect()
  print(choose1,choose2)
  if player1==1:#选择石头
    choose1=2
    disp.stone(56,128,0x0000)#甲下方显示石头
    player1=0
  if player2==1:
    choose2=2
    disp.stone(56,0,0x0000)#乙下方显示石头
    player2=0
  disp.putrect(64,64,16,32,0xffff)
  disp.cloth(64,64,0x0000)
  detect()
  print(choose1,choose2)
  if player1==1:#选择布
    choose1=3
    disp.cloth(56,128,0x0000)#甲下方显示布
    player1=0
  if player2==1:
    choose2=3
    disp.cloth(56,0,0x0000)#乙下方显示布
    player2=0
  disp.putrect(64,64,16,16,0xffff)
  print(choose1,choose2)
  if choose1>0 and choose2>0:
    if choose1==1 :
      if choose2==1:
        disp.putChinese(0,48,UI_6,disp.BLACK)
      if choose2==2:
        disp.putChinese(0,48,UI_3,disp.BLACK)
        score2=score2+1
      if  choose2==3:
        disp.putChinese(0,48,UI_2,disp.BLACK)
        score1=score1+1
    if choose1==2:
      if choose2==1:
        disp.putChinese(0,48,UI_2,disp.BLACK)
        score1=score1+1
      if choose2==2:
        disp.putChinese(0,48,UI_6,disp.BLACK)
      if choose2==3:
        disp.putChinese(0,48,UI_3,disp.BLACK)
        score2=score2+1
    if choose1==3:
      if choose2==1:
        disp.putChinese(0,48,UI_3,disp.BLACK)
        score2=score2+1
      if choose2==2:
        disp.putChinese(0,48,UI_2,disp.BLACK)
        score1=score1+1
      if choose2==3:
        disp.putChinese(0,48,UI_6,disp.BLACK)
    #更新甲得分
    disp.putrect(96,64,16,16,0xffff)
    disp.show_number(96,64,score1,disp.BLACK)
    #更新乙得分
    disp.putrect(112,64,16,16,0xffff)
    disp.show_number(112,64,score2,disp.BLACK)
    choose1=0
    choose2=0
  if res==1:
    choose1=0
    choose2=0
    disp.putrect(0,48,16,16,0xffff)#清除结果
    disp.putrect(56,128,16,32,0xffff)#清除甲的选择
    disp.putrect(56,0,16,32,0xffff)#清除乙的选择
    disp.putrect(40,66,16,8,0xffff)#清除回合数
    disp.show_number(40,66,round,disp.BLACK)#局数
    round=round +1
    res=0












