import goldCode
import threading
import time

class goldEriteMysql(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID= threadID
        self.name= name
        self.counter= counter
    def run(self) -> None:
        i=1
        while True:
            tm=time.localtime(time.time())
            print('[',tm.tm_year,tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min,tm.tm_sec,']'+'线程'+self.name+'开始第'+str(i)+'次运行！')
            goldCode.request()
            i = i + 1
            print('线程'+self.name+'进入睡眠！')
            time.sleep(60*20)
            print('线程'+self.name+'睡眠结束！')


try:
    g= goldEriteMysql(1,'gold',1)

    g.start()
    g.join()

except:
    pass