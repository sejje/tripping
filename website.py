import time
import requests

class Website:
	def __init__(self, url, interval, suckers):
		self.url = url
		self.interval = interval
		self.time_for_next = time.time()
		self.last_response = 0
		self.suckers = suckers
		self.status = 0

	def get(self):
		r = requests.get(self.url)
		self.last_response = r.status_code
		return r.status_code

	def clear(self):
		if self.status > 2:
			self.alert_up()
		self.status = 0

	def check(self):
		def get_interval():
			if self.status == 1:
				return 5
			else:
				return self.interval

		r = self.get()
		if r != 200:
			self.status += 1
			if self.status == 2:
				self.alert()
			else:
				self.report()
		else:
			self.clear()
			self.report()

		self.set_next_time(get_interval())

	def set_next_time(self, interval):
		self.time_for_next = time.time() + interval

	def alert(self):
		for sucker in self.suckers:
			sucker.sms(self.url, self.last_response, "down")

	def alert_up(self):
		for sucker in self.suckers:
			sucker.sms(self.url, self.last_response, "up")

	def report(self):
		print self.url + ": " + str(self.last_response)

	def run(self):
		if time.time() > self.time_for_next:
			self.check()
			print self.url + ": next check in " + str(self.time_for_next - time.time()) + " seconds"
