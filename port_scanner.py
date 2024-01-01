import socket
import termcolor



def scan(ip_addr, ports):
    print(termcolor.colored('\nStarted Scanning For ' + str(ip_addr), 'red', attrs=['bold', 'underline']))
    for port in range(1, ports + 1):
        port_scan(ip_addr, port)

def port_scan(ip_addr, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip_addr, port))
        print(termcolor.colored("[+] Port opened: " + str(port), 'green'))
        sock.close()
    except socket.error:
        pass

print(termcolor.colored("Welcome to the CrypticEnigmaX Port Scanner!", 'cyan', attrs=['bold']))
print(termcolor.colored("This tool is developed by CrypticEnigmaX for scanning ports.", 'cyan'))

targets = input("Enter the targets you want to scan [split by ,]: ")
ports = int(input("Enter the number of ports: "))

if ',' in targets:
    print(termcolor.colored("Scanning Multiple Targets...", 'red', attrs=['bold', 'underline']))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets, ports)
