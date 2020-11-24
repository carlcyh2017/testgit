#user/bin/env/python
#_*_ ecoding :utf-8 _*_

from card import Card
from user import User

import random
import time

class ATM(object):
	def __init__(self,alluser):
		self.alluser = alluser

	#开户
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
		cardId = self.creatCardNum() #创建ID单独写一个类方法

		card = Card(cardId,passWord,money)
		user = User(name,id,phone,card)

		#存入到字典
		self.alluser[card.cardId] = user
		print("您的开户已完成，请牢记开户账号 %d"  %cardId)

	#查询
	def inqure(self):
		cardNuminput = int(input("请输入您的卡号"))
		user = self.alluser.get(cardNuminput)

		if not self.alluser.get(cardNuminput):
			print("此卡号不存在。。。")
			return -1
		if not self.verify(user.card.passWord):
			return -1

		print("您的余额为: %d" %user.card.money)

	#取钱
	def getMoney(self):
		cardNuminput = int(input("请输入您的卡号"))
		user = self.alluser.get(cardNuminput)

		if not self.alluser.get(cardNuminput):
			print("此卡号不存在。。。")
			return-1
		if not self.verify(user.card.passWord):
			return -1

			num = int(input("请输入您的取款金额："))

		if not self.judgeNum(num): #判断金额是否有误的函数单独写一个类方法
			return -1
		user.card.money -= num

		print("取款成功，您的余额为：%d" %user.card.money)


	#存钱
	def saveMoney(self):
		cardNuminput = int(input("请输入您的卡号："))
		user = self.alluser.get(cardNuminput)

		if not self.alluser.get(cardNuminput):
			print("此卡号不存在。。。")
			return -1

		if not self.verify(user.card.passWord):

			return -1

		num = int(input("请输入您的存款金额:"))

		if not self.judgeNum(num):
			return -1
		user.card.money +=num
		print("取款成功，您的余额为%d" %user.card.money)

    #锁卡
	def cardLock(self):
		cardNuminput = int(input("请输入您的卡号"))
		user = self.alluser.get(cardNuminput)

		if not self.alluser.get(cardNuminput):
			print("此卡号不存在。。。")
			return -1

		if not self.verify(user.card.passWord):
			return -1
		user.card.cardLock = True
		print("卡已锁定")

	#解锁卡
	def unCardLock(self):
			cardNuminput = int(input("请输入您的卡号"))
			user = self.alluser.get(cardNuminput)

			if not self.alluser.get(cardNuminput):
				print("此卡号不存在。。。")
				return -1

			if not self.verify(user.card.passWord):
				return -1
			user.card.cardLock = False
			print("卡已解锁")

	#改密码
	def changePassword(self):
		cardNuminput = int(input("请输入您的卡号"))
		user = self.alluser.get(cardNuminput)

		if not self.alluser.get(cardNuminput):
			print("此卡号不存在")
			return -1

		if not self.verify(user.card.passWord):
			return -1
		changePassword = int(input("请输入要修改的密码："))
		user.card.passWord = changePassword
		print("密码修改成功，请牢记密码 %d" %changePassword)




	#注销账户
	def closeAccount(self):
		cardNuminput = int(input("请输入您的卡号"))
		user = self.alluser.get(cardNuminput)


		if not self.alluser.get(cardNuminput):
			print("此卡号不存在。。。")
			return -1

		if not self.verify(user.card.passWord):
			return -1
		del user

	#重开卡
	def reMakeCard(self):
		cardNuminput = int(input("请输入您的卡号"))
		user = self.alluser.get(cardNuminput)

		if not self.alluser.get(cardNuminput):
			print("此卡号不存在。。。")
			return -1

		idInput = input("请输入您的身份证号码：")
		if idInput == user.id:
			print("现在为您重新开户，请稍后。。。")
			time.sleep(2)
			self.openAcount()

	#退出系统
	def Exit(self):
		print("系统正在退出。。。")
		return -1

	#密码验证
	def verify(self,passWord):

		for i in range(3):
			psd2 = input("请输入密码")
			if psd2 == self.passWord:
				return True

		print("密码输错3次，系统自动退出。。。")
		return False

	#生成随机卡号

	def creatCardNum(self):
		return random.randrange(100000,1000000)

	#判断金额是否有误
	def judgeNum(self,num):
		while num <=0:
			num  = int(input("您输入的金额有误："))
		return -1


		




