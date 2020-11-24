#user/bin/env/python
#_*_ coding:utf-8 _*_

class Card(object):
	def __init__(self,cardId,passWord,money):
		self.cardId = cardId
		self.passWord = passWord
		self.money = money
		self.cardLock = False
