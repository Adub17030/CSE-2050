class BankAccount():
	def __init__(self, name, pasword, balance):
		self.name = name
		self.pasword = pasword
		self.balance = balance
	def desposit(self, money, paswordFromUser):
		if paswordFromUser == self.pasword:
			self.balance += money
		else:
			print('invalid')
	def withdraw(self, money, pasword):
		if paswordFromUser == self.pasword:
			self.balance -= money
			return money
		else:
			print('invalid')
	def changePassword(self, oldpass, newpass):
		if oldpass == self.pasword:
			self.pasword = newpass
		else:
			print('invalid')


d = BankAccount('duy', 'ss', 100)
d.desposit(400, 'ss')
print(d.balance)
print(d.pasword)