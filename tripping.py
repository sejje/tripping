from website import Website
from sucker import Sucker
import time

interval = 10

jesse = Sucker("Jesse", "5015451677@text.att.net", "5015451677")
david = Sucker("David", "2393316539@messaging.sprintpcs.com", "2393316539")

suckers = [jesse]

urls = ["http://www.positionlogic.com/", "http://threetwelvecreative.com/", "http://aspg.com/", "http://mohhaiti.org/", "http://swflresourcelink.com/"]

websites = []
for url in urls:
	websites.append(Website(url, interval, suckers))

w = Website(urls[0], interval, suckers)

while True:
	for site in websites:
		site.run()
	time.sleep(.001)

