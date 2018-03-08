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

varBinds1 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))]
varBinds2 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.2.0'))]
varBinds3 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0'))]
varBinds4 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.4.0'))]
varBinds5 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'))]
varBinds6 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0'))]
varBinds7 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.7.0'))]

print 'Pedimos cada cosa por separado'
t = time.time()

# Send request
response = snmp_engine.snmpget(varBinds1)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
response = snmp_engine.snmpget(varBinds2)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]

response = snmp_engine.snmpget(varBinds3)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
response = snmp_engine.snmpget(varBinds4)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
response = snmp_engine.snmpget(varBinds5)
if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    print response.varBinds[0]
response = snmp_engine.snmpget(varBinds6)
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

# Parte 2
for x in range(0,6):
    print('#')
print 'Pedimos ahora todo de golpe'
varBinds1 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'))
varBinds2 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.2.0'))
varBinds3 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0'))
varBinds4 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.4.0'))
varBinds5 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'))
varBinds6 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0'))
varBinds7 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.7.0'))
varBinds = [varBinds1, varBinds2, varBinds3, varBinds4, varBinds5, varBinds6, varBinds7]

t = time.time()

# Send request
response = snmp_engine.snmpget(varBinds)

if response.errorIndication:
    print 'errorIndication'
elif response.errorStatus:
    print 'errorStatus'
else:
    #Bucle maravilloso para sacar todos los varbind por pantalla
    for x in range(0,6):
        print response.varBinds[x]
        print tools().var_type(response.varBinds[x][1])

    # print response.varBinds[1]
    # print tools().var_type(response.varBinds[1][0])
    # print response.varBinds[2]
    # print tools().var_type(response.varBinds[2][0])
    # print response.varBinds[3]
    # print tools().var_type(response.varBinds[3][0])
    # print response.varBinds[4]
    # print tools().var_type(response.varBinds[4][0])
    # print response.varBinds[5]
    # print tools().var_type(response.varBinds[5][0])
    # print response.varBinds[6]
    # print tools().var_type(response.varBinds[0][0])

# ending time counter
elapsed2 = time.time() - t
print 'Total execution time: ' + str(elapsed2) + ' seconds'

print 'Es ' + str(elapsed1/elapsed2) + ' veces mas rapido!'
print 'Wow'
print 'Such speed'


for x in range(0,6):
    print('#')

print 'Ahora va a haber un error, veamos de que tipo es'
varBinds7 = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.8.0'))

#Conseguimos ahorrar tiempo equivalente al numero de peticiones si las pedimos todas de golpe
varBinds = [varBinds1, varBinds2, varBinds3, varBinds4, varBinds5, varBinds6, varBinds7]

t = time.time()

# Send request
response = snmp_engine.snmpget(varBinds)
status = response.errorStatus
index = response.errorIndex
print('Ha habido un error ' + str(status) + '  en la peticion ' + str(index))
