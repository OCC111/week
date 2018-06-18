print('-'*20)
print('欢迎进入节日祝福系统!!!')
print('1.娱乐\n2.乐娱\n3.退出')
print('-'*20)

a=['春节快乐','过年','大吉大利','国庆快乐','嗨皮波斯顿','元旦快乐','一溜儿玩啊','造作啊~']
b=['端午安康','端午快乐','端午吉祥','端午嗨皮','端午']

import time
import random

while True:
	print('='*20)
	user1 = input('请输入程序:')
	if user1 == '1':
		print('='*20)
		print('节日快乐!!!')
		time.sleep(3)
		suiji=random.sample(a,2)
		print('='*20)
		print(suiji)
	elif user1 == '2':
		print('='*20)
		print('端午嗨皮')
		time.sleep(2)
		jie=random.sample(b,2)
		print('='*20)
		print(jie)
	elif user1 == '3':
		break
