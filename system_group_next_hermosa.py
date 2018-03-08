# Imports
from snmp_library import *
from pysnmp.hlapi.asyncore import *
import time


# Variables in my program
version = 'v1'
community = 'public'
ip_addr = '192.168.3.4'
port = 161


# SNMP engine inicialization
snmp_engine = snmp_requests(version, community, ip_addr, port)


#######################################################################
#                            SNMP GET                                 #
#######################################################################

varBinds1 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.0.0'))]
varBinds2 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))]
varBinds3 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.2.0'))]
varBinds4 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0'))]
varBinds5 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.4.0'))]
varBinds6 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'))]
varBinds7 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0'))]

print 'Pedimos con getnext'
t = time.time()

# Send request
response = snmp_engine.snmpgetnext(varBinds1)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
response = snmp_engine.snmpgetnext(varBinds2)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]

response = snmp_engine.snmpgetnext(varBinds3)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
response = snmp_engine.snmpgetnext(varBinds4)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
response = snmp_engine.snmpgetnext(varBinds5)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
response = snmp_engine.snmpgetnext(varBinds6)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
response = snmp_engine.snmpget(varBinds7)

if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]

# ending time counter
elapsed1 = time.time() - t
print 'Total execution time: ' + str(elapsed1) + ' seconds'

t = time.time()

#Si usamos get normal

print 'Ahora con get'
# Send request
response = snmp_engine.snmpget(varBinds1)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
    print tools().var_type(response.varBinds[0])

response = snmp_engine.snmpget(varBinds2)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
    print tools().var_type(response.varBinds[0])

response = snmp_engine.snmpget(varBinds3)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
    print tools().var_type(response.varBinds[0])

response = snmp_engine.snmpget(varBinds4)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
    print tools().var_type(response.varBinds[0])

response = snmp_engine.snmpget(varBinds5)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
    print tools().var_type(response.varBinds[0])

response = snmp_engine.snmpget(varBinds6)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
    print tools().var_type(response.varBinds[0])

response = snmp_engine.snmpget(varBinds7)

if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
    print tools().var_type(response.varBinds[0])

# ending time counter
elapsed2 = time.time() - t
print 'Total execution time: ' + str(elapsed2) + ' seconds'

print 'Es ' + str(elapsed1/elapsed2) + ' veces mas rapido!'
print 'Wow'
print 'Such speed'