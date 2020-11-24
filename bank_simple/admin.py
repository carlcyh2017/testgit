#user/bin/env/python
#_*_ ecoding : utf-8 _*_

class Admin(object):
	admin = "1"
	password = "1"

	def printWelecom(self):
		print("*************************************")
		print("*                                   *")
		print("*                                   *")
		print("*           欢迎光临                 *")
		print("*                                   *")
		print("*                                   *")
		print("*************************************")

	def printFunctionSys(self):
		print("*************************************")
		print("*    开户（1）                  查询（2）             *")
		print("*    取款（3）                  存款（4）             *")
		print("*    改密（5）                  锁定（6）             *")
		print("*    解锁（7）                  补卡（8）             *")
		print("*    销户（9）                  退出（t）             *")
		print("*                                                   *")
		print("*****************************************************")

	def adminlogin(self):
		adminInput = input("请输入管理员账户：")
		if self.admin != adminInput:
			print("管理员账户输入错误。。。")
			return 0
		passwordInput = input("请输入密码：")
		if self.password != passwordInput:
			print("输入密码有误。。。。。。")
			return 0
		else:
			print("登录成功，请稍后。。。。。。。")
			return -1
		