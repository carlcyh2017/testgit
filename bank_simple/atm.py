#user/bin/env/python
#_*_ ecoding :utf-8 _*_

from card import Card
from user import User

import random
import time

class ATM(object):
	def __init__(self,alluser):
		self.alluser = alluser

	def openAcount(self):
		name = input("请输入你的姓名：")
		id = input("请输入你的身份证号：")
		phone = input("请输入你的手机号：")
		money = int(input("请输入你的预存金额:"))
		passWord = input("请输入你的密码")


		passWord2 = input("请再次输入密码")

		if passWord != passWord2:
			print("两次密码输入不同。。。")
			return -1
		print("密码设置成功，请牢记密码%s" %passWord)
		cardId = self.creatCardNum()
