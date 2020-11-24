#/user/bin/env/python
#-*- codding:utf-8 -*-

#主界面模块

from admin import Admin
from atm import ATM
1
import time

def main():
	alluser = {}
	#实例化对象
	admin = Admin()
	atm = ATM(alluser)
	#打印欢迎界面
	admin.printWelecom()


	#请管理员登录，并开机
	res1 = admin.adminlogin()
	if not res1:
		return -1

	time.sleep(2)


	#打印用户功能界面

	while True:
		admin.printFunctionSys()
		res = input("请输入您要办理的业务：")
		if res == "1":
			atm.openAcount()

		if res =="2":
			atm.inqure()
		if res =="3":
			atm.getMoney()
		if res == "4":
			atm.saveMoney()
		if res == "5":
			atm.changePassword()
		if res =="6":
			atm.cardLock()
		if res =="7":
			atm.unCardLock()
		if res == "8":
			atm.reMakeCard()
		if res == "9":
			atm.closeAccount()
		if res == "t":
			atm.Exit()
			time.sleep(2)
			return 0
		time.sleep(2)


if __name__ == "__main__":
		main()

