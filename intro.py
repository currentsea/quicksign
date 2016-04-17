#!/usr/bin/python
# Created for btcdata.org founding members for automation security improvement :)
VERSION="0.0.1-ALPHA"
MAINTAINER="currentsea"
__author__ = "currentsea"
__license__ = "MIT" 

# The MIT License (MIT)
# Copyright (c) 2016 currentsea (admin@btcdata.org)
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import getpass
import subprocess
import gnupg
import os
import sys


def checkTrust(): 
	
	print("THIS SCRIPT IS COPYRIGHT currentsea & btcdata.org 2016") 
	answerValid = False
	while answerValid == False: 
		stdinData = raw_input("DO YOU PROMISE TO KEEP MY \"SECRET SAUCE\" CONFIDENTIAL & PROPRIETARY? (Yes/No): ")
		answer = stdinData.lower().strip()
		answerValid = answer == "yes" or answer == "no"
		if answerValid == True: 
			if answer == "yes": 
				print("Good.  Lets begin the generation of your encryption keypair.")
				print("Launching currentsea\'s awesome credential generation script now...") 
				return True
			else: 
				print("Thanks for your honesty.  You will not have any credentials generated for you today.") 
				exit(1) 
		else:
			print("Invalid answer.  Try again (please type the word yes or no entirely, y or n will not work).") 


if __name__ == "__main__": 
	if os.path.isfile("stdout.txt"): 
		os.remove("stdout.txt")
		print "Removed old stdout.txt file"
	checkTrust()
	print("btcdata_keypair_generator " + VERSION + "                      ")
	print("Copyright 2016  " + MAINTAINER + "                             ")
	print("Utilization of this application constitutes acceptance of the MIT License agreement located at the repository's root") 
	print("---> BEGINNING SECURE CREDENTIALS GENERATOR FOR btcdata.org ---") 
	print("      This script wasPackaged exclusively for Aztek_btc        ")
	print("            DO NOT EVER LOSE YOUR PRIVATE KEY.                 ") 
	print("           ONLY SIGN OTHER KEYS THAT YOU TRUST!                ") 
	print("     DO NOT LET THESE CREDENTIALS GET COMPROMISED              ")
	print("               FINALLY, DON'T BE EVIL.                         ")
	finalCheck = raw_input("DO YOU AGREE TO ALL OF THE ETHICAL, MORAL, AND INTELLECTUAL PROPERTY CONSIDERATIONS THAT WERE DESCRIBED ABOVE? (Yes/No): ") 
	finalCheck = finalCheck.lower().strip()
	if finalCheck == "yes": 
		print("Good.  I'm generating your keypair now...")
		# processOutput(err)
			# for line in theOutput.split("\n"): 
				# if "marked as ultimately trusted" in line: 
				# 	print line
				# 	print "YYYY"
		# theCall = subprocess.call(["sed", "-i", "\"s,__PASSPHRASE__," + kpPass + ",g\"", "keyconf.properties"])
			# os.remove("tempkeyconf.properties") 
			# importKeyChains()
			# print("Please save your *.pub and *.sec files somewhere safely.") 
			# print("Would you like t")




