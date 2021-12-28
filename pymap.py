import socket
import timeit
import concurrent.futures
import sys
import re
from tqdm import tqdm

if len(sys.argv) < 4:
    print("Correct format: pymap.py {IP/URI} {First Port To Scan} {Last Port To Scan} {Num of Threads to use}")
    sys.exit()

start = timeit.default_timer()
ip = sys.argv[1]
# in case the argument given is a URI
if re.search('[a-zA-Z]', ip) is not None:
    ip = socket.gethostbyname(ip)

startPort = int(sys.argv[2])
endPort = int(sys.argv[3])
numThreads = int(sys.argv[4])
open_ports = []

def tryPort(portValue):
    try:
        s = socket.socket()
        # connect socket to ip and port
        s.connect((ip, portValue))
        open_ports.append(portValue)
        s.close()

    except:
        pass


print("Scanning host", ip + "...")
threads = min(numThreads, endPort-startPort)
array = range(startPort, endPort)
# distribute the ports between all the available threads
with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    list(tqdm(executor.map(tryPort, array), total=endPort))

open_ports.sort()

for portValue in open_ports:
    if portValue == 21:
        print("[+]Port", portValue, "open | FTP")
    elif portValue == 22:
        print("[+]Port", portValue, "open | SSH")
    elif portValue == 23:
        print("[+]Port", portValue, "open | Telnet")
    elif portValue == 25:
        print("[+]Port", portValue, "open | SMTP")
    elif portValue == 53:
        print("[+]Port", portValue, "open | DNS")
    elif portValue == 80:
        print("[+]Port", portValue, "open | HTTP")
    elif portValue == 88:
        print("[+]Port", portValue, "open | Kerberos")
    elif portValue == 110:
        print("[+]Port", portValue, "open | POP3")
    elif portValue == 139:
        print("[+]Port", portValue, "open | netbios-ssn")
    elif portValue == 389:
        print("[+]Port", portValue, "open | LDAP")
    elif portValue == 443:
        print("[+]Port", portValue, "open | HTTPS")
    elif portValue == 636:
        print("[+]Port", portValue, "open | LDAPS")
    elif portValue == 992:
        print("[+]Port", portValue, "open | TelnetS")
    elif portValue == 3306:
        print("[+]Port", portValue, "open | mySQL")
    elif portValue == 8080:
        print("[+]Port", portValue, "open | Web App")
    else:
        print("[+]Port", portValue, "open")

stop = timeit.default_timer()
print('Total runtime: ', stop - start, 'seconds')
