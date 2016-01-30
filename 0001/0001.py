# encoding: utf-8
import uuid

class Generate:
	def __init__(self):
		self.num = 0
		self.listid = []

	def generate_uuid(self, num):
		for i in xrange(int(num)):
			self.listid.append(uuid.uuid1())

	def get_uuid(self):
		return self.listid

if __name__ == '__main__':
	gen = Generate()
	gen.generate_uuid(200)
	keys = gen.get_uuid()
	f = file("gencodes.txt", "w")
	for key in keys:
		f.write(str(key) + "\n")
	f.close()

