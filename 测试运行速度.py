import time
import multiprocessing

def totaltime(ct):
	st = time.time()
	a = 100.33  
	b = 23.33  
	for v in range(ct):
		b = 1 + b
		c = a * b
	print("total time:", time.time()-st)

ct = 25000000

if __name__ == '__main__':
	for i in range(multiprocessing.cpu_count()):
		p = multiprocessing.Process(target=totaltime, args=(ct,))
		p.start()
	for p in multiprocessing.active_children():
		print('Child process name: ' + p.name + ' id: ' + str(p.pid))