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
# servidor   str:  nombre del servidor
# usuario    str:  nombre del usuario
# contraseña str:  contraseña del usuario
# bd         str:  nombre de la base de datos
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
        
        conn=conectar(HOST,USUARIO,PASSWORD,DB)
        intentos+=1
    if intentos==3:
        #intentos fallidos
        print("Intentelo mas tarde")
        return -1
    #exitoso
    return conn



#=============================================================================================
#consultar_usuarios_admin: realiza la consulta de todos los usuarios que son administradores
# siempre y cuando la conexion sea exitosa
#Parametros:
# conexion   objeto:  conexion realizadaa a la base de datos
#
# Retorna: lista_admins -- lista de tuplas con la idUsuario, user y password
#                           [(idUsuario,user,password)]
#--------------------------------------------------------------------------------------------

def consultar_usuarios_admin(conexion):
    #realizar solo si la conexion es exitosa
    if conexion!=-1:
        cursor=conexion.cursor()   #crear cursor

        #Ejecutar Query para seleccionar a los administradores
        cursor.execute("SELECT idUsuario,user,password FROM usuarios WHERE tipo='admin'")
        lista_admins=list(cursor.fetchall())
        cursor.close()  #cerrar cursor
        conexion.commit()
        
        return lista_admins

#=============================================================================================
# consultar_usuarios_admin: realiza la consulta de todos los usuarios que son monitoreo
# siempre y cuando la conexion sea exitosa
#Parametros:
# conexion   objeto:  conexion realizadaa a la base de datos
#
# Retorna: lista_monitoreo -- lista de tuplas con la idUsuario, user y password
#                           [(idUsuario,user,password)]
#--------------------------------------------------------------------------------------------        
        
def consultar_usuarios_monitoreo(conexion):
    #realizar solo si la conexion es exitosa
    if conexion!=-1:
        cursor=conexion.cursor()    #crear cursor

        #Ejecutar Query para seleccionar a los administradores
        cursor.execute("SELECT idUsuario,user,password FROM usuarios WHERE tipo='monitoreo'")
        lista_monitoreo=list(cursor.fetchall()) 
        cursor.close()
        conexion.commit()
        
        return lista_monitoreo

#===================================================================
# cerrar_conexion: realiza el cierre de la conexion de MySQL
# Parametros: ninguno
# Retorna: nada
#------------------------------------------------------------------
def cerrar_conexion(conexion):
    conexion.close()




    
