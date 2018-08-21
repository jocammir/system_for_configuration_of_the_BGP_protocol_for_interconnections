import pymysql as sql

#Parametros de conexion - - - - - - - - - 
USUARIO="grupo3"
DB="bgp"
PASSWORD="grupo3"
HOST="localhost"
#- - - - - - - - - - - - - - - - - - - - -


#===============================================================================
#conectar: realiza la conexion a la basse de datos de MySQL
#Parametros:
# servidor   (str):  nombre del servidor
# usuario    (str):  nombre del usuario
# contraseña (str):  contraseña del usuario
# bd         (str):  nombre de la base de datos
#
# Retorna: conn -- objeto de conexion a base de datos
#          -1   -- cuando la conexion falla
#-------------------------------------------------------------------------------
def conectar(servidor,usuario,contraseña,bd):
    try:
        conn=sql.connect(host=servidor,user=usuario,db=bd,passwd=contraseña)
        return conn
    except:
        return -1



#===============================================================================
#validar_conexion: realiza hasta 3 intentos la conexion de base de datos
#Parametros: ninguno
#
# Retorna: conn -- objeto de conexion a base de datos
#          -1   -- cuando la conexion falla
#-------------------------------------------------------------------------------
def realizar_conexion():
    #realizar conexion a base de datos
    conn=conectar(HOST,USUARIO,PASSWORD,DB)

    #si conn==-1, conexion fallida
    return conn



#=============================================================================================
#consultar_usuarios: realiza la consulta de todos los usuarios segun el rol
#siempre y cuando la conexion sea exitosa
#Parametros:
# conexion   (objeto):  conexion realizadaa a la base de datos
# rol   (string): admin, monitoreo, todos, por omision todos
#
# Retorna: lista_admins -- lista de tuplas con la idUsuario, user y password
#                           [(idUsuario,user,password)]
#--------------------------------------------------------------------------------------------

def consultar_usuarios(conexion,rol="todos"):
    #selecciona el tipo de consulta a la base de datos segun el rol
    
    if rol=="admin":
        query="SELECT idUsuario,user,password FROM usuarios WHERE tipo='admin'"
    elif rol=="monitoreo":
        query="SELECT idUsuario,user,password FROM usuarios WHERE tipo='monitoreo'"
    else:
        query="SELECT idUsuario,user,password FROM usuarios"
        
    #realizar solo si la conexion es exitosa
    if conexion!=-1:
        cursor=conexion.cursor()   #crear cursor

        #Ejecutar Query para seleccionar a los usuarios segun el rol
        cursor.execute(query)
        lista_usuarios=list(cursor.fetchall())
        cursor.close()  #cerrar cursor
        conexion.commit()
        
        return lista_usuarios


#=============================================================================================
# validar_sesion: Retorna True si el usuario existe y si la contraseña es correcta,
# caso contrario False
#Parametros:
# conexion   (objeto):  conexion realizada a la base de datos
# usuario   (string): nombre del usuario
# contraseña (string): contraseña del usuario
#
# Retorna: Bool
#--------------------------------------------------------------------------------------------

def validar_sesion(conexion,usuario,contraseña):
    
    datos_usuarios=all_users(conexion) #tupla de lista paralelas: (id_usuarios,usuarios,contraseñas)
    usuarios=datos_usuarios[1] #lista de todos los usuarios
    contraseñas=datos_usuarios[2] #lista de todas las contraseñas

    #validar si existe el usuario ingresado
    try:
        search=usuarios.index(usuario)
    except:
        search=-1 #el usuario no existe
        
    if search==-1:
        #el usuario no fue encontrado
        return False
    #El usuario fue encontrado
    index_user=usuarios.index(usuario)
    passwd=contraseñas[index_user] #obtener contraseña del usuario

    #si la contraseña es correcta True
    return passwd==contraseña

#=============================================================================================
# all_users: hace una consulta a la BD, y retorna una tupla de listas paralelas con las id,usuarios y contraseñas
# 
#Parametros:
# conexion   (objeto):  conexion realizada a la base de datos
#
# Retorna: [id_usuarios],[usuarios],[contraseñas]  --- listas paralelas con las id,usuarios y contraseñas
#--------------------------------------------------------------------------------------------
def all_users(conexion):
    #listas con todos los usuarios
    admins=consultar_usuarios(conexion,'admin')
    monitoreo=consultar_usuarios(conexion,'monitoreo')
    
    #creacion de listas paralelas
    usuarios=[]
    contraseñas=[]
    ids_usuarios=[]

    #llenar las listas paralelas con la informacion de cada usuario
    for id_u,user,pwd in admins+monitoreo:
        usuarios.append(user)
        contraseñas.append(pwd)
        ids_usuarios.append(id_u)

    #retornar las listas paralelas en una tupla
    return ids_usuarios,usuarios,contraseñas


#=============================================================================================
# all_empresas: hace una consulta a la BD, y retorna una tupla de listas paralelas con las id,nombre y ASNs de las empresas
# 
#Parametros:
# conexion   (objeto):  conexion realizada a la base de datos
#
# Retorna: [ids_empresas],[nombres],[ASNs]  --- listas paralelas con las id,usuarios y contraseñas
#--------------------------------------------------------------------------------------------
def all_empresas(conexion):
    #listas con todos las empresas    
    empresas=consultar_empresas(conexion) #[(idEmpresa, nombre, ASN)]
    
    #creacion de listas paralelas
    nombres=[]
    ASNs=[]
    ids_empresas=[]

    #llenar las listas paralelas con la informacion de cada empresa
    for id_e,nombre,asn in empresas:
        nombres.append(nombre)
        ASNs.append(asn)
        ids_empresas.append(id_e)

    #retornar las listas paralelas en una tupla
    return ids_empresas,nombres,ASNs

#=============================================================================================
# establecer_sesion: genera una variable de sesion con el usuario y contraseña ingresados
# 
#Parametros:
# conexion   (objeto):  conexion realizada a la base de datos
# usuario   (string): nombre del usuario
# contraseña (string): contraseña del usuario
#
# Retorna: {'id':<id_usuario>,'username': <usuario>} -- diccionario
#--------------------------------------------------------------------------------------------

def establecer_sesion(conexion,usuario,contraseña):
    
    id_usuarios,usuarios,contraseñas=all_users(conexion) #crea las listas con la informacion de los usuarios
    
    search=usuarios.index(usuario) #busca el indice del usuario

    #retorna un diccionario con las claves id,username. Variable de sesion.
    return {'id':id_usuarios[search],'username': usuarios[search],'password':contraseñas[search]}

#=============================================================================================
# consultar_devices_empresa: realiza la consulta de todos los dispositivos donde existe el usuario y en una empresa especifica
# siempre y cuando la conexion sea exitosa
#Parametros:
# conexion   (objeto):  conexion realizadaa a la base de datos
# sesion   (diccionario): variable de sesion con las claves id y user
# id_empresa  (string): id de la empresa a consultar los dispositivos donde esta el usuario
#
# Retorna: lista_dispositivos -- lista de tuplas con la idDispositivo, nombre, gateway del dispositivo
#                           [(idDispositivo, nombre, gateway)]
#--------------------------------------------------------------------------------------------

def consultar_devices_empresa(conexion,sesion,id_empresa):
    
    cursor=conexion.cursor()   #crear cursor
    
    #Query donde se seleccionan los dispositivos de la empresa y a los que pertenece el usuario
    query="SELECT dispositivos.idDispositivo,dispositivos.nombre,dispositivos.gateway FROM dispositivos INNER JOIN usuario_dispositivo WHERE dispositivos.empresa='{}' and usuario_dispositivo.idDispositivo=dispositivos.idDispositivo and usuario_dispositivo.idUsuario='{}' and dispositivos.estado='activo'".format(id_empresa,sesion['id'])
    cursor.execute(query)
    
    lista_dispositivos=list(cursor.fetchall())
    
    cursor.close()  #cerrar cursor
    conexion.commit()

    return lista_dispositivos

#=============================================================================================
# consultar_interfaces: realiza la consulta de todas las interfaces de un dispositivo
# siempre y cuando la conexion sea exitosa
#Parametros:
# conexion   (objeto):  conexion realizadaa a la base de datos
# id_empresa  (string): id del dispositivo
#
# Retorna: lista_interfaces -- lista de tuplas con el nombre, ipAddress, mascara del dispositivo
#                           [(nombre, ipAddress, mascara)]
#--------------------------------------------------------------------------------------------
def consultar_interfaces(conexion,id_dispositivo):
    cursor=conexion.cursor()   #crear cursor
    
    #Query donde se seleccionan todas las interfaces de un dispositivo dado
    query="SELECT nombre,ipAddress,mascara FROM interfaces WHERE idDispositivo='{}'".format(id_dispositivo)
    cursor.execute(query)
    
    lista_interfaces=list(cursor.fetchall())
    
    cursor.close()  #cerrar cursor
    conexion.commit()

    return lista_interfaces

#=============================================================================================
# consultar_empresas: realiza la consulta de todas las empresas
# siempre y cuando la conexion sea exitosa
#Parametros:
# conexion   (objeto):  conexion realizadaa a la base de datos
#
# Retorna: lista_empresas -- lista de tuplas con la idEmpresa, nombre,ASN
#                           [(idEmpresa, nombre, ASN)]
#--------------------------------------------------------------------------------------------
def consultar_empresas(conexion):
    cursor=conexion.cursor()   #crear cursor
    
    #Query donde se seleccionan todas las empresas existentes
    query="SELECT idEmpresa,nombre,ASN FROM empresa"
    cursor.execute(query)
    
    lista_empresas=list(cursor.fetchall())
    
    cursor.close()  #cerrar cursor
    conexion.commit()

    return lista_empresas

#=============================================================================================
# buscar_id_dispositivo: busca el dispositivo segun el nombre y la id de empresa
# siempre y cuando la conexion sea exitosa
#Parametros:
# conexion   (objeto):  conexion realizadaa a la base de datos
#
# Retorna: lista_empresas -- lista de tuplas con la idEmpresa, nombre,ASN
#                           [(idEmpresa, nombre, ASN)]
#--------------------------------------------------------------------------------------------
def buscar_id_dispositivo(nombre,id_empresa,conexion):
    cursor=conexion.cursor()   #crear cursor
    
    #Query donde se seleccionan todas las empresas existentes
    query="SELECT idDispositivo FROM dispositivos WHERE nombre='{}' AND empresa ='{}'".format(nombre,id_empresa)
    cursor.execute(query)
    
    lista_dispositivo=list(cursor.fetchall())
    
    cursor.close()  #cerrar cursor
    conexion.commit()

    return lista_dispositivo[0][0]

#=============================================================================================
# buscar_dispositivo: busca el dispositivo segun el nombre y la id de empresa
# siempre y cuando la conexion sea exitosa
#Parametros:
# conexion   (objeto):  conexion realizadaa a la base de datos
#
# Retorna: lista_empresas -- lista de tuplas con la idEmpresa, nombre,ASN
#                           [(idEmpresa, nombre, ASN)]
#--------------------------------------------------------------------------------------------
def buscar_ip_dispositivo(nombre,id_empresa,conexion):
    cursor=conexion.cursor()   #crear cursor
    
    #Query donde se seleccionan todas las empresas existentes
    query="SELECT gateway FROM dispositivos WHERE nombre='{}' AND empresa ='{}'".format(nombre,id_empresa)
    cursor.execute(query)
    
    lista_dispositivo=list(cursor.fetchall())
    
    cursor.close()  #cerrar cursor
    conexion.commit()

    return lista_dispositivo[0][0]

#===================================================================
# cerrar_conexion: realiza el cierre de la conexion de MySQL
# Parametros:
#   conexion (objeto):  conexion realizada a la base de datos
# Retorna: nada
#------------------------------------------------------------------
def cerrar_conexion(conexion):
    conexion.close()
    

