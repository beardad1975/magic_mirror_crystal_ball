from 模擬3D模組 import *
from 視覺模組 import *
import random as 隨機

攝影機 = 開啟影像擷取(解析度='720p')



鏡子 = 新增平面()
鏡子.位置z = 0.5
鏡子.縮放 = [9*1.65, 16*1.5, 1]
鏡子.顏色 = color.rgba(255,255,255,0)




物體 = 新增物體()
物體.模型 = '模型/愛心.obj'
物體.位置z = -10
物體.位置y = 0
物體.顏色 = color.rgba(255,0,0,150)
#物體.縮放 = 0.2
#物體.旋轉x = 270


def 當更新時(時間差):
#     陣列 = 擷取單張影像(攝影機)
#     鏡子.多維陣列貼圖 = 陣列
    物體.旋轉y += 3 
    

模擬主迴圈()