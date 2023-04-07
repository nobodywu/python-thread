# coding:utf-8
# 导入threading包
import threading


if __name__ == "__main__":
    print("当前活跃线程的数量", threading.active_count())
    print("将当前所有线程的具体信息展示出来", threading.enumerate())
    print("当前的线程的信息展示", threading.current_thread())
