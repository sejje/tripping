class Sucker:
	def __init__(self, name, email, phone):
		self.name = name
		self.email = email
		self.phone = phone

	def sms(self, url, response, message):
		print "SMS to " + self.name + ": " + message

	def email(self, url, response, message):
		#format like "Down: http://sejje.net (404)"
		msg = "\n" + message + ": " + url + "(" + response + ")"
		server = smtplib.SMTP(email_server)
		server.starttls()
		server.login(email_address, email_password)
		server.sendmail(email_address, self.email, msg)
		print msg
		server.close
