
from scapy.all import *

# Conf verb to 0
conf.verb = 0

print 'Empezamos los pings'
t = time.time()
# Check the network
for x in range(0, 100):
    send(IP(dst="155.210.157.202", ttl=20)/ICMP())
elapsed1 = time.time() - t

print 'Total execution time: ' + str(elapsed1) + ' seconds'