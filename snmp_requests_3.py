# Imports
from snmp_library import *
from pysnmp.hlapi.asyncore import *
import time


# Variables in my program
version = 'v1'
community = 'public'
ip_addr = '155.210.157.202'
port = 161

# SNMP engine inicialization
snmp_engine = snmp_requests(version, community, ip_addr, port)


#######################################################################
#                            SNMP GET                                 #
#######################################################################

varBinds1 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))
varBinds2 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.2.0'))
varBinds3 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0'))
varBinds4 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.4.0'))
varBinds5 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'))
varBinds6 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0'))
varBinds7 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.8.0'))

#Conseguimos ahorrar tiempo equivalente al numero de peticiones si las pedimos todas de golpe
varBinds = [varBinds1, varBinds2, varBinds3, varBinds4, varBinds5, varBinds6, varBinds7]

t = time.time()

# Send request
response = snmp_engine.snmpget(varBinds)
status = response.errorStatus
index = response.errorIndex
print('Ha habido un error ' + str(status) + ' en la peticion ' + str(index))

# ending time counter
elapsed = time.time() - t
print 'Total execution time: ' + str(elapsed) + ' seconds'