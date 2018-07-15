import getpass
import sys
import telnetlib
import time


#Funcion para realizar la conexion telnet con el router al que se va a aplicar el enrutamiento#
def conexion_telnet(ip,user,password):
    HOST = ip

    tn = telnetlib.Telnet(HOST,port='23')

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        # tn.read_until("Password: ")
        tn.write(password + "\n")
    print("Conexion telnet realizada con exito")
    return tn


#Funcion para aplicar la configuracion basica del router
def configuracionBasica(tn, hostname):
    tn.write("enable \n")
    tn.write("admin\n")
    tn.write("conf t \n")
    tn.write("hostname "+ hostname+" \n")
    #tn.write("ip domain-name fiec.espol.edu.ec \n")
    #tn.write("crypto key generate rsa \n")
    #tn.write("1024 \n")
    tn.write("username monitoreo privilege 5 secret monitoreo \n")
    tn.write("banner motd  # ACCESO SOLO A PERSONAL AUTORIZADO# \n")
    tn.write("line vty 0 4 \n")
    tn.write("transport input all \n")
    tn.write("login local \n")
    tn.write("exec-timeout 3 3 \n")
    tn.write("logging synchronous \n")
    tn.write("line console 0 \n")
    tn.write("transport output all \n")
    tn.write("login local \n")
    tn.write("exec-timeout 3 3 \n")
    tn.write("logging synchronous \n")
    configurarInterfaces(tn)
    tn.write("end \n")
    tn.write("wr \n")
    tn.write("\n")


    print("configuracion realizada con exito!!!")

#Configura la ip y mascara de subred al leer un archivo donde se encuentra cada interfaz con su respectiva ip y mascara
def configurarInterfaces(tn):
    f = open("R2_interfaces.txt", 'r')
    a = f.readlines()
    for linea in a:
        lista = linea.split(',')
        print(lista)
        interfaz = lista[0]
        ip = lista[1]
        mascara = lista[2]
        mascara2 = (mascara[0:(len(mascara) - 1)])

        tn.write("interface " + interfaz + "\n")
        tn.write("ip address " + ip + " " + mascara2 + "\n")
        tn.write("no shutdown \n")
        tn.write("exit \n")

    f.close()


#Funcion para habilitar el enrutamiento bgp en el router con su respectivo AS
def SesionBGP(tn, ASlocal):
    tn.write("enable \n")
    tn.write("admin\n")
    tn.write("configure terminal\n")
    tn.write("router BGP " + ASlocal+"\n")
    tn.write("end \n")
    tn.write("wr \n")
    tn.write("\n")


#Funcion para configurar el router vecino con su AS
def configurarVecino(ipNeighbor, ASlocal, ASremoto,tn):
    tn.write("conf terminal \n")
    tn.write("\n")
    tn.write("\n")
    tn.write("ip route 0.0.0.0 0.0.0.0 lo0 name to_core_isp \n")
    tn.write("\n")
    tn.write("\n")
    tn.write("router bgp "+ASlocal+"\n")
    tn.write("\n")
    tn.write("\n")
    tn.write("neighbor " +ipNeighbor+ " remote-as " +ASremoto+"\n")
    tn.write("\n")
    tn.write("\n")
    tn.write("end \n")
    tn.write("\n")
    tn.write("wr \n")
    tn.write("\n")


#Funcion para anunciar las redes que son ingresadas como parametro de entrada
def configurarNetwork(tn, network, ASlocal):
    tn.write("conf terminal \n")
    tn.write("router bgp " + ASlocal + "\n")
    if(network=="0.0.0.0"):
        tn.write("network "+ network+" \n")
    else:
        tn.write("network " + network + " mask 255.255.255.0" +"\n")

    tn.write("end \n")
    tn.write("wr \n")
    tn.write("\n")

def validarFormatoIP(ipAddress):
 # Validar el ingreso de la dirreccion ip, que contenga los cuatro octetos y que cada uno este dentro del rango(0-255)
 flag=False
 try:
     if (len(ipAddress.split("."))) != 4:
         print("ERROR: Ingrese una direcccion IP valida!!!")
     elif (int(ipAddress.split(".")[0]) < 0 or int(ipAddress.split(".")[0]) > 255):
         print("ERROR: Ingrese una direcccion IP valida!!!")
     elif (int(ipAddress.split(".")[1]) < 0 or int(ipAddress.split(".")[1]) > 255):
         print("ERROR: Ingrese una direcccion IP valida!!!")
     elif (int(ipAddress.split(".")[2]) < 0 or int(ipAddress.split(".")[2]) > 255):
         print("ERROR: Ingrese una direcccion IP valida!!!")
     elif (int(ipAddress.split(".")[3]) < 0 or int(ipAddress.split(".")[3]) > 255):
         print("Ingrese una direcccion IP (valida!!!")
     else:
         flag=True
 except ValueError:
     print("ERROR: La direccion IP debe ser numerica")

 return(flag)
