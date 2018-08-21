from tkinter import *
from tkinter import ttk
from auxiliares import *
import conexion_mysql as sql
import time as tm
import datetime as dtime

#===============================================================================
#inicio: ventana de login principal
#Parametros:
#
# conexion (objeto): conexion realizadaa a la base de datos
#
# Retorna: nada
#-------------------------------------------------------------------------------
def inicio(conexion):
    
    #===============================================================================
    #enviar: funcion interna que ejecuta el botón enviar
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------
    def enviar():
        #obtiene usuario y contraseña de los formularios
        password=passwd.get()
        user=usuario.get()

        #Usa la funcion de validacion de sesion
        if sql.validar_sesion(conexion,user,password):
            #Caso en que el usuario ingresa correctamente
            
            #Establece variable global de sesion
            global sesion
            sesion= sql.establecer_sesion(conexion,user,password)

            #Cierra la ventana inicial
            root.destroy()

            #Llama a la ventana de dispositivos
            ventana_dispositivos(conexion)
            
        elif password=="" or user=="":
            #Caso en que se dejan campos vacios, llama a la ventana de campos vacios
            error_campos_vacios()
        else:
            #Caso en el que el usuario no ingresa correctamente
            error_sesion()
            
    #Declaracion del contenedor principal    
    root=Tk()
    root.title("Aplicacion BGP - Iniciar Sesión")
    root.geometry("600x400+400+200")

    #Configuraciones del contenedor principal
    root.config(bg="blue")
    root.resizable(0,0)
    fondo=PhotoImage(file="prueba.png")
    Label(root,image=fondo).place(x=0,y=0)
   
    #Declaracion del contenido de la ventana
    frame=Frame(root,width=600,height=480,pady=100,padx=100)
    frame.pack()
        
    #Etiqueta de titulo
    titulo_label=Label(frame,text="ASISTENTE PARA CONFIGURACION BGP",fg="#0431B4",font=("Helvetica", 12))
    titulo_label.place(x=-20,y=-20)

    #Campo de formulario del usuario
    usuario=Entry(frame)
    usuario.grid(row=1,column=2, sticky="e", padx=10, pady=10)
    usuario_label=Label(frame,text="Usuario: ")
    usuario_label.grid(row=1,column=1, sticky="e", padx=7, pady=10)
    
    #Campo de formulario de la contraseña
    passwd=Entry(frame)
    passwd.grid(row=2,column=2, sticky="e", padx=10, pady=10)
    passwd.config(show="*") #mostrar * en lugar de texto
    passwd_label=Label(frame,text="Contraseña: ")
    passwd_label.grid(row=2,column=1, sticky="e", padx=7, pady=10)

    #Boton para el envio de datos
    boton=Button(frame,text="Iniciar Sesion")
    boton.grid(row=3,column=2, padx=10, pady=10)
    boton.config(bg="#2E9AFE",fg="white",command=enviar) #cuando pulse, ejecutar la funcion enviar

    #Ejecucion de la ventana
    root.mainloop()


#===============================================================================
# error_sesion: ventana en la que se muestra si ocurrio error de sesion
# Parametros: ninguno
# Retorna: nada
#-------------------------------------------------------------------------------    
def error_sesion():

    #===============================================================================
    #enviar: funcion interna que ejecuta el botón aceptar
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------
    def aceptar():
        #Cuando el boton es presionado, cierra la ventana
        root.destroy()
        
    #Declaracion del contenedor principal      
    root=Toplevel()
    root.title("Error")
    root.geometry("400x80+500+350")
    root.resizable(0,0)

    #Declaracion del contenido de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()

    #Etiqueta con el mensaje de error
    error_label=Label(frame,text="No se pudo establecer sesión, usuario o contraseña incorrectos")
    error_label.grid(row=0,column=1)

    #Imagen de X para representar el error
    errorimg=PhotoImage(file="error.png")
    Label(frame,image=errorimg).grid(row=0,column=0)

    #Boton para cerrar la ventana
    boton=Button(frame,text="Aceptar")
    boton.grid(row=1,column=1)
    boton.config(bg="#2E9AFE",fg="white",command=aceptar) #cuando se presiona, ejecuta la funcion aceptar

    #Ejecucion de la ventana
    root.mainloop()
    
#===============================================================================
# error_servidor: ventana en la que se muestra si ocurrio error en la conexion del servidor
# Parametros: ninguno
# Retorna: nada
#------------------------------------------------------------------------------- 
def error_servidor():

    #===============================================================================
    #enviar: funcion interna que ejecuta el botón aceptar
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------
    def aceptar():
        #Cuando el boton es presionado, cierra la ventana
        root.destroy()
        
    #Declaracion del contenedor principal    
    root=Tk()
    root.title("Error")
    root.geometry("400x80+500+350")
    root.resizable(0,0)

    #Declaracion del contenido de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()

    #Etiqueta con el mensaje de error
    error_label=Label(frame,text="No se pudo conectar con el servidor, intentelo más tarde")
    error_label.grid(row=0,column=1)

    #Imagen de X para representar el error
    errorimg=PhotoImage(file="error.png")
    Label(frame,image=errorimg).grid(row=0,column=0)

    #Boton para cerrar la ventana
    boton=Button(frame,text="Aceptar")
    boton.grid(row=1,column=1)
    boton.config(bg="#2E9AFE",fg="white",command=aceptar) #cuando se presiona, ejecuta la funcion aceptar

    #Ejecucion de la ventana
    root.mainloop()


#===============================================================================
# error_servidor: ventana en la que se muestra si ocurrio error en la conexion del servidor
# Parametros: ninguno
# Retorna: nada
#------------------------------------------------------------------------------- 
def error_campos_vacios():

    #===============================================================================
    #enviar: funcion interna que ejecuta el botón aceptar
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------
    def aceptar():
        #Cuando el boton es presionado, cierra la ventana
        root.destroy()
        
    #Declaracion del contenedor principal    
    root=Toplevel()
    root.title("Error")
    root.geometry("300x80+550+350")
    root.resizable(0,0)

    #Declaracion del contenido de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()

    #Etiqueta con el mensaje de error
    error_label=Label(frame,text="Falta información a rellenar en los formularios")
    error_label.grid(row=0,column=1)

    #Imagen de X para representar el error
    errorimg=PhotoImage(file="error.png")
    Label(frame,image=errorimg).grid(row=0,column=0)

    #Boton para cerrar la ventana
    boton=Button(frame,text="Aceptar")
    boton.grid(row=1,column=1)
    boton.config(bg="#2E9AFE",fg="white",command=aceptar)
    
    #Ejecucion de la ventana
    root.mainloop()

#===============================================================================
# error_asn: ventana en la que se muestra si ocurrio error en los rangos ASN
# Parametros: ninguno
# Retorna: nada
#------------------------------------------------------------------------------- 
def error_asn():
    
    #===============================================================================
    #enviar: funcion interna que ejecuta el botón aceptar
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------
    def aceptar():
        #Cuando el boton es presionado, cierra la ventana
        root.destroy()
        
    #Declaracion del contenedor principal     
    root=Toplevel()
    root.title("Error")
    root.geometry("300x80+550+350")
    root.resizable(0,0)

    #Declaracion del contenido de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()

    #Etiqueta con el mensaje de error
    error_label=Label(frame,text="Rango de ASN incorrecto")
    error_label.grid(row=0,column=1)

    #Imagen de X para representar el error
    errorimg=PhotoImage(file="error.png")
    Label(frame,image=errorimg).grid(row=0,column=0)

    #Boton para cerrar la ventana
    boton=Button(frame,text="Aceptar")
    boton.grid(row=1,column=1)
    boton.config(bg="#2E9AFE",fg="white",command=aceptar)

    #Ejecucion de la ventana
    root.mainloop()


#===============================================================================
# error_asn_dispositivo: ventana en la que se muestra si ocurrio error en los rangos ASN en
#                        un dispositivo
# Parametros:
#   dispositivo (str): string con el nombre del dispositivo
# Retorna: nada
#------------------------------------------------------------------------------- 
def error_asn_dispositivo(dispositivo):
    
    #===============================================================================
    #enviar: funcion interna que ejecuta el botón aceptar
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------
    def aceptar():
        #Cuando el boton es presionado, cierra la ventana
        root.destroy()
        
    #Declaracion del contenedor principal     
    root=Toplevel()
    root.title("Error")
    root.geometry("350x80+500+350")
    root.resizable(0,0)

    #Declaracion del contenido de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()

    #Etiqueta con el mensaje de error
    error_label=Label(frame,text="Rango de ASN incorrecto para el dispositivo {}".format(dispositivo))
    error_label.grid(row=0,column=1)

    #Imagen de X para representar el error
    errorimg=PhotoImage(file="error.png")
    Label(frame,image=errorimg).grid(row=0,column=0)

    #Boton para cerrar la ventana
    boton=Button(frame,text="Aceptar")
    boton.grid(row=1,column=1)
    boton.config(bg="#2E9AFE",fg="white",command=aceptar)

    #Ejecucion de la ventana
    root.mainloop()

#===============================================================================
# error_telnet: ventana en la que se muestra si ocurrio error en la conexion
#               telnet
# Parametros:
#   dispositivo (str): string con el nombre del dispositivo
# Retorna: nada
#-------------------------------------------------------------------------------     
def error_telnet(dispositivo):

    #===============================================================================
    #enviar: funcion interna que ejecuta el botón aceptar
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------
    def aceptar():
        #Cuando el boton es presionado, cierra la ventana
        root.destroy()
        
    #Declaracion del contenedor principal     
    root=Toplevel()
    root.title("Error")
    root.geometry("350x80+530+350")
    root.resizable(0,0)

    #Declaracion del contenido de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()

    #Etiqueta con el mensaje de error
    error_label=Label(frame,text="Falla en la conexion del dispositivo {}, intentelo mas tarde".format(dispositivo))
    error_label.grid(row=0,column=1)

    #Imagen de X para representar el error
    errorimg=PhotoImage(file="error.png")
    Label(frame,image=errorimg).grid(row=0,column=0)

    #Boton para cerrar la ventana
    boton=Button(frame,text="Aceptar")
    boton.grid(row=1,column=1)
    boton.config(bg="#2E9AFE",fg="white",command=aceptar)

    #Ejecucion de la ventana
    root.mainloop()

#===============================================================================
# ventana_exitosa: ventana en la que se muestra si la configuracion fue exitosa
# Parametros:
#   dispositivoL (str): string con el nombre del dispositivo local
#   asnL (str): string con el ASN del dispositivo local
#   dispositivoR (str): string con el nombre del dispositivo remoto
#   asnR (str): string con el ASN del dispositivo local
#
# Retorna: nada
#-------------------------------------------------------------------------------  
def ventana_exitosa(dispositivoL,asnL,dispositivoR,asnR):

    #===============================================================================
    #enviar: funcion interna que ejecuta el botón aceptar
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------
    def aceptar():
        root.destroy()
        
    #Declaracion del contenedor principal     
    root=Toplevel()
    root.title("Error")
    root.geometry("800x80+530+350")
    root.resizable(0,0)

    #Declaracion del contenido de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()

    #Etiqueta con el mensaje de exito
    exito_label=Label(frame,text="Configuracion exitosa en el dispositivo {} con ASN {} y el dispositivo {} con ASN {}".format(dispositivoL,asnL,dispositivoR,asnR))
    exito_label.grid(row=0,column=1)

    #Imagen de check para representar el exito
    ok_img=PhotoImage(file="visto.png")
    Label(frame,image=ok_img).grid(row=0,column=0)

    #Boton para cerrar la ventana
    boton=Button(frame,text="Aceptar")
    boton.grid(row=1,column=1)
    boton.config(bg="#2E9AFE",fg="white",command=aceptar)

    #Ejecucion de la ventana
    root.mainloop()

#===============================================================================
# error_ip: ventana en la que se muestra si la direcion IP no es valida
# Parametros:
#   tipo (str): string que indica si el mensaje es para IP o mask , (default: ip)
# Retorna: nada
#-------------------------------------------------------------------------------
def error_ip(tipo="both"):
    
    #===============================================================================
    #enviar: funcion interna que ejecuta el botón aceptar
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------
    def aceptar():
        root.destroy()

    #Declaracion del contenedor principal     
    root=Toplevel()
    root.title("Error")
    root.geometry("350x80+530+350")
    root.resizable(0,0)

    #Declaracion del contenido de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()

    #eleccion del mensaje
    if tipo=="ip":
        mensaje="La direccion IP no es valida"
    elif tipo=="mask":
        mensaje="La mascara de red no es valida"
    else: 
        mensaje="Las direcciones IP no son validas"
        
    #Etiqueta con el mensaje de exito    
    error_label=Label(frame,text=mensaje)
    error_label.grid(row=0,column=1)

    #Etiqueta con el mensaje de error
    errorimg=PhotoImage(file="error.png")
    Label(frame,image=errorimg).grid(row=0,column=0)

    #Boton para cerrar la ventana
    boton=Button(frame,text="Aceptar")
    boton.grid(row=1,column=1)
    boton.config(bg="#2E9AFE",fg="white",command=aceptar)

    #Ejecucion de la ventana
    root.mainloop()


#===============================================================================
#ventana_dispositivos: ventana de eleccion de dispositivos
#Parametros:
#
# conexion (objeto): conexion realizadaa a la base de datos
#
# Retorna: nada
#-------------------------------------------------------------------------------
def ventana_dispositivos(conexion):

    #===============================================================================
    # listas_empresa_par: funcion interna que retorna las listas paralelas id_dispo,ldispo,l_gateway
    # Parametros:
    #  id_empresa (str): id de la empresa a buscar
    # Retorna:
    #  id_dispo (lista): id de los dispositivos
    #  ldispo (lista): nombre de los dispositivos
    #  l_gateway (lista): IP asociada al dispositivo
    #-------------------------------------------------------------------------------
    def listas_empresa_par(id_empresa):

        #Obtener los dispositivos a los que puede acceder el usuario que ha iniciado sesion
        # segun una empresa solicitada
        ldispositivos=sql.consultar_devices_empresa(conexion,sesion,id_empresa) #[(idDispositivo, nombre, gateway)]
        
        #Declarar las listas paralelas
        id_dispo=[]
        ldispo=[]
        l_gateway=[]

        #Llenar las listas paralelas con la informacion de la consulta
        for idD,nom,gat in ldispositivos:
            id_dispo.append(idD)
            ldispo.append(nom)
            l_gateway.append(gat)
            
        return  id_dispo,ldispo,l_gateway

    #===============================================================================
    # buscarASN: funcion interna que retorna el ASN de una empresa segun su ID
    # Parametros:
    #  id_empresa (str): id de la empresa a buscar
    # Retorna:
    #  ASNs (str): ASN de la empresa
    #-------------------------------------------------------------------------------
    def buscarASN(id_empresa):
        
        ids_empresas,nombres,ASNs=sql.all_empresas(conexion)
        for i in range(len(ASNs)):
            if ids_empresas[i]==id_empresa:
                return ASNs[i]
            

    #===============================================================================
    # llenarL: funcion que llena la lista desplegable de los dispositivos y ASN segun
    #          se elija la empresa local
    # Parametros:
    #  event (event): evento de la libreria tkinter
    # Retorna: nada
    #-------------------------------------------------------------------------------
    def llenarL(event):
        #obtiene el nombre de la empresa y su id a traves de la eleccion en la lista desplegable
        nombreE=combo_empresaL.get()
        i=lcombo.index(nombreE)
        id_empresa=id_empresas[i]

        #obtiene las listas paralelas de la informacion de la empresa
        id_dispo,ldispo,l_gateway=listas_empresa_par(id_empresa) #[idDispositivo], [nombre], [gateway]

        #si se ha seleccionado una empresa
        if len(ldispo)!=0:

            #Se asigna a la lista de dispositivos locales los dispositivos de la empresa seleccionada
            combo_dispositivoL["values"]=ldispo
            combo_dispositivoL.current(0)  #selecciona el primer dispositivo de la lista

            #Llena el campo ASN de la empresa seleccionada
            asn=buscarASN(id_empresa)
            asnL.delete(0,END)
            asnL.insert(0,asn)

    #===============================================================================
    # llenarR: funcion que llena la lista desplegable de los dispositivos y ASN segun
    #          se elija la empresa remota
    # Parametros:
    #  event (event): evento de la libreria tkinter
    # Retorna: nada
    #-------------------------------------------------------------------------------    
    def llenarR(event):
        
        #obtiene el nombre de la empresa y su id a traves de la eleccion en la lista desplegable
        nombreE=combo_empresaR.get()
        i=lcombo.index(nombreE)
        id_empresa=id_empresas[i]

        #obtiene las listas paralelas de la informacion de la empresa
        id_dispo,ldispo,l_gateway=listas_empresa_par(id_empresa) #[idDispositivo], [nombre], [gateway]

        #si se ha seleccionado una empresa
        if len(ldispo)!=0:
            
            #Se asigna a la lista de dispositivos locales los dispositivos de la empresa seleccionada
            combo_dispositivoR["values"]=ldispo
            combo_dispositivoR.current(0) #selecciona el primer dispositivo de la lista

            #Llena el campo ASN de la empresa seleccionada
            asn=buscarASN(id_empresa)
            asnR.delete(0,END)
            asnR.insert(0,asn)


    #===============================================================================
    # configurar: funcion interna que ejecuta la accion al presionar el boton configurar AS.
    #             si los datos son correctos, abrira la ventana de elegir redes, caso contrario
    #             mostrara ventanas de errores
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------     
    def configurar():

        #obtiene los ASN local y remoto
        aslocal=asnL.get()
        asremoto=asnR.get()

        #Obtiene el nombre de la empresa local y remota
        nombreR=combo_empresaR.get()
        nombreL=combo_empresaL.get()

        #Obtiene el nombre del dispositivo local y remoto  
        dispoR=combo_dispositivoR.get()
        dispoL=combo_dispositivoL.get()

        #validaciones segun los campos
        if aslocal=='' or asremoto=='' or nombreL=='' or nombreR=='' or dispoL=='' or dispoR=='':
            #Si al menos uno de los campos queda vacio
            error_campos_vacios()
        elif not validar_ASN(aslocal) and not validar_ASN(asremoto):
            #Si tanto el ASN remoto como local son invalidos
            error_asn()
        elif not validar_ASN(aslocal):
            #Si el ASN local es invalido
            error_asn_dispositivo(dispoL)
        elif not validar_ASN(asremoto):
            #Si el ASN remoto es invalido
            error_asn_dispositivo(dispoR)
        else:
            #Si los datos son correctos

            #obtener el id de la empresa local
            i=lcombo.index(nombreR)
            id_empresaR=id_empresas[i]

            #obtener el id de la empresa remota
            i=lcombo.index(nombreL)
            id_empresaL=id_empresas[i]

            #llamar a la ventana de configuracion de redes
            ventana_redes(aslocal,asremoto,id_empresaL,id_empresaR,dispoL,dispoR,conexion)
        

    #Obtener la informacion de las empresas
    id_empresas,lcombo,l_ASN=sql.all_empresas(conexion)
    
    #Iniciacion de la ventana principal    
    root=Tk()
    root.title("Aplicacion BGP- Escoger Dispositivos")
    root.geometry("900x400+250+100")

    #configuracion de la ventana principal
    root.config(bg="blue")
    root.resizable(0,0)
    fondo2=PhotoImage(file="fondoGrande.png")
    Label(root,image=fondo2).place(x=0,y=0)
   
    #Iniciacion del contenedor de la ventana
    frame=Frame(root,width=600,height=480,pady=100,padx=75)
    frame.pack()

    #etiqueta del titulo   
    titulo_label=Label(frame,text="ESCOGER DISPOSITIVOS",fg="#0431B4",font=("Helvetica", 12))
    titulo_label.place(x=-20,y=-40)

    #Lista desplegable con las empresas locales
    combo_empresaL=ttk.Combobox(frame, state="readonly")
    combo_empresaL["values"]=lcombo
    combo_empresaL.bind("<<ComboboxSelected>>",llenarL)  #Cuando se selecciona una empresa, se llena automaticamente sus dispositivos
    combo_empresaL.grid(row=1,column=2, sticky="e", padx=10, pady=10)

    #Etiqueta para la empresa local
    local_label=Label(frame,text="Empresa Local: ")
    local_label.grid(row=1,column=1, sticky="e", padx=7, pady=10)

    #Lista desplegable de los dispositivos de la empresa local seleccionada 
    combo_dispositivoL=ttk.Combobox(frame, state="readonly")
    combo_dispositivoL["values"]=[]
    combo_dispositivoL.grid(row=2,column=2, sticky="e", padx=10, pady=10)

    #Etiqueta para los dispositivos locales
    dispositivoL=Label(frame,text="Dispositivo Local: ")
    dispositivoL.grid(row=2,column=1, sticky="e", padx=7, pady=10)

    #Campo de formulario para el ASN local
    asnL=Entry(frame)
    asnL.grid(row=3,column=2, sticky="w", padx=10, pady=10)
    asnL_label=Label(frame,text="ASN Local: ")
    asnL_label.grid(row=3,column=1, sticky="e", padx=7, pady=10)

    #Lista desplegable con las empresas remotas
    combo_empresaR=ttk.Combobox(frame, state="readonly")
    combo_empresaR["values"]=lcombo
    combo_empresaR.bind("<<ComboboxSelected>>",llenarR)
    combo_empresaR.grid(row=1,column=5, sticky="e", padx=10, pady=10)

    #Etiqueta para la empresa remota
    remoto_label=Label(frame,text="Empresa Remota: ")
    remoto_label.grid(row=1,column=4, sticky="e", padx=7, pady=10)

    #Lista desplegable de los dispositivos de la empresa remota seleccionada 
    combo_dispositivoR=ttk.Combobox(frame, state="readonly")
    combo_dispositivoR["values"]=[]
    combo_dispositivoR.grid(row=2,column=5, sticky="e", padx=10, pady=10)

    #Etiqueta para los dispositivos remotos
    dispositivoR=Label(frame,text="Dispositivo Remoto: ")
    dispositivoR.grid(row=2,column=4, sticky="e", padx=7, pady=10)

    #Campo de formulario para el ASN remoto
    asnR=Entry(frame)
    asnR.grid(row=3,column=5, sticky="w", padx=10, pady=10)
    asnR_label=Label(frame,text="ASN Remoto: ")
    asnR_label.grid(row=3,column=4, sticky="e", padx=7, pady=10)

    #Boton para configurar la sesion BGP
    boton=Button(frame,text="Configurar AS")
    boton.grid(row=4,column=3)
    boton.config(bg="#2E9AFE",fg="white",command=configurar) #cuando se presiona, llama a la funcion configurar

    #Ejecucion de la ventana
    root.mainloop()

#===============================================================================
# ventana_redes: ventana de configuracion de redes
# Parametros:
#   asnL         (str):    ASN local
#   asnR         (str):    ASN remoto
#   id_empresaL  (str):    ID empresa local
#   id_empresaR  (str):    ID empresa Remota
#   dispositivoL (str):    nombre dispositivo local
#   dispositivoR (str):    nombre dispositivo remota
#   conexion     (objeto): conexion realizada a la base de datos
# Retorna: nada
#-------------------------------------------------------------------------------
def ventana_redes(asnL,asnR,id_empresaL,id_empresaR,dispositivoL,dispositivoR,conexion):

    #===============================================================================
    # hora_actual: funcion interna que devuelve la hora local en formato AA-MM-DD H:M:S 
    # Parametros:
    # ninguno
    # Retorna:
    #    st (str): hora actual formato AA-MM-DD H:M:S
    #------------------------------------------------------------------------------- 
    def hora_actual():
        t=tm.time() #obtiene el tiempo actual
        st=dtime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S') #se le da el formato deseado
        return st

    #===============================================================================
    # escribir_log: funcion interna que escribe en el archivo de log de errores
    # Parametros:
    #   hora         (str):     hora actual
    #   dispositivoL (str):     nombre dispositivo local
    #   asnl         (str):     ASN local
    #   dispositivoR (str):     nombre dispositivo remoto
    #   asnr         (str):     ASN remoto
    #   motivo       (str):     motivo del error
    # Retorna: nada
    #------------------------------------------------------------------------------- 
    def escribir_log(hora,dispositivoL,asnl,dispositivoR,asnr,motivo):
        #abre el archivo, escribe la linea y cierra el archivo
        file=open("logs.txt","a")
        file.write(";".join([hora,dispositivoL,asnl,dispositivoR,asnr,motivo])+"\n")
        file.close()

    #===============================================================================
    # aceptar: funcion interna que ejecuta la accion al presionar el boton aceptar.
    #             si los datos son correctos, abrira configura las redes, caso contrario
    #             mostrara ventanas de errores
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------         
    def aceptar():
        
        #hora actual a la cual se presiono el boton
        hora=hora_actual()
        
        #Obtiene la lista de redes locales y remotas seleccionadas
        redes_locales=redesL.get(0,END)
        redes_remotas=redesR.get(0,END)

        #Validacion: si no hay redes locales o remotas seleccionadas
        if len(redes_locales)==0 or len(redes_remotas)==0:
            #Muestra ventana de error y crea una linea en el archivo de log
            error_campos_vacios()
            escribir_log(hora,dispositivoL,asnL,dispositivoR,asnR,"Se dejo campos vacios")
        else:
            #se eliminar las redes repetidas si existen
            redes_locales=set(redes_locales)
            redes_remotas=set(redes_remotas)
            
            #obtiene los datos de inicio de sesion del usuario
            user=sesion['username']
            contra=sesion['password']

            #Buscar IP asociada a los dispositivos local y remoto en la base de datos
            HOST_Local=sql.buscar_ip_dispositivo(dispositivoL,id_empresaL,conexion)
            HOST_Remoto=sql.buscar_ip_dispositivo(dispositivoR,id_empresaR,conexion)

            #intentar realizar la configuracion
            try:
                #Conexion telnet al dispositivo local
                tn1=conexion_Telnet(HOST_Local,user,contra)
                iniciar_Configuracion(tn1)

                #Configuracion redes de BGP
                BGP.config_Vecino(tn1, HOST_Local,HOST_Remoto, asnL,asnR,redes_locales,redes_remotas,user,contra)

                #Guarda la configuracion en el dispositivo y lanza la ventana de exito
                guardar_Configuracion(tn1)
                ventana_exitosa(dispositivoL,asnL,dispositivoR,asnR)
            except:
                #La conexion telnet fallo, se escribe un log y muestra ventana de error
                escribir_log(hora,dispositivoL,asnL,dispositivoR,asnR,"Fallo la conexion a los dispositivos")
                error_telnet(dispositivoL)
                
            
        
    #===============================================================================
    # agregarL: funcion interna que ejecuta la accion al presionar el boton agregar red
    #             para la empresa local
    #             mostrara ventanas de agregar redes
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------         
    def agregarL():
        id_dispositivo=sql.buscar_id_dispositivo(dispositivoL,id_empresaL,conexion)
        ventana_agregar_red(conexion,id_dispositivo,redesL)

    #===============================================================================
    # modificarL: funcion interna que ejecuta la accion al presionar el boton modificar red
    #             para la empresa local
    #             mostrara ventanas de modificar redes
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------     
    def modificarL():
        #Obtiene la red seleccionada
        indice=redesL.curselection()

        #Validacion para comprobar que se haya seleccionado una red
        if len(indice)!=0:
            
            #Obtiene el indice de la red seleccionada
            indice=indice[0]
            
            #red seleccionada
            seleccion=redesL.get(0,END)[indice]
            
            #mostrar  ventana
            ventana_modificar_red(seleccion,indice,redesL)

    #===============================================================================
    # eliminarL: funcion interna que ejecuta la accion al presionar el boton eliminar red
    #             para la empresa local
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------        
    def eliminarL():
        #Obtiene la red seleccionada
        indice=redesL.curselection()
        
        #Validacion para comprobar que se haya seleccionado una red        
        if len(indice)!=0:
            
            #Obtiene el indice de la red seleccionada
            indice=indice[0]
            redesL.delete(indice)  #elimina la red

    #===============================================================================
    # agregarR: funcion interna que ejecuta la accion al presionar el boton agregar red
    #             para la empresa remota
    #             mostrara ventanas de agregar redes
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------         
    def agregarR():
        id_dispositivo=sql.buscar_id_dispositivo(dispositivoR,id_empresaR,conexion)
        ventana_agregar_red(conexion,id_dispositivo,redesR)

    #===============================================================================
    # modificarR: funcion interna que ejecuta la accion al presionar el boton modificar red
    #             para la empresa remota
    #             mostrara ventanas de modificar redes
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------     
    def modificarR():
        #Obtiene la red seleccionada
        indice=redesR.curselection()
        #Validacion para comprobar que se haya seleccionado una red  
        if len(indice)!=0:
            
            #Obtiene el indice de la red seleccionada
            indice=indice[0]
            
            #red seleccionada
            seleccion=redesR.get(0,END)[indice]
            
            #mostrar  ventana
            ventana_modificar_red(seleccion,indice,redesR)

    #===============================================================================
    # eliminarR: funcion interna que ejecuta la accion al presionar el boton eliminar red
    #             para la empresa remota
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------  
    def eliminarR():
        #Obtiene la red seleccionada
        indice=redesR.curselection()
        
        #Validacion para comprobar que se haya seleccionado una red    
        if len(indice)!=0:
            
            #Obtiene el indice de la red seleccionada
            indice=indice[0]
            redesR.delete(indice)   #elimina la red 

    #Declaracion de la ventana principal    
    root=Toplevel()
    root.title("Ingresar Redes")
    root.geometry("800x500+10+25")
    root.resizable(0,0)

    #Declaracion del contenido de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()
  
    #Lista con las redes locales
    redesL=Listbox(frame,width="30")
    redesL.grid(row=1,column=2, sticky="n", padx=10, pady=10)

    #etiqueta para las redes locales
    redesL_label=Label(frame,text="Redes Locales: ")
    redesL_label.grid(row=1,column=1, sticky="n", padx=7, pady=10)

    #Boton agregar red para la empresa local
    agregarBL=Button(frame,text="Agregar Red")
    agregarBL.grid(row=1,column=3,sticky="n")
    agregarBL.config(bg="#2E9AFE",fg="white",command=agregarL)

    #Boton modificar red para la empresa local
    modificarBL=Button(frame,text="Modificar Red")
    modificarBL.grid(row=1,column=4,sticky="n")
    modificarBL.config(bg="#2E9AFE",fg="white",command=modificarL)

    #Boton eliminar red para la empresa local
    eliminarBL=Button(frame,text="Eliminar Red")
    eliminarBL.grid(row=1,column=5,sticky="n")
    eliminarBL.config(bg="#2E9AFE",fg="white",command=eliminarL)

    #Lista con las redes remotas
    redesR=Listbox(frame,width="30")
    redesR.grid(row=4,column=2, sticky="n", padx=10, pady=10)

    #etiqueta para las redes remotas
    redesR_label=Label(frame,text="Redes Remotas: ")
    redesR_label.grid(row=4,column=1, sticky="n", padx=7, pady=10)

    #Boton agregar red para la empresa remota
    agregarBR=Button(frame,text="Agregar Red")
    agregarBR.grid(row=4,column=3,sticky="n")
    agregarBR.config(bg="#2E9AFE",fg="white",command=agregarR)

    #Boton modificar red para la empresa remota
    modificarBR=Button(frame,text="Modificar Red")
    modificarBR.grid(row=4,column=4,sticky="n")
    modificarBR.config(bg="#2E9AFE",fg="white",command=modificarR)

    #Boton eliminar red para la empresa local
    eliminarBR=Button(frame,text="Eliminar Red")
    eliminarBR.grid(row=4,column=5,sticky="n")
    eliminarBR.config(bg="#2E9AFE",fg="white",command=eliminarR)

    #Boton aceptar para enviar la configuracion
    boton=Button(frame,text="Aceptar")
    boton.grid(row=6,column=2,sticky="n")
    boton.config(bg="#2E9AFE",fg="white",command=aceptar)

    #Ejecucion de la ventana
    root.mainloop()

#===============================================================================
# ventana_agregar_red: ventana de agregacion de redes
# Parametros:
#   conexion        (objeto):   conexion realizada a la base de datos
#   id_dispositivo  (str):      ID dispositivo 
#   listaRedes      (Listbox):  Objeto tkinter para lista de objetos
#
# Retorna: nada
#-------------------------------------------------------------------------------
def ventana_agregar_red(conexion,id_dispositivo,listaRedes):
    #===============================================================================
    # listas_redes_par: funcion interna que retorna las listas paralelas nombres,laddress,l_mask
    # Parametros:
    #  id_dispositivo   (str):        id del dispositivo a buscar
    #   conexion        (objeto):   conexion realizada a la base de datos
    # Retorna:
    #  nombres  (lista): nombre de las interfaces del dispositivo
    #  laddress (lista): direcciones de red de las interfaces
    #  l_mask   (lista): mascara de red de las interfaces
    #-------------------------------------------------------------------------------
    def listas_redes_par(id_dispositivo,conexion):

        #Consulta las interfaces del dispositivo segun la id
        ldispositivos=sql.consultar_interfaces(conexion,id_dispositivo) #[(nombre, ipAddress, mascara)]

        #Creacion de las listas paralelas
        nombres=[]
        laddress=[]
        l_mask=[]

        #Llenado de las listas paralelas segun la consulta a la base de datos
        for nom,ipadd,mask in ldispositivos:
            nombres.append(nom)
            laddress.append(obtener_dir_red(ipadd,mask)) #se obtiene la direccion de red a traves de la funcion obtener_dir_red
            l_mask.append(mask)
        return  nombres,laddress,l_mask

    #===============================================================================
    # llenarMask: funcion que llena el campo de la mascara de subred de la red 
    #             seleccionada
    # Parametros:
    #  event (event): evento de la libreria tkinter
    # Retorna: nada
    #------------------------------------------------------------------------------- 
    def llenarMask(event):
        #Obtener la red seleccionada
        red=combo_interfaz.get()
        
        #obtener la mascara de la red seleccionada
        i=ipAddress.index(red)
        mask=mascara[i]

        #actualizar el campo de la mascara de red    
        mask_entry.delete(0,END)
        mask_entry.insert(0,mask)

    #===============================================================================
    # finalizar: funcion que interna que agrega la red al presionar el boton agregar
    # Parametros: ninguno
    # Retorna: nada
    #-------------------------------------------------------------------------------     
    def finalizar():
        #validar formato de ip
        if not (validar_formato_IP(mask_entry.get())):
            #si la mascara de red no es correcta
            error_ip(tipo="mask")
        else:
            #si los campos con correctos, se agrega la red con su mascara a la lista
            listaRedes.insert(END,combo_interfaz.get()+"-"+mask_entry.get())
            root.destroy() #cierra la ventana

    #declaracion de la ventana principal    
    root=Toplevel()
    root.title("Ingresar Redes")
    root.geometry("650x100+400+300")
    nombre, ipAddress, mascara=listas_redes_par(id_dispositivo,conexion)
    root.resizable(0,0)

    #declaracion del contenedor de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()

    #lista desplegable de las redes
    combo_interfaz=ttk.Combobox(frame, state="readonly")
    combo_interfaz.bind("<<ComboboxSelected>>",llenarMask)
    combo_interfaz["values"]=ipAddress
    combo_interfaz.grid(row=1,column=2, sticky="e", padx=10, pady=10)

    #etiqueta para las direcciones de red
    red_label=Label(frame,text="Direccion de Red: ")
    red_label.grid(row=1,column=1, sticky="e", padx=7, pady=10)

    #campo de formulario para la mascara de subred
    mask_label=Label(frame,text="Mascara de Red: ")
    mask_label.grid(row=1,column=4, sticky="e", padx=7, pady=10)
    mask_entry=Entry(frame)
    mask_entry.grid(row=1,column=5, sticky="e", padx=10, pady=10)

    #boton agregar
    agregar=Button(frame,text="Agregar Red")
    agregar.grid(row=2,column=3,sticky="n")
    agregar.config(bg="#2E9AFE",fg="white",command=finalizar)

    #ejecucion de la ventana
    root.mainloop()
    
#===============================================================================
# ventana_modificar_red: ventana de agregacion de redes
# Parametros:
#   seleccion   (str):   red y mascara de subred seleccionada para modificar
#   indice      (int):      indice que ocupa la red seleccionada
#   listaRedes  (Listbox):  Objeto tkinter para lista de objetos
#
# Retorna: nada
#-------------------------------------------------------------------------------
def ventana_modificar_red(seleccion,indice,listaRedes):

    #===============================================================================
    # modificar: funcion que interna que agrega la red al presionar el boton modificar
    # Parametros: ninguno
    # Retorna: nada
    #------------------------------------------------------------------------------- 
    def modificar():
        #obtiene la nueva red y mascara
        nueva_ip=red.get()
        nueva_mask=mask_entry.get()

        #validar
        if not (validar_formato_IP(nueva_ip)) and not(validar_formato_IP(nueva_mask)):
            #no se ingreso la red ni la mascara correctamente
            error_ip()
        elif not (validar_formato_IP(nueva_ip)):
            #no se ingreso la red correctamente
            error_ip(tipo="ip")
        elif not(validar_formato_IP(nueva_mask)):
            #no se ingreso la mascara correctamente
            error_ip(tipo="mask")
        else:
            #Actualiza en la lista de redes, la nueva red
            listaRedes.delete(indice)
            listaRedes.insert(indice,nueva_ip+"-"+nueva_mask)
            root.destroy()

    #===============================================================================
    # cancelar: funcion que interna que cierra la ventana al presionar el boton cancelar
    # Parametros: ninguno
    # Retorna: nada
    #------------------------------------------------------------------------------- 
    def cancelar():
        root.destroy()

    #separa los datos de la seleccion realizada    
    ipadd,mask=seleccion.split("-")

    #declara la ventana principal
    root=Toplevel()
    root.title("Ingresar Redes")
    root.geometry("700x100+400+300")
    root.resizable(1,1)

    #declara el contenedor de la ventana
    frame=Frame(root,width=500,height=200,padx=15,pady=10)
    frame.pack()

    #etiqueta y campo para la direccion de red
    red_label=Label(frame,text="Direccion de Red: ")
    red_label.grid(row=1,column=1, sticky="e", padx=7, pady=10)
    red=Entry(frame)
    red.grid(row=1,column=2, sticky="e", padx=10, pady=10)
    red.delete(0,END)
    red.insert(0,ipadd)

    #etiqueta y campo para la mascara de red
    mask_label=Label(frame,text="Mascara de Red: ")
    mask_label.grid(row=1,column=5, sticky="e", padx=7, pady=10)
    mask_entry=Entry(frame)
    mask_entry.grid(row=1,column=6, sticky="e", padx=10, pady=10)
    mask_entry.delete(0,END)
    mask_entry.insert(0,mask)

    #boton modificar
    modify=Button(frame,text="Modificar Red")
    modify.grid(row=2,column=3,sticky="n")
    modify.config(bg="#2E9AFE",fg="white",command=modificar)

    #boton cancelar
    cancell=Button(frame,text="Cancelar")
    cancell.grid(row=2,column=4,sticky="n")
    cancell.config(bg="#2E9AFE",fg="white",command=cancelar)

    #ejecucion de la ventana principal
    root.mainloop()

    





