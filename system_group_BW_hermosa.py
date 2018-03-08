# Imports
from snmp_library import *
from pysnmp.hlapi.asyncore import *


# Variables in my program
version = 'v1'
community = 'public'
ip_addr = '155.210.157.27'
port = 161


snmp_engine = snmp_requests(version, community, ip_addr, port)

varBinds1 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10'))]
response = snmp_engine.snmpgetnext(varBinds1)
maskVar = tuple(response.varBinds[0][0])
while maskVar[len(maskVar)-2] >= tuple(response.varBinds[0][0])[len(maskVar)-2]:
    oldresponde = response
    response = snmp_engine.snmpgetnext(response.varBinds)
response = snmp_engine.snmpget(oldresponde.varBinds)
print(response.varBinds[0])
#snmpwalk(varBinds1)
