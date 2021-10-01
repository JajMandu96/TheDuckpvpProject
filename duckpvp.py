#!/usr/bin/python
# green= \033[1;32m
# red= \033[0;31m
#
#
#
#
import os
import sys

if not os.geteuid() == 0:
    sys.exit("""\e[92m you must run this programm as root!""")

print(""" \033[1;32m

██████╗░██╗░░░██╗░█████╗░██╗░░██╗██████╗░██╗░░░██╗██████╗░
██╔══██╗██║░░░██║██╔══██╗██║░██╔╝██╔══██╗██║░░░██║██╔══██╗
██║░░██║██║░░░██║██║░░╚═╝█████═╝░██████╔╝╚██╗░██╔╝██████╔╝
██║░░██║██║░░░██║██║░░██╗██╔═██╗░██╔═══╝░░╚████╔╝░██╔═══╝░
██████╔╝╚██████╔╝╚█████╔╝██║░╚██╗██║░░░░░░░╚██╔╝░░██║░░░░░
╚═════╝░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░    \033[1;m""")

def main():

	print("\033[1;32m [\033[0;31m**\033[1;m] starting...\033[1;m")

	print("""\033[1;32m
TheDuckpvpProject by Canarddu38
try help for more info...\033[1;m
""")
	system0 = raw_input("\033[0;31m>>> \033[1;m")
	if system0 == "help":
		print("...")
		install = os.system("apt-get update && apt-get install -y nmap hping3 build-essential python-pip ruby-dev git libpcap-dev libgmp3-dev && pip install tabulate terminaltables")


	else:
		print("Please select the option 1 or 2")
		main()
	return()
main()
