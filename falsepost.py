import requests
import random
import threading

def randon():
    return random.randint(11111110,1111111111)
def randop():
    return random.randint(1000001,99999996)

proxies = {
  "http": "http://61.185.137.126:3128"
}
def post():
    
    try:
        while True:
            data={"username":str(randon()),"password":'a' + str(randop())}
            requests.post('http://lolcdapp.club/', data=data, proxies=proxies)
            print(data)
    except:
        print('error')
    
if __name__ == '__main__':
    threads_num = 8
    threads = []
    try:
        for i in range(threads_num):
            t = threading.Thread(target=post, name=i)
            threads.append(t)
            t.start()
    except:
        for t in threads:
            t.join()
            print('%s,over'%t.name)