import socket
from IPy import IP


def scan(target):
	converted_ip = check_ip(target)
	print('\n' + '[_0 Scanning Target] ' + str(target))
	for port in range(21, 80):
		scan_port(converted_ip, port)

def check_ip(ip):
	try:
		IP(ip)
		return ip
	except ValueError:
		return socket.gethostbyname(ip)

def get_banner(s):
	return s.recv(1024)

def scan_port(ip_address, port):
	try:
		sock = socket.socket()
		sock.settimeout(0.5)  # decreases accuracy but also speeds up the scan
		sock.connect((ip_address, port))
		try:
			banner = get_banner(sock)
			print('[+] Open Port ' + str(port) + ' : ' + ' Banner: ' + str(banner.decode().strip('\n')))
		except:
			print('[+] Open Port ' + str(port))
	except:
		pass

if __name__ == "__main__":  # will only run if the main program is run, not from an imported file
	targets = input('[+] Enter a Target/s To Scan(split multiple targets with ,): ')
	if ',' in targets:
		for ip_add in targets.split(','):
			scan(ip_add.strip(' '))
	else:
		scan(targets)
