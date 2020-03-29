# Threadlocal
import threading

local = threading.local()


def process_student():
    student_name = local.name
    print('线程名：{}学生姓名:{}'.format(threading.current_thread().getName(), student_name))


def process_thread(name):
    local.name = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('张三',))
t2 = threading.Thread(target=process_thread, args=('李四',))
t1.start()
t2.start()
t1.join()
t2.join()