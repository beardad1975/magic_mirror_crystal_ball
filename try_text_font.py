
from 模擬3D模組 import *
import random as 隨機

舞台 = 模擬3D引擎(400,600)
舞台.背景顏色 = color.black

文字物體 = 新增文字('試著說<red>魔鏡魔鏡')
文字物體.y = -.3
文字物體.x = -0.3

中心物體 = 新增立方體()
# 顏色清單 = [color.red, color.yellow, color.orange,
#          color.green, color.white]
顏色清單 = [color.rgba(255,255,255,130),
        color.rgba(0,255,0,130),
        color.rgba(255,255,0,130),
        color.rgba(255,125,0,130),
        color.rgba(250,0,0,130)]

decor = []
for i in range(10):
    for j in range(10):
        物體 = 新增平面()
        物體.材質貼圖 = '圖片/愛心.png'
        物體.兩面貼圖 = True
        
        #物體 = 新增立方體()
        物體.位置 = [隨機.randint(-10,10),
                     隨機.randint(-10,10),
                     隨機.randint(-10,10)]
        物體.上層物件 = 中心物體
        物體.顏色 = 隨機.choice(顏色清單)
        
        物體.縮放 = 隨機.random() * 1.5
        
        
#         物體.旋轉 = [隨機.randint(0,90),
#                     隨機.randint(0,90),
#                     隨機.randint(0,90)]    
        decor.append(物體)


#透明 = color.rgba(255,255,255,0)
#不透明 = color.rgba(255,255,255,255)

魔鏡角色 = 新增6面貼圖方塊()
魔鏡角色.材質貼圖 = '魔鏡角色紋理'
魔鏡角色.位置z = 0
魔鏡角色.縮放 = 6
魔鏡角色.顏色 = color.clear


#物體.旋轉動畫([90,0,0], 持續=1)
#物體.位置動畫([1,0,0], 持續=1)
#魔鏡角色.顏色動畫([255,0,0,255], 持續=1)


# 角色到上方 = 
# 角色朝後 = 
# 角色隱藏 = 
# 角色顯示動畫 = 
# 角色移至中間動畫 = 
# 
# 角色轉向前動畫 = 


登場動畫 = 動畫組合(
    動作(setattr,魔鏡角色,'位置',[0,5,0]), 
    動作(setattr,魔鏡角色,'旋轉',[0,180, 0]),
    動作(setattr,魔鏡角色,'顏色', color.clear),
    動作(魔鏡角色.顏色動畫,color.white, 持續=1),
    動作(魔鏡角色.位置動畫,[0,0,0], 持續=1), 
    1,  
    動作(魔鏡角色.旋轉動畫 , [0,0,0],持續=1), 
    )

說話動畫組合 = 動畫組合(
    動作(魔鏡角色.晃動),
    0.3,
    動作(魔鏡角色.晃動),
    0.7,
    loop=True,
    )





旋轉速度 = [.05, 0.4, .05]


def 當更新時(時間差):
    #中心物體.旋轉 += 旋轉速度
    
    中心物體.旋轉y += .5
    
def 當按下時(按鍵):
    global 旋轉速度
    if 按鍵 == '+' :
        旋轉速度[0] += 0
        旋轉速度[1] += 0.1
        旋轉速度[2] += 0
        print(旋轉速度)
    elif 按鍵 == '-' :
        旋轉速度[0] -= 0
        旋轉速度[1] -= 0.1
        旋轉速度[2] -= 0
        print(旋轉速度)
    elif 按鍵 == 'space' :
        文字物體.逐字動畫(速度=0.5)
    elif 按鍵 == 'a' :        
        登場動畫組合.start()
    elif 按鍵 == 's' :
        魔鏡角色.晃動()
        
    elif 按鍵 == 't' :
        if 說話動畫組合.paused:
            說話動畫組合.start()
        else:
            說話動畫組合.pause()


模擬主迴圈()
