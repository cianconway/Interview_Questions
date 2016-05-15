class Person(object):
	def __init__(self, name):
		self.name = name

	def reveal_identity(self):
		print "My name is {}".format(self.name)

class SuperHero(Person):
	def __init__(self, name, hero_name):
		super(SuperHero, self).__init__(name)
		self.hero_name = hero_name

	def reveal_identity(self):
		super(SuperHero, self).reveal_identity()
		print ".. and my alter ego is {}".format(self.hero_name)

cian = Person('Cian')
cian.reveal_identity()

wade = SuperHero('Wade Wilson', 'Deadpool')
wade.reveal_identity()