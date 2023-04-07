# coding:utf-8
import threading
import time

def job1():
    # 让这个线程多执行几秒
    time.sleep(5)
    print("the number of T1 is %s" % threading.current_thread())

if __name__ == "__main__":
    # 创建一个新的线程
    new_thread = threading.Thread(target=job1, name="T1")
    # 启动新线程
    new_thread.start()
    # 以下信息在job1函数内的打印之前出现，因为没有阻塞new_thread线程
    print("当前线程数量为", threading.active_count())
    print("所有线程的具体信息", threading.enumerate())
    print("当前线程具体信息", threading.current_thread())
