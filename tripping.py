from website import Website
from sucker import Sucker
import time

interval = 10

jesse = Sucker("Jesse", "sejje@sejje.net", "5015451677")
david = Sucker("David", "david.dewhirst@threetwelvecreative.com", "239XXXXXXX")

suckers = [jesse, david]

urls = ["http://sejje.net/", "http://jessebriggs.net/superduperman"]

websites = []
for url in urls:
	websites.append(Website(url, interval, suckers))

w = Website(urls[0], interval, suckers)

while True:
	for site in websites:
		site.run()
	time.sleep(.001)

