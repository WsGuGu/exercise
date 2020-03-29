import _thread
import time


def fun1():
    print('startfun1')
    time.sleep(4)
    print('endfun1')


def fun2():
    print('startfun2')
    time.sleep(2)
    print('endfun2')


if __name__ == '__main__':
    print('start')
    _thread.start_new_thread(fun1, ())
    _thread.start_new_thread(fun2, ())
    time.sleep(7)