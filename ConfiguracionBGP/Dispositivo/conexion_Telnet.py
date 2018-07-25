import telnetlib

import ConfiguracionBGP.Base_de_Datos.conexion_mysql


#===============================================================================
#conexion_Telnet: realiza la conexión a telnet con el Router a configurar
#Parametros:
# ip   (str):  dirección IP del dispositivo
# user_Dispo    (str):  usuario del dispositivo
# password_Dispo (str):  contraseña del dispositivo
#
# Retorna: objeto_Telnet -- objeto de conexion Telnet
#          -1   -- cuando la conexion falla
#-------------------------------------------------------------------------------

def conexion_Telnet(ip,user_Dispo,password_Dispo):
    host = ip
    try:
        objeto_Telnet = telnetlib.Telnet(host,port='23')
        objeto_Telnet.write(user_Dispo + "\n")
        objeto_Telnet.write(password_Dispo + "\n")
        return(objeto_Telnet)
        print("Conexion Telnet realizada con exito")
    except:
        print("Error al establecer conexión Telnet")

#===============================================================================
#config_Plantilla_Basica: configuración básica de un router
#Parametros:
# objeto_Telnet   (telnet):  objeto tipo telnet
# hostname_Dispo    (str):  nombre del dispositivo
#
#-------------------------------------------------------------------------------

def config_Plantilla_Basica(objeto_Telnet, hostname_Dispo):
    objeto_Telnet.write("enable\n".encode('ascii'))
    objeto_Telnet.write("conf t\n".encode('ascii'))
    objeto_Telnet.write("hostname "+hostname_Dispo+"\n")
    objeto_Telnet.write("ip domain-name fiec.espol.edu.ec\n".encode('ascii'))
    objeto_Telnet.write("ip name-server 192.168.1.17\n".encode('ascii'))
    objeto_Telnet.write("ip name-server 192.168.1.19\n".encode('ascii'))
    objeto_Telnet.write("username monitoreo privilege 5 secret monitoreo\n".encode('ascii'))
    objeto_Telnet.write("banner motd #ACCESO SOLO A PERSONAL AUTORIZADO#\n".encode('ascii'))
    objeto_Telnet.write("line vty 0 4\n".encode('ascii'))
    objeto_Telnet.write("transport input all\n".encode('ascii'))
    objeto_Telnet.write("login local\n".encode('ascii'))
    objeto_Telnet.write("exec-timeout 3 3\n".encode('ascii'))
    objeto_Telnet.write("logging synchronous\n".encode('ascii'))
    objeto_Telnet.write("line console 0\n".encode('ascii'))
    objeto_Telnet.write("transport output all\n".encode('ascii'))
    objeto_Telnet.write("login local\n".encode('ascii'))
    objeto_Telnet.write("exec-timeout 3 3\n".encode('ascii'))
    objeto_Telnet.write("logging synchronous\n".encode('ascii'))
    configurar_Interfaces(objeto_Telnet,hostname_Dispo)
    objeto_Telnet.write("end\n".encode('ascii'))
    objeto_Telnet.write("wr\n".encode('ascii'))
    objeto_Telnet.write("\n".encode('ascii'))


#===============================================================================
#configurar_Interfaces: configura IP y Mask  en las interfaces del router.
#Parametros:
# objeto_Telnet   (telnet):  objeto tipo telnet
# id_empresa (int):  identificador del dispositivo
# usuario(str): nombre del usuario
# contraseña (str): contraseña del usuario
#
#-------------------------------------------------------------------------------

def configurar_Interfaces(objeto_Telnet, id_empresa, usuario, contraseña):
    conex_BD = ConfiguracionBGP.sql.validar_conexion()
    sesion = ConfiguracionBGP.sql.establecer_sesion(conex_BD, usuario, contraseña)
    #id_empresas, nombres, ASNs = ConfiguracionBGP.sql.all_empresas(conex_BD)
    dispositivos = ConfiguracionBGP.sql.consultar_devices_empresa(conex_BD, sesion, id_empresa)

    for idDispositivo, nombre, gateway in dispositivos:
        id_dispositivo = dispositivos[id_empresa][0]
        lista_Interfaces_Dispo= ConfiguracionBGP.consultar_interfaces(conex_BD,id_dispositivo)

    for interfaz in lista_Interfaces_Dispo:
        nom_Interfaz = interfaz[0]
        ip_Interfaz = interfaz[1]
        mascara_Interfaz = interfaz[2]

        objeto_Telnet.write("int "+nom_Interfaz+"\n".encode('ascii'))
        objeto_Telnet.write("ip address "+ip_Interfaz+" "+mascara_Interfaz+"\n".encode('ascii'))
        objeto_Telnet.write("no shutdown\n".encode('ascii'))
        objeto_Telnet.write("exit\n".encode('ascii'))
