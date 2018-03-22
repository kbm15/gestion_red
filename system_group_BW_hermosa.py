# Imports
from snmp_library import *
from pysnmp.hlapi.asyncore import *


# Variables in my program
version = 'v1'
community = 'public'
ip_addr = '155.210.157.27' #ip de un hub
port = 161


snmp_engine = snmp_requests(version, community, ip_addr, port)

varBinds1 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2'))]
response = snmp_engine.snmpgetnext(varBinds1)
#generamos una mascara, asi he diseñado el walk
maskVar = tuple(response.varBinds[0][0])

#Recorremos toda la tabla de interfaces y mostramos el ancho de banda cursado
while maskVar[len(maskVar)-2] >= tuple(response.varBinds[0][0])[len(maskVar)-2]:
    oldresponse = response
    currInst = tuple(response.varBinds[0][0])[len(maskVar)-1] #Salvamos el indice
    varBindsIn = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.' + str(currInst)))]
    responseIn = snmp_engine.snmpget(varBindsIn)
    inOctects = responseIn.varBinds[0][1] #Guardamos los octetos que entran
    varBindsOut = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.16.' + str(currInst)))]
    responseOut = snmp_engine.snmpget(varBindsOut)
    OutOctects = responseOut.varBinds[0][1]  #Guardamos los octetos que salen
    time.sleep(5) #Esperamos para que se curse trafico
    varBindsIn = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.' + str(currInst)))]
    responseIn = snmp_engine.snmpget(varBindsIn)
    inOctects = responseIn.varBinds[0][1] - inOctects #Calculamos la diferencia
    varBindsOut = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.16.' + str(currInst)))]
    responseOut = snmp_engine.snmpget(varBindsOut)
    OutOctects = responseOut.varBinds[0][1] - OutOctects #Calculamos la diferencia
    print(response.varBinds[0][1])
    print('Trafico entrante (b/s): ' +  str(inOctects/5))
    print('Trafico saliente (b/s): ' + str(OutOctects/5))
    response = snmp_engine.snmpgetnext(oldresponse.varBinds)

