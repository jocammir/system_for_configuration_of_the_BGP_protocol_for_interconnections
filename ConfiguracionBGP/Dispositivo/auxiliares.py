#===============================================================================
# obtener_dir_red: obtiene la direccion de red de una ip de host segun su mascara
# Parametros:
#   ip      (str):   direccion ip
#   mascara (str):   mascara de subred
#
# Retorna:
#   direccion de red
#-------------------------------------------------------------------------------    
def obtener_dir_red(ip,mascara):
    #separa los octetos
    octetos_ip=ip.split(".") #[xxx,xxx,xxx,xxx]
    octetos_mask=mascara.split(".") #[xxx,xxx,xxx,xxx]

    #lista con los octetos de la direccion de red
    network=[]
    
    for i in range(len(octetos_ip)):
        #convierte los octetos de la ip y la mascara a binario
        a=conv_bin(int(octetos_ip[i]))
        b=conv_bin(int(octetos_mask[i]))

        #realiza operacion and entre los octetos y la convierte a decimal
        operacion=operar_bin(a,b)
        operacion=conv_dec(operacion)

        #guarda el nuevo octeto
        network.append(str(operacion))
    return ".".join(network)

#===============================================================================
# operar_bin: opera con and bit a bit un numero binario
# Parametros:
#   octeto1     (str):   numero binario
#   octeto2     (str):   numero binario
#
# Retorna:
#   res  (str): numero binario
#-------------------------------------------------------------------------------    
def operar_bin(octeto1,octeto2):
    res=""

    #comparacion bit a bit
    for i in range(len(octeto1)):
        a=int(octeto1[i])
        b=int(octeto2[i])
        res+=str(a and b)
        
    return res

#===============================================================================
# conv_bin: convierte a binario un numero decimal
# Parametros:
#   n     (int):   numero decimal
#
# Retorna:
#   numero binario de 8 bits
#-------------------------------------------------------------------------------   
def conv_bin(n):
    binary=""
    while n!=0:
        r=n%2
        binary=str(r)+binary
        n//=2
    return "0"*(8-len(binary))+binary

#===============================================================================
# conv_dec: convierte a decimal un numero binario
# Parametros:
#   bn     (str):   numero binario
#
# Retorna:
#   n (int):  numero decimal
#-------------------------------------------------------------------------------
def conv_dec(bn):
    n=0
    bn=bn[::-1]
    for i in range(len(bn)):
        n+=(2**int(i))*int(bn[i])
    return n

#===============================================================================
# validar_formato_IP: determina si una direccion ip tiene el formato correcto
# Parametros:
#   ip_Address     (str):   numero binario
#
# Retorna:
#   True: ip valida, False: ip no valida
#-------------------------------------------------------------------------------
def validar_formato_IP(ip_Address):
    octetos=ip_Address.split(".")
    #si no tiene 4 octetos
    if len(octetos)!=4:
        return False
    
    #verificar octeto por octeto
    for octeto in octetos:
        
        if not octeto.isdigit():
            #si el octeto no es un numero decimal
            return False
        
        #el octeto es decimal
        octeto=int(octeto)
        
        if not 0<=octeto<=255:
            #si el octeto no esta entre 0 y 255
            return False

    #la direccion ip es valida
    return True

#===============================================================================
# validar_ASN: determina si un ASN tiene el formato correcto
# Parametros:
#   asn     (str):   numero de sistema autonomo
#
# Retorna:
#   True: asn valido, False: asn no valido
#-------------------------------------------------------------------------------
def validar_ASN(asn):
    
    if not asn.isdigit():
        #si no es un digito
        return False

    #convertir a digito
    asn=int(asn)

    #verificar si esta entre 1 y 64512
    return 1<=asn<=64512
