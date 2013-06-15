from website import Website
from sucker import Sucker
import time

interval = 600

jesse = Sucker("Jesse", "sejje@sejje.net", "501XXXXXXX")

suckers = [jesse]

urls = ["http://www.google.com/", "http://ebay.com/"]

websites = []
for url in urls:
	websites.append(Website(url, interval, suckers))

w = Website(urls[0], interval, suckers)

while True:
	for site in websites:
		site.run()
	time.sleep(.001)

