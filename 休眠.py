import 共用
import 準備召喚 # 2


def 進入():
    print('進入 休眠1')



def 更新():
    pass
    #print('休眠 更新')

    
def 按下(按鍵):
    if 按鍵 == '2':
        離開()
        共用.目前狀態 = 2
        準備召喚.進入()
            
    
def 離開():
    print('離開 休眠1')
    
