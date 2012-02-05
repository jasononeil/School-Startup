#!/usr/bin/python
import sys
import os
import subprocess

# A simple function to launch a command
def runCommand(cmd):
	sys.stderr = sys.stdout
	args = cmd.split(" ")
	proc = error=subprocess.Popen(args, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	if sys.platform == "win32": 
		proc.communicate()[0].decode("windows-1252")
	else:
		proc.communicate()[0].decode("utf8")

	output = ""
	#for line in proc.stdout:
	#	output = output + "stdout: " + line.decode("windows-1252").rstrip() + "\n"
	#for line in proc.stderr:
	#	output = output + "stderr: " + line.decode("windows-1252").rstrip() + "\n"
	
	return_code = proc.wait()
	return return_code
	
	pass

# Some simple variables we can use
home = os.getenv('USERPROFILE') or os.getenv('HOME')
networkDir = home + "/NetworkDrives/"
pwsAppDir = home + "/.pws/"

# Launch commands depending on the platform...
if sys.platform == "linux2":
	runCommand("./update.sh " + pwsAppDir + "School-Startup")
	runCommand("./update.sh " + pwsAppDir + "School-Logon")
elif sys.platform == "win32": 
	pass
elif sys.platform == "darwin":
	runCommand("./update.sh " + pwsAppDir + "School-Startup")
	runCommand("./update.sh " + pwsAppDir + "School-Logon")