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
print('Ha habido un error ' + str(status) + '  en la peticion ' + str(index))
#Bucle maravilloso para sacar todos los varbind por pantalla
# for x in range(0,6):
#     print response.varBinds[x]
#     print tools().var_type(response.varBinds[x][1])

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
elapsed = time.time() - t
print 'Total execution time: ' + str(elapsed) + ' seconds'