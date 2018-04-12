# Imports
from snmp_library import *
from pysnmp.hlapi.asyncore import *
import time
import numpy
from  matplotlib import pyplot


# Variables in my program
version = 'v1'
community = 'public'
ip_addr = '155.210.157.84' #ip de un hub
port = 161


snmp_engine = snmp_requests(version, community, ip_addr, port)

#Version oficial con plots de una sola interfaz, en este caso la 27 con ifDescr.141
t = time.time()
elapsed = time.time() - t
varBindsIn = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.4227626'))]
varBindsOut = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.16.4227626'))]
bwOut = []
bwIn = []
print('Comenzamos la medida de ancho de banda')

while time.time() - t <= 44:
    responseIn = snmp_engine.snmpget(varBindsIn)
    responseOut = snmp_engine.snmpget(varBindsOut)
    inOctects = responseIn.varBinds[0][1]  # Guardamos los octetos que entran
    outOctects = responseOut.varBinds[0][1]  # Guardamos los octetos que salen
    time.sleep(1) # Esperamos
    responseIn = snmp_engine.snmpget(varBindsIn) # Volvemos a pedir
    responseOut = snmp_engine.snmpget(varBindsOut)
    inOctects = responseIn.varBinds[0][1] - inOctects  # Calculamos la diferencia
    outOctects = responseOut.varBinds[0][1] - outOctects  # Calculamos la diferencia
    bwIn.append(int(inOctects))
    bwOut.append(int(outOctects))
seconds = numpy.arange(0, bwIn.__len__()*2 , 2) # El tiempo que tardan las peticiones es variable


pyplot.figure(1)
pyplot.subplot(211)
pyplot.plot(seconds, bwIn)
pyplot.ylabel('Bytes')
pyplot.title('Ancho de banda de entrada (b/s)')
pyplot.grid(True)

pyplot.subplot(212)
pyplot.plot(seconds, bwOut)
pyplot.ylabel('Bytes')
pyplot.title('Ancho de banda de salida (b/s)')
pyplot.grid(True)
pyplot.show()

# Si quisieramos monitorizar todas las interfaces EXTRA

varBinds1 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2'))]
response = snmp_engine.snmpgetnext(varBinds1)
#Hacemos un walk de la tabla de interfaces para encontrar el ethernet
maskVar = tuple(response.varBinds[0][0])
print('Monitorizacion ancho de banda del resto de interfaces')
#Recorremos toda la tabla de interfaces y mostramos el ancho de banda cursado
while maskVar[len(maskVar)-2] >= tuple(response.varBinds[0][0])[len(maskVar)-2]:
    oldresponse = response
    currInst = tuple(response.varBinds[0][0])[len(maskVar)-1] #Salvamos el indice
    varBindsIn = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.' + str(currInst)))]
    responseIn = snmp_engine.snmpget(varBindsIn)
    inOctects = responseIn.varBinds[0][1] #Guardamos los octetos que entran
    varBindsOut = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.16.' + str(currInst)))]
    responseOut = snmp_engine.snmpget(varBindsOut)
    outOctects = responseOut.varBinds[0][1]  #Guardamos los octetos que salen
    time.sleep(5) #Esperamos para que se curse trafico
    varBindsIn = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.' + str(currInst)))]
    responseIn = snmp_engine.snmpget(varBindsIn)
    inOctects = responseIn.varBinds[0][1] - inOctects #Calculamos la diferencia
    varBindsOut = [ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.16.' + str(currInst)))]
    responseOut = snmp_engine.snmpget(varBindsOut)
    outOctects = responseOut.varBinds[0][1] - outOctects #Calculamos la diferencia
    print(response.varBinds[0][1])
    print('Trafico entrante (b/s): ' +  str(inOctects/5))
    print('Trafico saliente (b/s): ' + str(outOctects/5))
    response = snmp_engine.snmpgetnext(oldresponse.varBinds)