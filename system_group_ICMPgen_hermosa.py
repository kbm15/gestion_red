
from scapy.all import *

conf.verb = 0

print 'Empezamos los pings'
t = time.time()
# Inicializamos los valores y empezamos a pingear
for x in range(0, 100):
    send(IP(dst="155.210.157.202", ttl=20)/ICMP())
elapsed1 = time.time() - t

print 'Total execution time: ' + str(elapsed1) + ' seconds'