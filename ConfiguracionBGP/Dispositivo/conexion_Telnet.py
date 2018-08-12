import telnetlib

import conexion_mysql as sql

#import ConfiguracionBGP.Base_de_Datos.conexion_mysql

HOST_Loopback=str('192.168.100.254')
HOST_Local=str("192.168.100.1")
HOST_Remoto=str("192.168.100.2")

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

def conexion_Telnet(host,user_Dispo,password_Dispo):
    try:
        objeto_Telnet = telnetlib.Telnet(host,port='23')
        objeto_Telnet.open(host, port='23')
        user = str(user_Dispo + "\n")
        password = str(password_Dispo + "\n")
        objeto_Telnet.write(user.encode('ascii'))
        objeto_Telnet.write(password.encode('ascii'))
        print("Conexion Telnet realizada con exito\n")
        return(objeto_Telnet)
    except:
        print("Error al establecer conexión Telnet")


#===============================================================================
#iniciar_Configuracion: Permite inicar una configuración
#Parametros:
# objeto_Telnet   (Telnet): objeto de conexión Telnet
# 
#-------------------------------------------------------------------------------

def iniciar_Configuracion(objeto_Telnet):
    objeto_Telnet.write("enable\n".encode('ascii'))
    objeto_Telnet.write("conf t\n".encode('ascii'))
    

#===============================================================================
#guardar_Configuracion: guarda en memoria las configuraciones realizadas
#Parametros:
# objeto_Telnet   (Telnet): objeto de conexión Telnet
#
#-------------------------------------------------------------------------------
    
def guardar_Configuracion(objeto_Telnet):
    objeto_Telnet.write("end\n".encode('ascii'))
    objeto_Telnet.write("wr\n".encode('ascii'))
    objeto_Telnet.write("\n".encode('ascii'))
    
#===============================================================================
#config_Plantilla_Basica: configuración básica de un router
#Parametros:
# objeto_Telnet   (telnet):  objeto tipo telnet
# hostname_Dispo    (str):  nombre del dispositivo
#
#-------------------------------------------------------------------------------

def config_Plantilla_Basica(objeto_Telnet,hostname_Dispo):
    iniciar_Configuracion(objeto_Telnet)
    nombre_Host=str("hostname "+hostname_Dispo+"\n")
    objeto_Telnet.write(nombre_Host.encode('ascii'))
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
    guardar_Configuracion(objeto_Telnet)


#===============================================================================
#configurar_Interfaces: configura IP y Mask  en las interfaces del router.
#Parametros:
# objeto_Telnet   (telnet):  objeto tipo telnet
# id_empresa (int):  identificador del dispositivo
# usuario(str): nombre del usuario
# contraseña (str): contraseña del usuario
#
#-------------------------------------------------------------------------------

def configurar_Interfaces(objeto_Telnet, nom_empresa,nom_Dispo_Especifico, usuario, contraseña):
    conex_BD = sql.validar_conexion()
    config_Plantilla_Basica(objeto_Telnet,nom_Dispo_Especifico)
    sesion = sql.establecer_sesion(conex_BD, usuario, contraseña)
    id_empresas, nombres, ASNs = sql.all_empresas(conex_BD)
    
    try:
        id_empresa=""
        id_Dispo_Especifico=""
        for i in range(len(nombres)):
            if (nombres[i]==nom_empresa.strip()):
                id_empresa=id_empresas[i]
            
        list_Dispositivos = sql.consultar_devices_empresa(conex_BD, sesion, id_empresa)
        for id_Dispositivo,nom_Dispositivo,gateway_Dispo in list_Dispositivos:
            if(nom_Dispositivo==nom_Dispo_Especifico.strip()):
                id_Dispo_Especifico=id_Dispositivo
        
        lista_Interfaces_Dispo= sql.consultar_interfaces(conex_BD,id_Dispo_Especifico)
    
    
        for interfaz in lista_Interfaces_Dispo:
            nom_Interfaz = str("int "+interfaz[0]+"\n")
            ip_Interfaz = str(interfaz[1])
            mascara_Interfaz = str(interfaz[2]+"\n")
            ip_Adress=str("ip address "+ip_Interfaz+" "+mascara_Interfaz)
        
            objeto_Telnet.write(nom_Interfaz.encode('ascii'))
            objeto_Telnet.write(ip_Adress.encode('ascii'))
            objeto_Telnet.write("no shutdown\n".encode('ascii'))
            objeto_Telnet.write("exit\n".encode('ascii'))
    except:
        print("Empresa o dispositivo incorrectos")
    guardar_Configuracion(objeto_Telnet)
    print(nom_empresa+"->"+nom_Dispo_Especifico+"\nInterfaces configuradas con éxito")

#Pruebas
#tn=conexion_Telnet(HOST_Local,str("admin"),str("admin"))
#config_Plantilla_Basica(tn,str("RouterLoco"))
#configurar_Interfaces(tn,str("RoutingSA"),str("RouterLocal"), str("jocelyn"), str("jocelyn"))
    
