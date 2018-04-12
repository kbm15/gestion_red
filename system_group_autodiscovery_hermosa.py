from snmp_library import *
from pysnmp.hlapi.asyncore import *
from scapy.all import *



# Conf verb to 0
conf.verb = 0

version = 'v1'
community = 'public'
port = 161

# Check the network
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = '155.210.157.0/24'), timeout = 2)
varBinds = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0'))]


# Para cada una de las repuestas snd y rcv son el paquete que has mandado y la respuesta que has recivido
for snd, rcv in ans:
    print(rcv.sprintf(r"%Ether.src% - %ARP.psrc%"))
    ip_addr =  str(rcv.ARP.psrc)
    snmp_engine = snmp_requests(version, community, ip_addr, port)
    response = snmp_engine.snmpget(varBinds)
# ans, unans = sr(IP(dst="155.210.157.0/24")/UDP(sport=RandShort(),dport=161)/SNMP(community='public',version=["v1"],PDU=SNMPget(varbindlist=SNMPvarbind(oid="1.3.6.1.2.1.1.1.0"))), timeout = 2)
#
# for snd, rcv in ans:
#
#     print(rcv.sprintf(r"%SNMP.src% - %IP.src%"))