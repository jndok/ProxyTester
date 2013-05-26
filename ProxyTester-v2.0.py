#########################################################################################
# ,------.                                 ,--------.              ,--.                 #
# |  .--. ',--.--. ,---.,--.  ,--.,--. ,--.'--.  .--',---.  ,---.,-'  '-. ,---. ,--.--. #
# |  '--' ||  .--'| .-. |\  `'  /  \  '  /    |  |  | .-. :(  .-''-.  .-'| .-. :|  .--' #
# |  | --' |  |   ' '-' '/  /.  \   \   '     |  |  \   --..-'  `) |  |  \   --.|  |    #
# `--'     `--'    `---''--'  '--'.-'  /      `--'   `----'`----'  `--'   `----'`--'    #
#                                 `---'                                        --V 2.0  #
# * Coded by jndok, 2013. Released under GNU/GPLv3.                                     #
#                                                                                       #
#                                                                                       #
# ProxyTester v.2.0 - Python script to check proxies status.                            #
#    Copyright (C) 2013  jndok                                                          #
#                                                                                       #
#    This program is free software: you can redistribute it and/or modify               #
#    it under the terms of the GNU General Public License as published by               #
#    the Free Software Foundation, either version 3 of the License, or                  #
#    (at your option) any later version.                                                #
#                                                                                       #
#    This program is distributed in the hope that it will be useful,                    #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                     #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                      #
#    GNU General Public License for more details.                                       #
#                                                                                       #
#    You should have received a copy of the GNU General Public License                  #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.              #
#                                                                                       #
# ------------------------------------------------------------------------------------- #
#                                                                                       #
# Please report any bugs at: jndok@live.com | I need your help to improve ProxyTester!  #
#                                                                                       #
# ------------------------------------------------------------------------------------- #
#                                                                                       #
# Changelog: http://wp.me/P2U9gI-I                                                      #
#                                                                                       #
#########################################################################################

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#                                                             #
# Need free SOCKS proxies? Check this out: http://cur.lv/xt06 #
#                                                             #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


import urllib2
import string
import sys
import time
import argparse
import re

VERSION = "2.0"

def msm(list_file, time_out, out_file):

	try:
		p = re.compile("\d+\.\d+\.\d+\.\d+:\d+")
		f = open(list_file, "r")
		content = f.read()
		tmp_proxy_array = re.sub(' ', '', str(content))
		proxy_array = p.findall(tmp_proxy_array)
	except:
		print "[!] List file not found!"
		sys.exit(1);


	status_array = range(len(proxy_array))

	print "\n# USING MULTIPLE SCAN MODE #\n"

	print "\n[+] Checking proxies status..."
	print "[+] Timeout is set to " + str(time_out) + "...\n"

	scan_file = open(out_file, 'w')

	for prox in range(len(proxy_array)):

		print "########################################################\n"
		print "[+] Trying proxy " + proxy_array[prox]

		localtime = time.asctime(time.localtime(time.time()))
		proxies = {"http":"http://%s" % proxy_array[prox]}
		url = "http://www.google.com/"
		headers = {'User-agent' : 'Googlebot/2.1'} # Tricks the website, make it believe that Googlebot is scanning the site.

		proxy_support = urllib2.ProxyHandler(proxies)
		opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
		urllib2.install_opener(opener)

		try:

			u = urllib2.urlopen(url, timeout=time_out) # Test the proxy, with a timeout of n seconds.
			print "\n### PROXY IS ALIVE! ###\n"
			print "[+] The proxy is alive and is working correctly.\n"

			status_array[prox] = "ALIVE"

		except: # If the connection gets no response;

			print "\n### PROXY IS DEAD! ###\n"
			print "[!] The proxy is dead, otherwise is not a valid proxy.\n"

			status_array[prox] = "DEAD"

		scan_file.write(proxy_array[prox].rstrip() + "\t[" + status_array[prox] + "] {LAST CHECK: " + localtime + "}\n")

	print "########################################################\n"
	print "[+] PROXIES COMPLESSIVE STATUS: [" + ' | '.join(status_array) + "]"
	print "[+] Output saved to '" + out_file + "'.\n"

	scan_file.close()
	sys.exit(0)

def cmd_ssm(address, port, time_out):

	print "\n# USING SINGLE SCAN MODE #\n"

	proxy = address + ":" + port

	print "\n[+] Checking proxy status..."
	print "[+] Timeout is set to " + str(time_out) + "...\n"

	proxies = {"http":"http://%s" % proxy}
	url = "http://www.google.com/"
	headers = {'User-agent' : 'Googlebot/2.1'} # Tricks the website, make it believe that Googlebot is scanning the site.

	proxy_support = urllib2.ProxyHandler(proxies)
	opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
	urllib2.install_opener(opener)

	try:

		u = urllib2.urlopen(url, timeout=time_out)
		print "\n### PROXY IS ALIVE! ###\n"
		print "[+] The proxy is alive and is working correctly.\n"

	except: # If the connection gets no response;

		print "\n### PROXY IS DEAD! ###\n"
		print "[!] The proxy is dead, otherwise is not a valid proxy.\n"

def ssm():

	print "\n# USING SINGLE SCAN MODE #\n"

	proxy = raw_input("[+] Please enter an IP-Port combination, divided by a colon (Ex. 142.23.37.12:8080): ") # Gets the IP-Port combination.

	print "\n[+] Checking proxy status..."
	print "[+] Timeout is set to 10...\n"

	proxies = {"http":"http://%s" % proxy}
	url = "http://www.google.com/"
	headers = {'User-agent' : 'Googlebot/2.1'} # Tricks the website, make it believe that Googlebot is scanning the site.

	proxy_support = urllib2.ProxyHandler(proxies)
	opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
	urllib2.install_opener(opener)

	try:

		u = urllib2.urlopen(url, timeout=10)
		print "\n### PROXY IS ALIVE! ###\n"
		print "[+] The proxy is alive and is working correctly.\n"

	except: # If the connection gets no response;

		print "\n### PROXY IS DEAD! ###\n"
		print "[!] The proxy is dead, otherwise is not a valid proxy.\n"

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--mode", help="| The scanning mode.")
	parser.add_argument("-f", "--file", help="| The txt list file.")
	parser.add_argument("-a", "--address", help="| The proxy's IP.")
	parser.add_argument("-p", "--port", help="| The proxy's port.")
	parser.add_argument("-t", "--timeout", type=int, help="| The connection's response timeout. Default is 10.")
	parser.add_argument("-o", "--output", help="| The output file's name.")
	args = parser.parse_args()

	if args.mode == None:
		if args.address == None and args.port == None and args.file == None and args.timeout == None and args.output == None:
			pass
		elif args.address != None or args.port != None or args.file != None:
			print parser.print_help()
			sys.exit(1)
	elif args.mode == "msm":
		if args.file != None and args.address == None and args.port == None:
			if args.timeout != None and args.output == None:
				msm(args.file, args.timeout, "scan_file.txt")
				sys.exit(0)
			elif args.timeout == None and args.output != None:
				msm(args.file, 10, args.output)
				sys.exit(0)
			elif args.timeout != None and args.output != None:
				msm(args.file, args.timeout, args.output)
				sys.exit(0)
			elif args.timeout == None and args.output == None:
				msm(args.file, 10, "scan_file.txt")
				sys.exit(0)
		else:
			print parser.print_help()
			sys.exit(1)
	elif args.mode == "ssm":
		if args.address != None and args.port != None and args.file == None:
			if args.timeout != None:
				cmd_ssm(args.address, args.port, args.timeout)
				sys.exit(0)
			elif args.timeout == None:
				cmd_ssm(args.address, args.port, 10)
				sys.exit(0)
		else:
			print parser.print_help()
			sys.exit(1)


	print "\n[*] ProxyTester v. " + str(VERSION) + " initialized."

	_input = raw_input("[+] Do you want to use multiple-scan mode(MSM) or single-scan mode(SSM): ")

	if _input == "msm":
		msm("list.txt");
	elif _input == "ssm":
		ssm();
	else:
		print "[!] Invalid input! Program will now terminate."
		sys.exit(0)

if __name__ == "__main__":
	main() 