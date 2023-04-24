#python script version 0.3 December 2020 to access via telnet
#and export via tftp the startup-config from a list of Raisecom
#devices all with same username, password and optional enable password
#enter commands and send their startup-config to the root folder of a TFTP server
#tested in python 3.8.5 on windows 7 pro 64 bit with 3cDaemon TFTP server
#pip version 20.1.1
#ssh libraries: paramiko version 2.7.2, netmiko version 3.3.2
#import required python libraries to execute this script
import getpass
import sys
import telnetlib
import time
import socket
import os
import re
from datetime import datetime

#user is prompted to insert unique username and password of all the target devices
print ("#############################################################")
print ("Python script to export startup-config via TFTP from Raisecom")
print ("##########FaAndàIMan#########################################")
user=input("Enter Login: ")
password=getpass.getpass()
#ask if the target device has a privileged password to get administrator access
while ( answer:= input ("Has target device an enable password (Y/N)?").upper() ) not in {"Y", "N"}: pass
if answer == "Y":
 enable=input("Enter enable password: ")
#enter the ip address of the tftp server where startup-configs will be exported
tftp_server= input ("Type IP address of TFTP server: ")

#check that ip address of the tftp_server is properly typed by the end user
#in case of error the script will be immediately terminated
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
  25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
  25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
  25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
       
def check(tftp_server):
 if(re.search(regex, tftp_server)):  
  print("###############################################################")
  print("You entered a valid IP address")
  print("TFTP server MUST be running on such host")
  print("Its firewall or anti-virus should not discard any incoming file") 
  print("###############################################################")
 else:  
  print("###################################################################")
  print("ERROR: you entered an invalid IP address: script will be terminated") 
  print("Re-launch the script and type a correct IP address")  
  print("###################################################################")
  time.sleep(5)
  quit()
check(tftp_server)

print ("All operations logged into tftp-log.txt of your present folder")
time.sleep(2)

#all activities on screen will be saved into tftp-log.txt file created in
#the same folder of this script: any previous copy of tftp-log will be overwritten
stdout_fileno = sys.stdout
sys.stdout = open("tftp-log.txt","w")

#open file ip.txt to retrieve addresses of target devices
#this ip.txt file must be in same folder of this python script
iplist=open("ip.txt")

for line in iplist:
 Host=line.strip("\n")
 sys.stdout.write ("Working on device " + Host + "\n" )
 stdout_fileno.write ("Working on device " + Host + "\n" )
 #telnet performed on default TCP port 23
 try:
  tn = telnetlib.Telnet(Host,23)
  #following line must exactly match the prompt of the target device
  #telnet the target device to verify if its exact prompt is Login:
  #or Username: or user> or something else
  tn.read_until(b"Login:")
  tn.write(user.encode("ascii") + b"\n")
  #following line must exactly match the prompt of the target device
  #telnet the target device to verify if its exact prompt is Password:
  #or password: or password> or something else
  tn.read_until(b"Password:")
  tn.write(password.encode("ascii")+ b"\n")
  time.sleep(2)
  #script enters the enable command in telnet session to get privileged access
  #on the target device, next it will type the relevant enable password
  if answer == "Y":
   tn.write(b"enable\n")
   tn.write(enable.encode("ascii") + b"\n")
   time.sleep(2)
   #activities will be displayed both on screen and saved into tftp-log.txt file
   #created in the same folder of this script
  sys.stdout.write ("Exporting the startup-config..." + "\n")
  stdout_fileno.write ("Exporting the startup-config..." + "\n")
  #startup-config exported from the target device will be saved into the root
  #folder of the tftp server with an unique name startup-config_IPaddress_date/time
  #IP adddress is from the target device
  timestr = datetime.now().strftime("%m%d%Y-%H%M%S")
  config_file = "upload startup-config tftp " + tftp_server + " startup-config_" + Host + "_" + timestr
  tn.write(config_file.encode("ascii") + b"\n")
  time.sleep(5)
  #telnet session MUST be closed properly with an exit command otherwise log files will not be 
  #created or the telnet session will not work reliably
  tn.write(b"exit\n")
  sys.stdout.write ("End of operations on device " + Host + "\n")
  stdout_fileno.write ("End of operations on device " + Host + "\n")
  sys.stdout.write ("File is in root folder of TFTP server " + tftp_server + "\n") 
  stdout_fileno.write ("File is in root folder of TFTP server " + tftp_server + "\n")
  sys.stdout.write ("It is called startup-config_" + Host + "_" + timestr + "\n")
  stdout_fileno.write ("It is called startup-config_" + Host + "_" + timestr + "\n")
  tn.close()
 except IOError:
  sys.stdout.write ("Unable to reach via telnet device " + Host + "\n")
  stdout_fileno.write ("Unable to reach via telnet device " + Host + "\n")
  time.sleep(2)
  pass

iplist.close()

sys.stdout.write ("############# end of python script #############\n")
stdout_fileno.write ("############# end of python script #############\n")
sys.stdout.write ("All operations logged into tftp-log.txt of your present folder\n")
stdout_fileno.write ("All operations logged into tftp-log.txt of your present folder\n")
sys.stdout.write ("Log closed on " + timestr + "\n")
stdout_fileno.write ("Log closed on " + timestr + "\n")


sys.stdout.close()
sys.stdout = stdout_fileno
