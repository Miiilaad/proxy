#!/usr/bin/env python
import mechanize, json, sys

red="\033[0;31m"
green="\033[0;32m"
yellow="\033[1;33m"
end="\033[1;37m"
tur="\033[0;36m"

logo = """\033[1;33m
  ____      _      ____
 / ___| ___| |_   |  _ \ _ __ _____  ___   _
| |  _ / _ \ __|  | |_) | '__/ _ \ \/ / | | |
| |_| |  __/ |_   |  __/| | | (_) >  <| |_| |
 \____|\___|\__|  |_|   |_|  \___/_/\_\\__, |
                                       |___/
\033[1;37m"""
print
print logo
print
print "Developer: Sir.uidops"
print "E-mail   : Sir.u1d0p5@gmail.com"
print "Telegram : https://t.me/Sir_uidops"
print "Github   : https://github.com/siruidops"
print

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
res = br.open('http://pubproxy.com/api/proxy').read()
js = json.loads(res)
for i in js.keys():
	if i == "data":
		for j in js[i]:
			data = j.iteritems()
			for c,d in data:
				if c == 'support':
					sup = d.iteritems()
					for k,o in sup:
						print green,k,': ',o,end
					continue
				print green,c,': ',d,end
	else:
		print green,i,": ",tur,js[i],end
print
