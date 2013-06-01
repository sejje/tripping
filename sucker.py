class Sucker:
	def __init__(self, name, email, phone):
		self.name = name
		self.email = email
		self.phone = phone

	def sms(self, url, response, message):
		print "SMS to " + self.name + ": " + message
