import os
import subprocess
import getpass
import signal

####################### ctrl + c signal block ########################
def lw(x,y):
	print("\ngoodbye,  see u next time")
	exit()
signal.signal(2 , lw)

#################################################
 
os.system("tput setaf 1")
print("\t\twelcome to my tools!")

os.system("tput setaf 0")

print ("\t\t-----------------------")

apassword = "lw"

print("Enter your password : ", end = ' ')
password = getpass.getpass("Enter tyour password")

if apassword != password:
	print("U are not authorised")
	exit()

print("""
press 1 : to install JDK
press 2 : to install Hadoop
press 3 : to start Namenode
press 4 : to start datanode
press 5 : to exit""")

print("Enter your choice")
ch=input()
print("You have selected",ch)

if int(ch) == 1:
	x = subprocess.getstatusoutput("rpm -q /root//Desktop/jdk-8u171-linux-x64.rpm")
	exitcode = x[0]
	cmdoutput = x[1]
	if exitcode == 0:
		print(cmdoutput)
	else:
		print("Already Installed")


elif int(ch) == 2:
	y = subprocess.getstatusoutput("rpm -i /root/Desktop/hadoop-1.2.1-1.x86_64.rpm")
	exitcode1 = y[0]
	cmdoutput1 = y[1]
	if exitcode1 == 0:
		print(cmdoutput1)
	else:
		print("Already Installed")

elif int(ch) == 3:
	subprocess.getstatusoutput("iptables -F")
	subprocess.getstatusoutput("hadoop-daemon.sh start Namenode")
	print("Namenode created")

elif int(ch) == 4:
	subprocess.getstatusoutput("iptables -F")
	subprocess.getstatusoutput("hadoop-daemon.sh start datanode")
	print("Datanode created")

else:
	print("don't support")


	 

