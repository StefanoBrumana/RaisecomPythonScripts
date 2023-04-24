# RaisecomPythonScripts
Python scripts for Raisecom devices

RaisecomMultiTelnet.py: interactive script to telnet multiple Raisecom devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, enter commands ( listed in the commands.txt file saved in the same folder of this script ) and save the entire log into a .txt file whose name is made by IP address of target device + date/time

RaisecomMultiSsh.py: interactive script to ssh multiple Raisecom devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, enter commands ( listed in commands.txt file that must be manually created in the same folder of this script ) and save the entire log into a .txt file whose name is made by IP address of target device + date/time

RaisecomMultiTftpUploadTelnet.py: to access via telnet to a list of Raisecom devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, export their startup-config to the root folder of a TFTP server ( all these activities are logged in a .txt file created in the same folder of the script )

RaisecomMultiTftpUploadSsh.py: to access via ssh to a list of Raisecom devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, export their startup-config to the root folder of a TFTP server ( all these activities are logged in a .txt file created in the same folder of the script )

If log file has empty lines they can be removed by Notepad++ ( my favourite free app to consult log files: it also has a compare plug-in to quickly locate differences )
