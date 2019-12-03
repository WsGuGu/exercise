from multiprocessing import Process
from time import sleep
def run_proc(a,b):
    print("加法")
    sleep(3)
    print(a+b)

if __name__=='__main__':
    print('主进程')
    p=Process(target=run_proc,args=(1,2))
    p.start()
    p.join()
    print('主进程末尾')