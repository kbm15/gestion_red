# Imports
from snmp_library import *
from pysnmp.hlapi.asyncore import *
import time


# Variables in my program
version = 'v1'
community = 'private'
ip_addr = '192.168.3.4'
port = 161


# SNMP engine inicialization
snmp_engine = snmp_requests(version, community, ip_addr, port)


#######################################################################
#                            SNMP SET                                 #
#######################################################################
newName= 'potato'
print 'El nuevo nombre va a ser ' + newName
varBinds5 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'),OctetString('potato'))]
response = snmp_engine.snmpset(varBinds5)

community = 'public'
snmp_engine = snmp_requests(version, community, ip_addr, port)

varBinds5 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'))]

response = snmp_engine.snmpget(varBinds5)
print response.varBinds[0]