# coding:utf-8
import threading
import time

def job1():
    print("T1 start")
    for i in range(5):
        time.sleep(1)
        print(i)
    print("T1 finish")


def main():
    # 新创建一个线程
    new_thread = threading.Thread(target=job1, name="T1")
    # 启动新线程
    new_thread.start()
    # 阻塞这个T1线程
    new_thread.join()
    print("All done...")


if __name__ == "__main__":
    main()
