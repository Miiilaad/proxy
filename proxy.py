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
print "Github   : https://github.com/siruidos/"
print

try:
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	res = br.open('http://pubproxy.com/api/proxy').read()
	js = json.loads(res)
	for i in js.keys():
		if i == "data":
			print green,i," : ",tur,js[i],end
		else:
			print green,i,": ",tur,js[i],end
	print
except:
	print red," [-] No Resoult!",end
	print
