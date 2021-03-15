from 模擬3D模組 import *
from 視覺模組 import *
from 語音模組 import *

import 共用
import 鏡子狀態1
import 魔鏡狀態2
import 立體狀態3
import 視覺特效狀態4
import 水晶球狀態5

def 初始設定():
    共用.攝影機 = 開啟影像擷取(解析度='720p')
    共用.行1 = 0
    共用.行2 = 720
    共用.列1 = 438
    共用.列2 = 842
    
    語音辨識azure(key='fd570f9b66164d20a68dab0dcdbbb681', location='eastasia')
    暫停語音辨識()
    設定語音音量(100)
        
    
    共用.舞台 = 模擬3D引擎(400,600)
    共用.舞台.背景顏色 = color.rgb(0, 0, 0)
    
    共用.閃電聲音 = 載入聲音('聲音/遠處雷聲.wav')
    共用.火焰聲音 = 載入聲音('聲音/火焰聲音.wav')
    共用.奇怪風聲 = 載入聲音('聲音/奇怪風聲.wav')
    
    共用.鏡子 = 新增平面()
    共用.鏡子.縮放 = [9 * 1.6, 16* 1.6, 1]
    共用.鏡子.顏色 = color.rgba(255,255,255,255)
    共用.鏡子.有效狀態 = False
    
    共用.閃電 = 新增平面()
    共用.閃電.縮放 = [9 * 1.8, 16* 1.8, 1]
    共用.閃電.材質貼圖 = '影片/閃電.mp4'
    共用.閃電.有效狀態 = False
    
    共用.火焰 = 新增平面()
    共用.火焰.材質貼圖 = '影片/火焰.mp4'
    共用.火焰.位置z = 0
    共用.火焰.縮放x = 9*1.7
    共用.火焰.縮放y = 16*1.5
    共用.火焰.有效狀態 = False
    
    共用.煙霧 = 新增平面()
    共用.煙霧.材質貼圖 = '影片/煙霧.mp4'
    共用.煙霧.位置z = 0
    共用.煙霧.縮放x = 9*1.7
    共用.煙霧.縮放y = 16*1.5
    共用.煙霧.有效狀態 = False
    
    
    共用.魔鏡角色 = 新增6面貼圖方塊()
    共用.魔鏡角色.材質貼圖 = '圖片/魔鏡角色.png'
    共用.魔鏡角色.位置z = 0
    共用.魔鏡角色.縮放 = 6
    共用.魔鏡角色.有效狀態 = False   
        
    共用.愛心 = 新增物體()
    共用.愛心.模型 = '模型/愛心.obj'
    共用.愛心.著色器 = 光影著色器
    共用.愛心.顏色 = color.red
    共用.愛心.位置y = 2
    共用.愛心.縮放 = 2.5
    共用.愛心.有效狀態 = False 
    
    共用.水晶球 = 新增內面貼圖球體()
    共用.水晶球.縮放 = 5.7
    共用.水晶球.有效狀態 = False
    共用.水晶球.位置 = [0.5,2.8,0]
    
    共用.水晶球玻璃 = 新增平面()
    共用.水晶球玻璃.材質貼圖 = '圖片/水晶球玻璃.png'
    共用.水晶球玻璃.縮放 = 13
    共用.水晶球玻璃.位置 = [0.5,2,-1]
    共用.水晶球玻璃.有效狀態 = False
        
    共用.鏡子文字 = 新增文字('試著慢慢說\n「<red>魔鏡<default>魔鏡」', 尺寸='小')
    共用.鏡子文字.背景 = True    
    共用.鏡子文字.位置 = [-0.15,-0.2,0]
    共用.鏡子文字.有效狀態 = False
    
    
    命令 = '試著慢慢說\n「誰是最<red>美麗<default>的人」\n'
    命令 = 命令 + '「誰是最<red>可怕<default>的人」\n'
    命令 = 命令 + '「學校最<red>自由<default>的地方」'
    共用.命令文字 = 新增文字(命令, 尺寸='小')
    共用.命令文字.背景 = True    
    共用.命令文字.有效狀態 = False
    共用.命令文字.位置x = -0.25
    共用.命令文字.位置y = -0.2
    共用.命令文字.縮放 = [0.8, 0.8, 1]

    共用.美麗文字 = 新增文字('<black>「心地善良的人最美麗」\n\n<blue>說「魔鏡魔鏡」繼續', 尺寸='小')
    共用.美麗文字.位置 = [-0.25,-0.2,0]
    共用.美麗文字.有效狀態 = False

    共用.可怕文字 = 新增文字('「顛倒是非的人最可怕<default>」\n\n說「魔鏡魔鏡」繼續', 尺寸='小')
    共用.可怕文字.背景 = True
    共用.可怕文字.位置 = [-0.25,-0.2,0]
    共用.可怕文字.有效狀態 = False
    
    共用.導覽文字 = 新增文字(共用.操場導覽文字, 尺寸='小')
    共用.導覽文字.有效狀態 = False
    共用.導覽文字.位置x = -0.25
    共用.導覽文字.位置y = 0
    共用.導覽文字.縮放 = [0.7, 0.7, 1]    
    
    共用.鏡子動畫 = 動畫組合(
        動作(setattr, 共用.鏡子, '有效狀態', True),
        1,
        動作(setattr, 共用.鏡子文字, '有效狀態', True),
        1,
        動作(繼續語音辨識),
    )
    
 
    共用.魔鏡動畫 = 動畫組合(
        動作(共用.火焰聲音.播放),
        動作(setattr, 共用.火焰, '有效狀態', True),
        2,
        動作(setattr, 共用.魔鏡角色, '有效狀態', True),
        動作(setattr,共用.魔鏡角色,'位置',[0,5,-4]), 
        動作(setattr,共用.魔鏡角色,'旋轉',[0,180, 0]),
        動作(共用.魔鏡角色.位置動畫,[0,1,-4], 持續=1), 
        1,  
        動作(共用.魔鏡角色.旋轉動畫 , [0,0,0],持續=1),
        1,
        動作(語音合成, '我是哈哈魔鏡，請說出你的指令', 等待=False),
        4,
        動作(setattr, 共用.命令文字, '有效狀態', True),
        動作(繼續語音辨識),
    )
 
    共用.立體動畫 = 動畫組合(
        動作(共用.奇怪風聲.播放),
        動作(setattr, 共用.煙霧, '有效狀態', True),
        4,
        動作(setattr, 共用.煙霧, '有效狀態', False),
        動作(setattr, 共用.舞台, '背景顏色', color.rgb(255, 200, 200)),
        動作(setattr, 共用.愛心, '有效狀態', True),
        動作(語音合成, '心地善良的人最美麗', 等待=False),
        動作(setattr, 共用.美麗文字, '有效狀態', True),
        #動作(共用.美麗文字.逐字動畫),
        3,
        動作(繼續語音辨識),
    )

 
 
    共用.視覺特效動畫 = 動畫組合(
        動作(共用.奇怪風聲.播放),
        動作(setattr, 共用.煙霧, '有效狀態', True),
        4,
        動作(setattr, 共用.煙霧, '有效狀態', False),
        動作(setattr, 共用.鏡子, '有效狀態', True),
        動作(語音合成, '顛倒是非的人最可怕', 等待=False),
        動作(setattr, 共用.可怕文字, '有效狀態', True),
        動作(共用.可怕文字.逐字動畫),
        3,
        動作(繼續語音辨識),
    )
    
    共用.水晶球動畫 = 動畫組合(
        動作(共用.奇怪風聲.播放),
        動作(setattr, 共用.煙霧, '有效狀態', True),
        4,
        動作(setattr, 共用.煙霧, '有效狀態', False),
        動作(setattr, 共用.水晶球玻璃, '有效狀態', True),
        動作(共用.水晶球玻璃.淡入, 持續=1),
        0.5,
        動作(setattr, 共用.水晶球, '材質貼圖', '圖片/操場360.jpg'),
        動作(setattr, 共用.水晶球, '有效狀態', True),
        動作(共用.水晶球.淡入, 持續=2),
        1,
        動作(setattr, 共用.導覽文字, '有效狀態', True),
        動作(共用.導覽文字.逐字動畫, 速度=0.1),
        動作(語音合成, 共用.操場導覽內容, 等待=False),         
        10,
        動作(繼續語音辨識),
)

    共用.目前狀態 = 鏡子狀態1
    共用.目前狀態.進入()
