#!/usr/bin/python
#  -*- coding: utf-8 -*-
#  coded by @magic_coding (icoder@mail.com)
#  Twitter: @magic_coding

import json
import urllib
import urllib2
import time
import simplejson
import webbrowser
import os
import sys

"""
VirusTotal Public API:
Learn more how to get VirusTotal API (https://www.virustotal.com/en/documentation/public-api/)
"""
Api_Key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def progressbar(it, prefix="", size=60):
	count = len(it)
	def _show(_i):
		x = int(size*_i/count)
		sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
		sys.stdout.flush()

	_show(0)
	for i, item in enumerate(it):
		yield item
		_show(i+1)
	sys.stdout.write("\n")
	sys.stdout.flush()

def scanurl():
	get_link = raw_input("Link to scan: ")
	url = "https://www.virustotal.com/vtapi/v2/url/report"
	parameters = {"resource": get_link,"apikey": Api_Key}
	data = urllib.urlencode(parameters)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	json = response.read()
	response_dict = simplejson.loads(json)
	scan_id = response_dict.get("scan_id")
	link = response_dict.get("url")
	response_code = response_dict.get("response_code")
	scan_date = response_dict.get("scan_date")
	analysis = response_dict.get("permalink")
	Positives = response_dict.get("Positives")
	total = response_dict.get("total")
	for i in progressbar(range(15), "Scanning: ", 40):
		time.sleep(0.7)
	if response_code==1:
		cls()
		print """   ______                __   _       __           __   __
  / ____/___  ____  ____/ /  | |     / /___  _____/ /__/ /
 / / __/ __ \/ __ \/ __  /   | | /| / / __ \/ ___/ //_/ / 
/ /_/ / /_/ / /_/ / /_/ /    | |/ |/ / /_/ / /  / ,< /_/  
\____/\____/\____/\__,_/     |__/|__/\____/_/  /_/|_(_)\n"""
		print "Scan finished, Check your scan information bellow:\n"
		# print "|Scan ID: "+scan_id
		print "|Link: "+link
		print "|Scan Date: "+scan_date
		print "|Scan report url: "+analysis
		print "|Scanner: "+str(total)+ " Scanner."
		print "|Positives: "+str(Positives)
		again = raw_input("\nOpen report link in browser? (y/n): ")
		if again=="y":
			webbrowser.open(analysis)
		else:
			pass
	else:
		enter = raw_input("[!] There is error. Please try again..[Press Enter]")

def cls():
	os.system('cls' if os.name=='nt' else 'clear')


def info():
	cls()
	print """   __  ______  __       _____                                 
  / / / / __ \/ /      / ___/_________ _____  ____  ___  _____
 / / / / /_/ / /       \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
/ /_/ / _, _/ /___    ___/ / /__/ /_/ / / / / / / /  __/ /    
\____/_/ |_/_____/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/\n"""
	print """This program coded by Mahmoud Al-nafei (www.twitter.com/magic_coding)
with Python language and it's free for use.
You can get this programe as open source from my Github account:
www.github.com/magic-coding

Enjoy..
-----
For Help: @magic_coding
	"""
	Enter = raw_input("press (Enter) to go back..")
	if Enter:
		pass

while True:
	cls()
	print """   __  ______  __       _____                                 
  / / / / __ \/ /      / ___/_________ _____  ____  ___  _____
 / / / / /_/ / /       \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
/ /_/ / _, _/ /___    ___/ / /__/ /_/ / / / / / / /  __/ /    
\____/_/ |_/_____/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                                                              
Scan any url using more than 60 scanner from (virustotal).
Credit @magic_coding (www.twitter.com/magic_coding)\n
-------------------------\n"""
	print "1- Scan url with (VirusTotal)"
	print "2- about"
	print "3- Exit System"
	try:
		decision = raw_input("Please select a number: ")
		if decision.isdigit() == True:
			if(int(decision) == 1):
				scanurl()
			elif(int(decision) == 2):
				info()
			elif(int(decision) == 3):
				cls()
				print """  ________                __                       
 /_  __/ /_  ____ _____  / /__   __  ______  __  __
  / / / __ \/ __ `/ __ \/ //_/  / / / / __ \/ / / /
 / / / / / / /_/ / / / / ,<    / /_/ / /_/ / /_/ / 
/_/ /_/ /_/\__,_/_/ /_/_/|_|   \__, /\____/\__,_/  
                              /____/\n"""
				print "program exit.."
				print "Thank you for using URL Scanner by @magic_coding"
				exit()
			else:
				print "Error"
		else:
			print "[!] Please enter number not string."
			time.sleep(2)
	except KeyboardInterrupt:
		print "\nprogram exit.."
		print "See you again."
		exit()
