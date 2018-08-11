import pymysql as sql
import time as tm

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
        print("No se pudo conectar con el servidor")
        return -1



#===============================================================================
#validar_conexion: realiza hasta 3 intentos la conexion de base de datos
#Parametros: ninguno
#
# Retorna: conn -- objeto de conexion a base de datos
#          -1   -- cuando la conexion falla
#-------------------------------------------------------------------------------
def validar_conexion():
    #realizar conexion a base de datos
    conn=conectar(HOST,USUARIO,PASSWORD,DB)
    intentos=0
    
    #plazo de 3 intentos
    while not(intentos==3 or conn!=-1):
        tm.sleep(2)
        
        #plazo de 5 segundos
        for i in range(5,0,-1):
            print("\n"*50)
            print("Reintentando en",i,"segundos [{}] intentos restantes".format(3-intentos))
            tm.sleep(1)
            
        #temporizador de intentos
        conn=conectar(HOST,USUARIO,PASSWORD,DB)
        intentos+=1

        
    if intentos==3:
        #intentos fallidos
        print("Intentelo mas tarde")
        return -1
    #exitoso
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
    return {'id':id_usuarios[search],'username': usuarios[search]}

#=============================================================================================
#consultar_usuarios: realiza la consulta de todos los usuarios segun el rol
#siempre y cuando la conexion sea exitosa
#Parametros:
# conexion   (objeto):  conexion realizadaa a la base de datos
# sesion   (diccionario): variable de sesion con las claves id y user
# id_empresa  (string): id de la empresa a consultar donde esta el usuario
#
# Retorna: lista_dispositivos -- lista de tuplas con la idDispositivo, nombre, gateway del dispositivo
#                           [idDispositivo, nombre, gateway]
#--------------------------------------------------------------------------------------------

def consultar_dispositivos_usuarios_empresa(conexion,sesion,id_empresa):
    
    cursor=conexion.cursor()   #crear cursor
    #Query donde se seleccionan los dispositivos de la empresa y a los que pertenece el usuario
    query="SELECT idDispositivo,nombre,gateway FROM dispositivos INNER JOIN usuarios_dispositivos WHERE idEmpresa='{}' and usuario_dispositivo.idDispositivo=idDispositivo and usuario_dispositivo.idUsuario='{}'".format(id_empresa,sesion['id'])
    cursor.execute(query)
    lista_dispositivos=list(cursor.fetchall())
    cursor.close()  #cerrar cursor
    conexion.commit()
    
#===================================================================
# cerrar_conexion: realiza el cierre de la conexion de MySQL
# Parametros:
#   conexion (objeto):  conexion realizada a la base de datos
# Retorna: nada
#------------------------------------------------------------------
def cerrar_conexion(conexion):
    conexion.close()
    


    


    
