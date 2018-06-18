print('$'*30)
print('欢迎进入系统后台')
print('$'*30)

def testB():
	print('----testB start----')
	print('这里是testB函数执行的代码')
	print('----    testB end    ----')
	
def testA():
	print('----testA start----')
	
	testB()

	print('----    testA end    ----')
testA()
