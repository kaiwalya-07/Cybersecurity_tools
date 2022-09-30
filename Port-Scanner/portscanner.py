
import pyfiglet
import socket
import termcolor


def scan(target, ports):
        print(termcolor.colored(('\n' + 'Starting scan for' + str(target)), 'red'))
        for port in range(1, ports):
             scan_port(target, port)




def scan_port(ipaddress, port):
   try:
       sock = socket.socket()
       sock.connect((ipaddress, port))
       print("[+] PORT is Open"+str(port))
       sock.close()
            
   except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
   except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
   except socket.error:
        print("\ Server not responding !!!!")
        sys.exit() 

        
logo = pyfiglet.figlet_format("PORT SCANNER")
print(logo)
        
targets = input("[*] Enter Target To scan split them by ,")
ports = int(input("[*] Enter how many ports to scan"))
if ',' in targets:
         print(termcolor.colored(("[*] Scanning multiple  target IPs"),'green'))
         for ip_addr in targets.split(','):
                                 scan(ip_addr.strip(' '), ports)
else:
        scan(targets, ports)
