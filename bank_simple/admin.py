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
		print("*    改密（3）                  锁定（4）             *")
		print("*    解锁（3）                  补卡（4）             *")
		print("*    销户（3）                  退出（4）             *")
		print("*                                                   *")
		print("*****************************************************")

	def adminlogin(self):
		adminInput = input("请输入管理员账户：")
		if self.amin != adminInput:
			print("管理员账户输入错误。。。")
			return 0
		passwordInput = input("请输入密码：")
		if self.password != passwordInput:
			print("输入密码有误。。。。。。")
			return 0
		else:
			print("登录成功，请稍后。。。。。。。")
			return -1
		