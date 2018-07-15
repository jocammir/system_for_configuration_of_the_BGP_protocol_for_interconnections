# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import easygui as eg
import funciones_telnet

#El software wxFormBuilder define cada frame como una clase

###########################################################################
## Class inicial
###########################################################################

#Clase "inicial", este representa el frame en donde se valida que la direccion IP ingresada mediante teclado por el ususario sea la correcta a la cual se conecta el ordenador donde se ejecuta la aplicacion
class direccionIP(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PROYECTO DE CONMUTACION Y ENRUTAMIENTO",
                          pos=wx.DefaultPosition, size=wx.Size(500, 500),
                          style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer4 = wx.GridBagSizer(0, 0)
        gbSizer4.SetFlexibleDirection(wx.BOTH)
        gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbSizer11 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"INGRESO DE DIRECCCION IP DEL ROUTER"), wx.VERTICAL)

        gbSizer8 = wx.GridBagSizer(0, 0)
        gbSizer8.SetFlexibleDirection(wx.BOTH)
        gbSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText35 = wx.StaticText(sbSizer11.GetStaticBox(), wx.ID_ANY, u"DIRECCION IP", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gbSizer8.Add(self.m_staticText35, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.user = wx.TextCtrl(sbSizer11.GetStaticBox(), wx.ID_ANY, u"0.0.0.0", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.user, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        sbSizer11.Add(gbSizer8, 1, wx.EXPAND, 5)

        gbSizer4.Add(sbSizer11, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.EXPAND, 5)

        sbSizer12 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_staticText34 = wx.StaticText(sbSizer12.GetStaticBox(), wx.ID_ANY, u"VERIFICACION DE DIRECCION IP",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        sbSizer12.Add(self.m_staticText34, 0, wx.ALL, 5)

        #Se establece una imagen seleccionada por el desarrolador de la aplicacion
        self.m_bitmap3 = wx.StaticBitmap(sbSizer12.GetStaticBox(), wx.ID_ANY,
                                         wx.Bitmap("fondo.jpg", wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                         0)
        sbSizer12.Add(self.m_bitmap3, 0, wx.ALL, 5)

        gbSizer4.Add(sbSizer12, wx.GBPosition(1, 3), wx.GBSpan(1, 1), 0, 5)

        #Se genera un boton con el nombre "validar", que una vez presionado procede a realizar la conexion via Telnet al enrutador a configurar
        self.btn_validar = wx.Button(self, wx.ID_ANY, u"VALIDAR", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.btn_validar, wx.GBPosition(6, 2), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        #Se genera un boton con el nombre "SALIR", que tiene la funcion de destruir el frame donde se realiza la validacion de la direccion IP por donde se realiza la conexion via Telnet.
        self.btn_salir1 = wx.Button(self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.btn_salir1, wx.GBPosition(6, 3), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(gbSizer4)
        self.Layout()

        self.Centre(wx.BOTH)
        # Se asocian los eventos de cada boton dentro del frame con su funcion respectiva
        # Connect Events
        self.btn_validar.Bind(wx.EVT_BUTTON, self.validar_IP)
        self.btn_salir1.Bind(wx.EVT_BUTTON, self.salir1)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def validar_IP(self, event):
        #Se intenta realizar la conexion Telnet con el enrutador una vez dado click en el boton "VALIDAR"
        try:
            tn = funciones_telnet.conexion_telnet( str(self.user.GetLineText(0)), "admin", "admin")
            #Se deja la variable "tn" que contiene la conexion Telnet de manera global, para que pueda ser utilizada en cualquier otra funcion dentro del sistema
            global tn
            msg = "CONEXION ESTABLECIDA"
            titulo = "MENSAJE:"
            choices = ["OK"]
            reply = eg.buttonbox(msg, title=titulo, choices=choices)
            frame.Show()
        #En caso de no coincidir la direccion IP ingresade se cae la conexion Telnet y se genera un mensaje de error a traves de la interfaz grafica
        except:
            msg = "ERROR: IMPOSIBLE REALIZAR CONEXION TELNET, DIRECCION IP NO VALIDA"
            titulo = "error"
            choices = ["ok"]
            reply = eg.buttonbox(msg, title=titulo, choices=choices)


    def salir1(self, event):
        frame0.Destroy()


###########################################################################
## Class principal
###########################################################################

#Clase "principal", En este frame de realiza la el login de los usuarios a traves del nombre del usuario y una contraseña establecida por el administrador

class principal(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PROYECTO DE CONMUTACION Y ENRUTAMIENTO",
                          pos=wx.DefaultPosition, size=wx.Size(500, 500),
                          style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer4 = wx.GridBagSizer(0, 0)
        gbSizer4.SetFlexibleDirection(wx.BOTH)
        gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbSizer11 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"LOGIN"), wx.VERTICAL)

        gbSizer8 = wx.GridBagSizer(0, 0)
        gbSizer8.SetFlexibleDirection(wx.BOTH)
        gbSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #Etiqueta
        self.m_staticText35 = wx.StaticText(sbSizer11.GetStaticBox(), wx.ID_ANY, u"USUARIO", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gbSizer8.Add(self.m_staticText35, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        #Se establece por defecto la palabra "user" para guiar al usuario y saber con el valor llenar el campo
        self.user = wx.TextCtrl(sbSizer11.GetStaticBox(), wx.ID_ANY, u"user", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.user, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        # Etiqueta
        self.password1234 = wx.StaticText(sbSizer11.GetStaticBox(), wx.ID_ANY, u"PASSWORD", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.password1234.Wrap(-1)
        gbSizer8.Add(self.password1234, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        #Se establece n valor cualquiera por defecto, debido a que el valor que se ingresa en la variable "password" no es visible en la interfaz grafica
        self.password = wx.TextCtrl(sbSizer11.GetStaticBox(), wx.ID_ANY, u"xxxxxxx", wx.DefaultPosition, wx.DefaultSize,
                                    wx.TE_PASSWORD)
        gbSizer8.Add(self.password, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        sbSizer11.Add(gbSizer8, 1, wx.EXPAND, 5)

        gbSizer4.Add(sbSizer11, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.EXPAND, 5)

        sbSizer12 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        # Etiqueta
        self.m_staticText34 = wx.StaticText(sbSizer12.GetStaticBox(), wx.ID_ANY, u"SISTEMA DE AUTENTICACION",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        sbSizer12.Add(self.m_staticText34, 0, wx.ALL, 5)

        # Se establece una imagen seleccionada por el desarrolador de la aplicacion
        self.m_bitmap3 = wx.StaticBitmap(sbSizer12.GetStaticBox(), wx.ID_ANY,
                                         wx.Bitmap("fondo.jpg", wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.DefaultSize,
                                         0)
        sbSizer12.Add(self.m_bitmap3, 0, wx.ALL, 5)

        gbSizer4.Add(sbSizer12, wx.GBPosition(1, 3), wx.GBSpan(1, 1), 0, 5)

        #Se crea el boton "VALIDAR", que una vez en que se da click se procede a validar usuario y contraseña ingresada
        self.btn_validar = wx.Button(self, wx.ID_ANY, u"VALIDAR", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.btn_validar, wx.GBPosition(6, 2), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        #Se crea el boton "SALIR", que destruye el frame "principal" y por ende se genera la salida del sistema
        self.btn_salir1 = wx.Button(self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.btn_salir1, wx.GBPosition(6, 3), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(gbSizer4)
        self.Layout()

        self.Centre(wx.BOTH)
        # Se asocian los eventos de cada boton dentro del frame con su funcion respectiva
        # Connect Events
        self.btn_validar.Bind(wx.EVT_BUTTON, self.validar_ingreso)
        self.btn_salir1.Bind(wx.EVT_BUTTON, self.salir1)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def validar_ingreso(self, event):
        #Ingreso al documento d extension .txt que contiene a base de datos de los ususario con sus respectivas contraseñas que nos permiten ingresar al sistema
        x = 0
        f = open("base_de_datos.txt", 'r')
        a = f.readlines()
        for linea in a:
            lista = linea.split(',')
            usr = lista[0]
            contra = lista[1]
            contra2 = (contra[0:(len(contra) - 1)])
            if (self.user.GetLineText(0) == usr and self.password.GetLineText(0) == contra2):
                x = 1
        if (x == 1):
            #En caso de coincidir el ususario y contraeña, se abre el frame2, que es el que contiene el menu del sistema
            f.close()
            frame2.Show()

        #Mensaje de error en caso de no coincidir usuario y contraseña o que no exista en la base de datos
        else:
            msg = "ERROR: USUARIO O CONTRASEÑA INCORRECTO"
            titulo = "error"
            choices = ["ok"]
            reply = eg.buttonbox(msg, title=titulo, choices=choices)

    def salir1(self, event):
        #Se destruye el frame "principal" al dar click en el boton "SALIR"
        frame.Destroy()


###########################################################################
## Class opciones
###########################################################################

#Clase "OPCIONES", este frame contiene tres botones, donde podemos escoger una de las opciones para poder realizar la configuracion que se requiere dentro del enrutador a la cual se accedio via Telnet

class opciones(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"BIENVENIDOS", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        # Etiqueta
        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"ELIJA UNA OPCION A REALIZAR", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText5.Wrap(-1)
        bSizer2.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer2.AddSpacer(5)

        #Creacion del boton "CONFIGURACION BASICA"
        self.btn_con_basica = wx.Button(self, wx.ID_ANY, u"CONFIGURACION BASICA", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_con_basica, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.AddSpacer(5)

        # Creacion del boton "CONFIGURAR BGP"
        self.btn_bgp = wx.Button(self, wx.ID_ANY, u"CONFIGURAR BGP", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_bgp, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.AddSpacer(5)

        # Creacion del boton "SALIR"
        self.btn_salir = wx.Button(self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_salir, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.AddSpacer(5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)
        # Se asocian los eventos de cada boton dentro del frame con su funcion respectiva
        # Connect Events
        self.btn_con_basica.Bind(wx.EVT_BUTTON, self.configuracion_basica)
        self.btn_bgp.Bind(wx.EVT_BUTTON, self.configurar_bgp)
        self.btn_salir.Bind(wx.EVT_BUTTON, self.salir2)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    #Una vez que se de click en el boton "CONFIGURACION BASICA", se realiza la transicion al frame3, donde se procedera a configurar la plantilla basica en el enrutador
    def configuracion_basica(self, event):
        temp = frame.IsBeingDeleted()
        print(temp)
        if (temp != True):
            frame3.Show()
        else:
            frame3.Show()

    #Un vez dado click en el boton "CONFIGURAR BGP", se hace la transicion al frame4, donde tendremos las opciones para configurar la sesion BGP en el enrutador
    def configurar_bgp(self, event):
        frame4.Show()
    #Cuando se da click en el boton "SALIR", se dstruye el frame2, donde se contiene el menu del sistema
    def salir2(self, event):
        frame2.Destroy()
        frame.Destroy()


###########################################################################
## Class op1
###########################################################################

#Clase "op1", este frame corresponde al de configuracion basica, donde a traves de un nombre establecido por el ususario, se realiza la configuracion basica en el enrutador

class op1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"CONFIGURACION BASICA", pos=wx.DefaultPosition,
                          size=wx.Size(562, 356), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Etiqueta
        self.m_staticText26 = wx.StaticText(self, wx.ID_ANY,
                                            u"--*-- UD VA A REALIZAR LA CONFIGURACION BASICA DEL ROUTER --*--",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)
        gbSizer3.Add(self.m_staticText26, wx.GBPosition(0, 3), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"CONFIGURAR"), wx.VERTICAL)

        # Etiqueta
        self.m_staticText27 = wx.StaticText(sbSizer6.GetStaticBox(), wx.ID_ANY, u"INGRESE EL HOSTNAME",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText27.Wrap(-1)
        sbSizer6.Add(self.m_staticText27, 0, wx.ALL, 5)
        #Se crea un cuadro de texto con el nombre "hostname", que es el nombre ingresado por el usuario y con el cual se configurara el enrutador
        self.hostname = wx.TextCtrl(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        sbSizer6.Add(self.hostname, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        #Se crea el boton "CONFIGURACION BASICA" de manera grafica
        self.btn_configuracion_basica = wx.Button(sbSizer6.GetStaticBox(), wx.ID_ANY, u"CONFIGURACION BASICA",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer6.Add(self.btn_configuracion_basica, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer3.Add(sbSizer6, wx.GBPosition(3, 3), wx.GBSpan(1, 1),
                     wx.EXPAND | wx.SHAPED | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer8 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        #Se crea el boton "SALIR" de manera grafica
        self.btn_salir1 = wx.Button(sbSizer8.GetStaticBox(), wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer8.Add(self.btn_salir1, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer8.AddSpacer(5)

        #Se crea el boton "REGRESAR" de manera grafica
        self.btn_regresar = wx.Button(sbSizer8.GetStaticBox(), wx.ID_ANY, u"REGRESAR", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        sbSizer8.Add(self.btn_regresar, 0, wx.ALL | wx.BOTTOM | wx.EXPAND, 5)

        sbSizer8.AddSpacer(5)

        gbSizer3.Add(sbSizer8, wx.GBPosition(5, 3), wx.GBSpan(1, 1),
                     wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.SetSizer(gbSizer3)
        self.Layout()

        self.Centre(wx.BOTH)
        #Se asocian los eventos de cada boton dentro del frame con su funcion respectiva
        # Connect Events
        self.btn_configuracion_basica.Bind(wx.EVT_BUTTON, self.realizar_conf_bas)
        self.btn_salir1.Bind(wx.EVT_BUTTON, self.salir3)
        self.btn_regresar.Bind(wx.EVT_BUTTON, self.returned1)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class

    #una vez dado click en el boton "CONFIGURACION BASICA", se ejecuta la funcion "configuracionBasica" importada del archivo "funcionesTelnet.py"
    def realizar_conf_bas(self, event):
        host = str(self.hostname.GetLineText(0))
        if (host != ""):
            funciones_telnet.configuracionBasica(tn, host)
            #Se muestra un mnesaje en caso de que se realice la configuracion basica del enrutador
            msg = "CONFIGURACION BASICA ESTABLECIDA"
            titulo = "MENSAJE:"
            choices = ["OK"]
            reply = eg.buttonbox(msg, title=titulo, choices=choices)
        else:
            #En caso de no haber ingreado ningun nombre del host, se emite un mensaje de error de manera grafica
            msg1 = "no se ha ingresado hostname";
            titulo1 = "error"
            choices1 = ["ok"]
            reply = eg.buttonbox(msg1, title=titulo1, choices=choices1)

        frame.Show()

    #Al dar click en el boton "SALIR", se destruyen el frame, frame2 y frame3 que son las ventanas anteriores del sistema
    def salir3(self, event):
        frame.Destroy()
        frame2.Destroy()
        frame3.Destroy()

    #Al dar click en el boton "REGRESAR" se regresa se destruye el frame3 y quedamos en el frame anterior de opciones
    def returned1(self, event):
        frame3.Destroy()


###########################################################################
## Class op2
###########################################################################

#Clase "op2", este frame contiene los requerimientos dados para la creacion de este sistema, en el consta los pasos para la configuracion de una sesion BGP de un enrutador

class op2(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"CONFIGURACION BGP", pos=wx.DefaultPosition,
                          size=wx.Size(779, 598), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Etiqueta
        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY,
                                            u"--*-- UD VA A CONFIGURAR EL PROTOCOLO DE ENRUTAMIENTO BGP --*-- ",
                                            wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText12.Wrap(-1)
        gbSizer2.Add(self.m_staticText12, wx.GBPosition(2, 1), wx.GBSpan(1, 10),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        # Etiqueta que indica el primer paso a configurar
        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"NUMERO DE AS  "), wx.VERTICAL)

        #Etiqueta
        self.m_staticText14 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"INGRESE EL NUMERO DE AS LOCAL",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        sbSizer2.Add(self.m_staticText14, 0, wx.ALL, 5)

        self.numero_as_local = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, u"25000", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        sbSizer2.Add(self.numero_as_local, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        # Etiqueta
        self.m_staticText15 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"INGRESE EL NUMERO DE AS REMOTO",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        sbSizer2.Add(self.m_staticText15, 0, wx.ALL, 5)

        self.numero_as_remoto = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, u"25001", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        sbSizer2.Add(self.numero_as_remoto, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_guardar_as = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"GUARDAR AS", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        sbSizer2.Add(self.btn_guardar_as, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.mostrar = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, wx.TE_READONLY)
        sbSizer2.Add(self.mostrar, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer2.Add(sbSizer2, wx.GBPosition(4, 2), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.EXPAND | wx.SHAPED, 5)

        # Etiqueta que indica el segundo paso a configurar
        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"CONFIGURAR VECINDAD"), wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"INGRESE LA DIRECCION IP DEL VECINO",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        sbSizer3.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.ip_vecino = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, u"10.10.10.10", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        sbSizer3.Add(self.ip_vecino, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_configurar_vecino = wx.Button(sbSizer3.GetStaticBox(), wx.ID_ANY, u"CONFIGURAR VECINO",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer3.Add(self.btn_configurar_vecino, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer2.Add(sbSizer3, wx.GBPosition(4, 4), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.EXPAND | wx.SHAPED, 5)

        self.btn_regresar2 = wx.Button(self, wx.ID_ANY, u"REGRESAR", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btn_regresar2, wx.GBPosition(10, 4), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_salir3 = wx.Button(self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.btn_salir3, wx.GBPosition(10, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        # Etiqueta que indica el tercer paso a configurar
        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"CONFIGURAR REDES"), wx.VERTICAL)

        self.m_staticText19 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"INGRESE LAS REDES A PUBLICAR",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        sbSizer4.Add(self.m_staticText19, 0, wx.ALL, 5)

        self.network = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, u"10.10.10.0", wx.DefaultPosition,
                                   wx.Size(-1, -1), 0)
        sbSizer4.Add(self.network, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_configurar_redes = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"CONFIGURAR REDES",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer4.Add(self.btn_configurar_redes, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer2.Add(sbSizer4, wx.GBPosition(8, 3), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.SetSizer(gbSizer2)
        self.Layout()

        self.Centre(wx.BOTH)
        #Se asocian los eventos de cada boton dentro del frame con su funcion respectiva
        # Connect Events
        self.btn_guardar_as.Bind(wx.EVT_BUTTON, self.guardarAS)
        self.btn_configurar_vecino.Bind(wx.EVT_BUTTON, self.vecinosGP)
        self.btn_regresar2.Bind(wx.EVT_BUTTON, self.returned2)
        self.btn_salir3.Bind(wx.EVT_BUTTON, self.salir4)
        self.btn_configurar_redes.Bind(wx.EVT_BUTTON, self.con_red)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    #Dado click en el boton de "GUARDAR AS", se emiten las lineas de comandos a traves de la funcion "SesionBGP" del archivo "funcionesTelnet.py"
    def guardarAS(self, event):
        local = str(self.numero_as_local.GetLineText(0))
        remoto = str(self.numero_as_remoto.GetLineText(0))
        if (local != "") and (remoto != ""):
            self.mostrar.SetValue("Local: " + local + " Remoto: " + remoto)
            funciones_telnet.SesionBGP(tn, local)
            print(local)
            print ("Se guardo el as")
            msg = "SE HA GUARDADO CORRECTAMENTE LOS NUMEROS AUTONOMOS"
            titulo = "MENSAJE:"
            choices = ["OK"]
            reply = eg.buttonbox(msg, title=titulo, choices=choices)
        #En caso de que al dar click en el boton "GUARDAR AS" y no se haya ingresado algun valor el sistema mostrara un mensaje de error
        else:
            msg2 = "ERROR: No se ha ingresado AS previamente"
            titulo2 = "error"
            choices2 = ["ok"]
            reply = eg.buttonbox(msg2, title=titulo2, choices=choices2)
            print("error")

    #Al dar click en el boton "CONFIGURAR VECINO", ejecuta la funcion "configurarVecino" alojado dentro del archivo "funcionesTelnet.py"
    def vecinosGP(self, event):
        vecino = str(self.ip_vecino.GetLineText(0))
        local = str(self.numero_as_local.GetLineText(0))
        remoto = str(self.numero_as_remoto.GetLineText(0))

        flag = funciones_telnet.validarFormatoIP(vecino)
        if (flag and local != "" and remoto != ""):
            funciones_telnet.configurarVecino(vecino, local, remoto, tn)
            print("se guardo correntamente")
            #Se muestra de manera grafica un mensaje al usuario de que se ha configurado correntamente el vecino dentro de la sesion BGP
            msg = "SE GUARDO CORRECTAMENTE"
            titulo = "MENSAJE:"
            choices = ["OK"]
            reply = eg.buttonbox(msg, title=titulo, choices=choices)
        #Se valida el ingreso de los datos para proceder a configurar los enrutadores vecinos dentro de la sesion BGP
        else:
            #Si no se ingresa un numero AS el sistema mostrara un error
            if (local == "" and remoto == ""):
                msg = "ERROR: No se ha ingresado AS previamente"
                titulo = "error"
                choices = ["ok"]
                reply = eg.buttonbox(msg, title=titulo, choices=choices)
            #Si no se ingresa la direccion IP del enrutador vecino el sistema muestra un mensaje de error
            else:
                msg = "error ingrese una direccion ip"
                titulo = "error"
                choices = ["ok"]
                reply = eg.buttonbox(msg, title=titulo, choices=choices)

    #Al dar click en el boton "REGRESAR", se destruye el frame4 que es el que contiene los pasos de configuracion de la sesion BGP
    def returned2(self, event):
        frame4.Destroy()
    #Al dar click en el boton "SALIR", se procede a eliminar todos los frames antes abiertos y se realiza la salida del sistema
    def salir4(self, event):
        frame2.Destroy()
        frame.Destroy()
        frame4.Destroy()

    #Al dar click en el boton "CONFIGURAR REDES", se ejecuta la funcion "configurarNetwork" que se aloja en el archivo "funcionesTelnet.py"
    def con_red(self, event):
        red = str(self.network.GetLineText(0))
        #Parametro que nos valida si el formato de la direccion de la red tiene un formato adecuado de los 4 octetos a traves de la funcion "validarFormatoIP" alojada en el archivo "funcionesTelnet.py"
        flag = funciones_telnet.validarFormatoIP(red)
        local = str(self.numero_as_local.GetLineText(0))
        if (flag):
            funciones_telnet.configurarNetwork(tn, red, local)
            print ("Se guardo la conexion de red ")
            msg = "SE GUARDO CORRECTAMENTE"
            titulo = "MENSAJE:"
            choices = ["OK"]
            reply = eg.buttonbox(msg, title=titulo, choices=choices)
        #Se muestra un mensaje de error si el formato ingresado no es el adecuado
        else:
            msg = "ERROR: La dirección IP ingresada es incorrecta"
            titulo = "error"
            choices = ["ok"]
            reply = eg.buttonbox(msg, title=titulo, choices=choices)

app = wx.App(False)
frame0 = direccionIP(None)
frame = principal(None)
frame2 = opciones(None)
frame3 = op1(None)
frame4 = op2(None)
frame0.Show(True)
app.MainLoop()