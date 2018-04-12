# Imports
from snmp_library import *
from pysnmp.hlapi.asyncore import *
import time

#Configuraciones SNMPs
version = 'v1'
community = 'private'
ip_addr = '155.210.157.202'
port = 161

# SNMP engine inicialization
snmp_engine = snmp_requests(version, community, ip_addr, port)

#######################################################################
#                            SNMP SET                                 #
#######################################################################
# Aqui configuramos el nombre
newName= 'BrokenHub'
print 'El nuevo nombre va a ser ' + newName
varBinds5 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'),OctetString(newName))]
response = snmp_engine.snmpset(varBinds5)

#######################################################################
#                            SNMP GET                                 #
#######################################################################
#Volvemos a configurarlo para que poder leer
community = 'public'
snmp_engine = snmp_requests(version, community, ip_addr, port)
varBinds5 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'))]
response = snmp_engine.snmpget(varBinds5)
print response.varBinds[0]