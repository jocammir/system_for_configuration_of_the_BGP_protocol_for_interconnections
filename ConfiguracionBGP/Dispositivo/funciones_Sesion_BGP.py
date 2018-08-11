
#===============================================================================
#conexion_Telnet: Habilitar BGP
#Parametros:
# objeto_Telnet(Telnet):  objeto  Telnet
# AS_Local  (int):  usuario del dispositivo
#
#-------------------------------------------------------------------------------

def Sesion_BGP(objeto_Telnet, AS_Local):
    objeto_Telnet.write("enable\n".encode('ascii'))
    objeto_Telnet.write("configure terminal\n".encode('ascii'))
    objeto_Telnet.write("router bgp " +AS_Local+"\n".encode('ascii'))
    objeto_Telnet.write("end\n".encode('ascii'))
    objeto_Telnet.write("wr\n".encode('ascii'))
    objeto_Telnet.write("\n".encode('ascii'))


#Funcion para configurar el router vecino con su AS
def configurarVecino(ipNeighbor, ASlocal, ASremoto,tn):
    tn.write("conf terminal\n".encode('ascii'))
    tn.write("\n".encode('ascii'))
    tn.write("\n".encode('ascii'))
    tn.write("ip route 0.0.0.0 0.0.0.0 lo0 name to_core_isp \n".encode('ascii'))
    tn.write("\n".encode('ascii'))
    tn.write("\n".encode('ascii'))
    tn.write("router bgp "+ASlocal+"\n".encode('ascii'))
    tn.write("\n".encode('ascii'))
    tn.write("\n".encode('ascii'))
    tn.write("neighbor " +ipNeighbor+ " remote-as " +ASremoto+"\n".encode('ascii'))
    tn.write("\n".encode('ascii'))
    tn.write("\n".encode('ascii'))
    tn.write("end \n".encode('ascii'))
    tn.write("\n".encode('ascii'))
    tn.write("wr \n".encode('ascii'))
    tn.write("\n".encode('ascii'))


#Funcion para anunciar las redes que son ingresadas como parametro de entrada
def configurarNetwork(tn, network, ASlocal):
    tn.write("conf t \n".encode('ascii'))
    tn.write("router bgp " + ASlocal + "\n".encode('ascii'))
    if(network=="0.0.0.0"):
        tn.write("network "+ network+" \n".encode('ascii'))
    else:
        tn.write("network " + network + " mask 255.255.255.0" +"\n".encode('ascii'))

    tn.write("end \n".encode('ascii'))
    tn.write("wr \n".encode('ascii'))
    tn.write("\n".encode('ascii'))

