import 共用
import 準備召喚狀態


def 進入():
    print('進入 休眠')

def 更新():
    pass
    print('休眠 更新')
    
def 按下(按鍵):
    if 按鍵 == 'space':
        離開()
        
        準備召喚狀態.進入()
        共用.目前狀態 = "準備召喚"
        
    
    
    
def 離開():
    print('離開 休眠')
    
