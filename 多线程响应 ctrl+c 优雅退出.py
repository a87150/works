import time
import random
from threading import Thread

stop = False
threads_num = 10

todos = list(range(1000))
total = len(todos)

def test(name):
    while todos:
        todo = todos.pop()
        # print('{}获取到 todo-{}'.format(name, todo))
        sleep_time = random.randint(1, 5) / 10
        # print('{}休息{}秒'.format(name, sleep_time))
        time.sleep(sleep_time)
        if stop:
            print('{}收到结束信号正在处理'.format(name))
            break
    print('{}结束'.format(name))


if __name__ == '__main__':
    start_time = time.time()
    # 启动线程
    threads = []
    for i in range(threads_num):
        t = Thread(target = test, args = ('线程-{}'.format(i),))
        threads.append(t)
        t.start()
    
    # 响应 ctrl+c
    try:
        while todos:
            print('已完成{}中的{}，还剩余{}'.format(total, total - len(todos), len(todos)))
            time.sleep(1)
    except KeyboardInterrupt as e:
        print('收到结束信号，正在处理')
        stop = True

    # 确认所有子线程结束
    for t in threads:
        t.join()
        
    print('所有子线程已结束')
    print('执行清理工作...')
    print('共计用时{}秒'.format(time.time() - start_time))