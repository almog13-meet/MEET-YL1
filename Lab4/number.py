class integer(object):
	def __init__(self, n, negative_or_positive):
		self.number = n
		self.nop = negative_or_positive
	def display(self):
		print self.nop + str(self.number)

class NegativeInteger(integer):
	def __init__(self, n):
		super(NegativeInteger, self).__init__(n, "-") 

	def display(self):
		print "-" + str(self.number)

if __name__=="__main__":
	test = NegativeInteger(90)
	test.display()

#Q 8

