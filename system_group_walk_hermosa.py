# Imports
from snmp_library import *
from pysnmp.hlapi.asyncore import *


# Variables in my program
version = 'v1'
community = 'public'
ip_addr = '155.210.157.202'
port = 161


def snmpwalk(varbinds):

    response = snmp_engine.snmpgetnext(varbinds)
    maskVar = tuple(varbinds[0][0])
    while maskVar[len(maskVar)-1] >= tuple(response.varBinds[0][0])[len(maskVar)-1]:
        print([maskVar[len(maskVar)-1], tuple(response.varBinds[0][0])[len(maskVar)-1]])
        print(response.varBinds[0])
        response = snmp_engine.snmpgetnext(response.varBinds)

snmp_engine = snmp_requests(version, community, ip_addr, port)

varBinds1 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2'))]
snmpwalk(varBinds1)
