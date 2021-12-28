import socket
import timeit
import concurrent.futures

start = timeit.default_timer()

def tryPort(portValue):
    try:
        s = socket.socket()
        s.connect(('45.33.32.156', portValue))
        print("[+]Port", portValue, "open")
        s.close()
    except:
        pass


stop = timeit.default_timer()
threads = 20
array = range(1,10000)
with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    list(executor.map(tryPort, array), total=10000)

print('Time: ', stop - start, 'seconds')


