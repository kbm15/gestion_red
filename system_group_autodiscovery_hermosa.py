# Network discovery
from scapy.all import *
from snmp_library import *


# Conf verb to 0
conf.verb = 0

# Check the network
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = '155.210.157.0/24'), timeout = 2)

# Para cada una de las repuestas snd y rcv son el paquete que has mandado y la respuesta que has recivido
for snd, rcv in ans:

    print(rcv.sprintf(r"%Ether.src% - %ARP.psrc%"))
    # Escaneo todos los puertos
    #answers, un_answered = sr()
    #
    #for req, resp in answers:
        # Compruebo si la respuesta es un SYN/ACK
        #pass # Pass solamente esta para llenar el loop. Tu lo deberas borrar


    # En caso de ser SYN/ACK cierro la conexion con un reset

ans, unans = srp (IP(dst="155.210.157.0/24")/UDP(sport=RandShort(),dport=161)/SNMP(community='public',version=["v2c","v1","v2"],PDU=SNMPget(varbindlist=SNMPvarbind(oid="1.3.6.1.2.1.1.1.0"))))

for snd, rcv in ans:

    print(rcv.sprintf(r"%SNMP.src% - %IP.src%"))