#!/usr/bin/python
# Usage: ./gencreds_aztekbtc.py 
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

def populatePassphraseToConf(kpPass): 
	kpPass = kpPass.strip()

def getProps(targetPass): 
	with open("keyconf.properties", "r") as propsFile: 
		tempConfProps = open("tempkeyconf.properties", "w") 
		for line in propsFile: 
			if "PASSPHRASE" in line: 
				theStr = "Passphrase: " + targetPass + "\n"
				tempConfProps.write(theStr)
			else: 
				tempConfProps.write(line) 
		tempConfProps.close()

def getNewKeyPairID(gpg): 
	keyList = gpg.list_keys()
	if len(keyList) == 1: 
		newKey = keyList[0]
	else: 
		newKey = keyList[len(keyList)]
	return newKey
	# print keyList[len(keyList)]

if __name__ == "__main__": 
	kpPass = sys.argv[1] 
	gpg = gnupg.GPG(homedir=str(os.environ["HOME"]) + "/.gnupg")
	getProps(kpPass.strip())
	print ("Generating your cryptographically secure keypair, please generate random activity to generate atrophy...")
	print ("This process may take a minute or so...") 
	with open("tempkeyconf.properties") as tempFile: 
		createKey = gpg.gen_key(tempFile.read())
		print createKey
	# out = subprocess.Popen(['gpg', '--gen-key', '--batch', 'tempkeyconf.properties'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
	# # print theCall.stderr
	# if theCall.returncode == None: 
	# 	theOutput = str(theCall.stdout.read())
	print "Key generated successfully"
	# newKey = getNewKeyPairID(gpg)
	print "CREATED NEW KEY: " + str(createKey)
	with open("TARGET_SIGNING_KEY.txt", "w") as theSigningFile: 
		theSigningFile.write(str(createKey))
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




