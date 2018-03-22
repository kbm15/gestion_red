from snmp_library import *
from pysnmp.hlapi.asyncore import *

# Email
from email.mime import multipart, text
import smtplib

# TrapReceiver
from pysnmp.carrier.asyncore.dispatch import AsyncoreDispatcher
from pysnmp.carrier.asyncore.dgram import udp, udp6, unix
from pyasn1.codec.ber import decoder
from pysnmp.proto import api

# Habilitar https://myaccount.google.com/lesssecureapps


# Configuracion sonda

version = 'v1'
ip_addr = '155.210.157.202'
community = 'private'
port = 161
snmp_engine = snmp_requests(version, community, ip_addr, port)

# Genero una entrada en localSnmp
varBindsFree = [ObjectType(ObjectIdentity('1.3.6.1.4.1.43.10.10.3.0'))]
response = snmp_engine.snmpget(varBindsFree)
print(response.varBinds[0])
varBindsTrap=ObjectType(ObjectIdentity('1.3.6.1.4.1.43.10.10.2.1.7.5'),Integer(4))
varBindsDest=ObjectType(ObjectIdentity('1.3.6.1.4.1.43.10.10.2.1.2.5'),OctetString('155.210.157.126'))
varBindsDest=ObjectType(ObjectIdentity('1.3.6.1.4.1.43.10.10.2.1.4.5'),OctetString('public'))
varBinds = [varBindsTrap, varBindsDest]
response = snmp_engine.snmpset(varBinds)



# Grupo event
varBindsEvent = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.9.1.1.7.1337'),Integer(3))
varBindsDescription = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.9.1.1.2.1337'),OctetString('Alarma trol'))
varBindsCommunity = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.9.1.1.4.1337'),OctetString('Comunidad del anillo'))
varBindsType = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.9.1.1.3.1337'),Integer(4))
varBinds = [varBindsEvent, varBindsDescription, varBindsType]
response = snmp_engine.snmpset(varBinds)
print(response.errorStatus)

# Grupo alarm
varBindsAlarm = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.3.1.1.12.1337'),Integer(3))
varBindsInterval = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.3.1.1.2.1337'),Integer(5))
varBindsType = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.3.1.1.3.1337'),ObjectIdentifier('1.3.6.1.2.1.5.1.0'))
varBindsRise = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.3.1.1.7.1337'),Integer(20))
varBindsEvent = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.3.1.1.9.1337'),Integer(1337))
varBindsOwner = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.3.1.1.11.1337'),OctetString('github.com/kbm15/'))
varBinds = [varBindsAlarm, varBindsInterval, varBindsType, varBindsRise, varBindsEvent, varBindsOwner]
response = snmp_engine.snmpset(varBinds)
print(response.errorStatus)

# Valid
varBindsEvent = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.9.1.1.7.1337'),Integer(1))
varBindsAlarm = ObjectType(ObjectIdentity('1.3.6.1.2.1.16.3.1.1.12.1337'),Integer(1))
varBindsTrap = ObjectType(ObjectIdentity('1.3.6.1.4.1.43.10.10.2.1.7.1'),Integer(1))
varBinds = [varBindsAlarm, varBindsEvent, varBindsTrap]
response = snmp_engine.snmpset(varBinds)
print(response.errorStatus)
# Esta funcion es la que envia el mensaje
def send_msg(body):

    fromaddr = "woodencnc@gmail.com"
    toaddr = "keyblademaster15@gmail.com"
    password = "maduixa69"

    msg = multipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alarm"

    #body = "Python test mail"
    msg.attach(text.MIMEText(body, 'plain'))


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr, password)
    cuerpo = msg.as_string()
    server.sendmail(fromaddr, toaddr, cuerpo)






# noinspection PyUnusedLocal
def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
    while wholeMsg:
        msgVer = int(api.decodeMessageVersion(wholeMsg))
        if msgVer in api.protoModules:
            pMod = api.protoModules[msgVer]
        else:
            print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(
            wholeMsg, asn1Spec=pMod.Message(),
        )
        print('Notification message from %s:%s: ' % (
            transportDomain, transportAddress
        )

              )
        send_msg('Notification message from %s:%s: ' % (
            transportDomain, transportAddress
        ))
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        text = ''
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:
                text = text + 'Enterprise: ' + pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint() + '\n'
                # Incluir el resto de campos del trap que se consideren oportunos

                varBinds = pMod.apiTrapPDU.getVarBinds(reqPDU)
            else:
                varBinds = pMod.apiPDU.getVarBinds(reqPDU)

            # Incluir el contenido de las varBinds en el correo electronico





    return wholeMsg


transportDispatcher = AsyncoreDispatcher()

transportDispatcher.registerRecvCbFun(cbFun)

# UDP/IPv4
transportDispatcher.registerTransport(
    udp.domainName, udp.UdpSocketTransport().openServerMode(('0.0.0.0', 162))
)

# UDP/IPv6
transportDispatcher.registerTransport(
    udp6.domainName, udp6.Udp6SocketTransport().openServerMode(('::1', 162))
)


transportDispatcher.jobStarted(1)

try:
    # Dispatcher will never finish as job#1 never reaches zero
    transportDispatcher.runDispatcher()
except:
    transportDispatcher.closeDispatcher()
    raise
