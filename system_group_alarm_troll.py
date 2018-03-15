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

# Codigo walk para ver status creados
version = 'v1'
community = 'public'
ip_addr = '155.210.157.203'
port = 161


def snmpwalk(varbinds):

    response = snmp_engine.snmpgetnext(varbinds)
    maskVar = tuple(varbinds[0][0])
    while maskVar[len(maskVar)-1] >= tuple(response.varBinds[0][0])[len(maskVar)-1]:
        print([maskVar[len(maskVar)-1], tuple(response.varBinds[0][0])[len(maskVar)-1]])
        print(response.varBinds[0])
        response = snmp_engine.snmpgetnext(response.varBinds)

snmp_engine = snmp_requests(version, community, ip_addr, port)

varBinds1 = [ObjectType(ObjectIdentity('1.3.6.1.2.1.16.3.1.1.12'))]
snmpwalk(varBinds1)


# Configuracion sonda

version = 'v1'
ip_addr = '155.210.157.203'
community = 'private'
port = 161


# Genero una entrada en localSnmp
snmp_engine = snmp_requests(version, community, ip_addr, port)



# Grupo event




# Grupo alarm
varBindsAlarm = [ObjectType(ObjectIdentity('1.3.6.1.2.1.16.3.1.1.12.112'),Integer(4))]
snmp_engine.snmpset(varBindsAlarm)



# Esta funcion es la que envia el mensaje
# def send_msg(body):
#
#     fromaddr = ""
#     toaddr = ""
#     password = ""
#
#     msg = multipart.MIMEMultipart()
#     msg['From'] = fromaddr
#     msg['To'] = toaddr
#     msg['Subject'] = "Alarm"
#
#     #body = "Python test mail"
#     msg.attach(text.MIMEText(body, 'plain'))
#
#
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#     server.login(fromaddr, password)
#     cuerpo = msg.as_string()
#     server.sendmail(fromaddr, toaddr, cuerpo)
#
#
#
#
#
#
# # noinspection PyUnusedLocal
# def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
#     while wholeMsg:
#         msgVer = int(api.decodeMessageVersion(wholeMsg))
#         if msgVer in api.protoModules:
#             pMod = api.protoModules[msgVer]
#         else:
#             print('Unsupported SNMP version %s' % msgVer)
#             return
#         reqMsg, wholeMsg = decoder.decode(
#             wholeMsg, asn1Spec=pMod.Message(),
#         )
#         print('Notification message from %s:%s: ' % (
#             transportDomain, transportAddress
#         )
#               )
#         reqPDU = pMod.apiMessage.getPDU(reqMsg)
#         text = ''
#         if reqPDU.isSameTypeWith(pMod.TrapPDU()):
#             if msgVer == api.protoVersion1:
#                 text = text + 'Enterprise: ' + pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint() + '\n'
#                 # Incluir el resto de campos del trap que se consideren oportunos
#
#                 varBinds = pMod.apiTrapPDU.getVarBinds(reqPDU)
#             else:
#                 varBinds = pMod.apiPDU.getVarBinds(reqPDU)
#
#             # Incluir el contenido de las varBinds en el correo electronico
#
#
#
#
#
#     return wholeMsg
#
#
# transportDispatcher = AsyncoreDispatcher()
#
# transportDispatcher.registerRecvCbFun(cbFun)
#
# # UDP/IPv4
# transportDispatcher.registerTransport(
#     udp.domainName, udp.UdpSocketTransport().openServerMode(('0.0.0.0', 162))
# )
#
# # UDP/IPv6
# transportDispatcher.registerTransport(
#     udp6.domainName, udp6.Udp6SocketTransport().openServerMode(('::1', 162))
# )
#
#
# transportDispatcher.jobStarted(1)
#
# try:
#     # Dispatcher will never finish as job#1 never reaches zero
#     transportDispatcher.runDispatcher()
# except:
#     transportDispatcher.closeDispatcher()
#     raise
