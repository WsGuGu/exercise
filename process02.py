# 继承实现多进程
from multiprocessing import Process
from time import sleep
from time import ctime


class ClockProcess(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print('子进程开始执行时间:{}'.format(ctime()))
        sleep(self.interval)
        print('子进程结束的时间:{}'.format(ctime()))


if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    p.join()
    print('主进程执行完')