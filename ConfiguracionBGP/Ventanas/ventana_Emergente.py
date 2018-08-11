import wx
import wx.xrc

class pantalla_login(wx.Frame):
    def __init__(self, parent):
        #Creando la ventana con sus caracterisicas de tamaño y estilo
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PROYECTO DE CONMUTACION Y ENRUTAMIENTO",
                          pos=wx.DefaultPosition, size=wx.Size(600,300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        #Creando particiones del escenario en dichas posiciones
        pant_login_sizer = wx.GridBagSizer(0, 0)
        pant_login_sizer.SetFlexibleDirection(wx.BOTH)
        pant_login_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #Creando un subescenerio que contendra el texto estatico
        login_zone = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"LOGIN LOCAL"), wx.VERTICAL)

        # Creando particiones del escenario en dichas posiciones
        pant_login_sizer2 = wx.GridBagSizer(0, 0)
        pant_login_sizer2.SetFlexibleDirection(wx.BOTH)
        pant_login_sizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #Creando el texto estatico para USUARIO LOCAL con sus caracteristicas
        self.staticText_user_local = wx.StaticText(login_zone.GetStaticBox(), wx.ID_ANY, "USUARIO LOCAL", wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.staticText_user_local.Wrap(-1)
        pant_login_sizer2.Add(self.staticText_user_local, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        #Creando una caja de texto para ingresar el usuario LOCAL
        self.user = wx.TextCtrl(login_zone.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        pant_login_sizer2.Add(self.user, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        # Creando una caja de texto para ingresar el la contraseña del usuario LOCAL
        self.staticText_pass = wx.StaticText(login_zone.GetStaticBox(), wx.ID_ANY, u"PASSWORD", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.staticText_pass.Wrap(-1)

        #Añadiendo al espacio creado el texto de la contraseña
        pant_login_sizer2.Add(self.staticText_pass, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        # Creando una caja de texto para ingresar la contraseña del usuario LOCAL
        self.password = wx.TextCtrl(login_zone.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize,
                                    wx.TE_PASSWORD)
        # Añadiendo al espacio creado el texto de la contraseña
        pant_login_sizer2.Add(self.password, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        #Añadiendo a la particion mas grande la particion mas pequeña que contiene el usuario con su contraseña
        login_zone.Add(pant_login_sizer2, 1, wx.EXPAND, 5)
        #Añadiendo el escenario a la pantalla
        pant_login_sizer.Add(login_zone, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.EXPAND, 5)

        # Creando particiones del escenario en dichas posiciones
        pant_login_sizer3 = wx.GridBagSizer(0,0)
        pant_login_sizer3.SetFlexibleDirection(wx.BOTH)
        pant_login_sizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Creando un subescenerio que contendra el texto estatico
        login_zone_ur = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"LOGIN LOCAL"), wx.VERTICAL)

        # Creando particiones del escenario en dichas posiciones
        pant_login_sizer4 = wx.GridBagSizer(0,0)
        pant_login_sizer4.SetFlexibleDirection(wx.BOTH)
        pant_login_sizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        """//** Creando el texto estatico para USUARIO LOCAL con sus caracteristicas
        self.staticText_user_remoto = wx.StaticText(login_zone.GetStaticBox(), wx.ID_ANY, "USUARIO REMOTO",
                                                   wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.staticText_user_remoto.Wrap(-1)
        pant_login_sizer4.Add(self.staticText_user_remoto, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)
        **// """

        #Creando un titulo a la pantalla con sus caracteristicas y añadiendolo al escenerio
        title_zone = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)
        self.m_staticText34 = wx.StaticText(title_zone.GetStaticBox(), wx.ID_ANY, u"SISTEMA DE AUTENTICACION",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        title_zone.Add(self.m_staticText34, 0, wx.ALL, 5)
        pant_login_sizer.Add(title_zone, wx.GBPosition(1, 3), wx.GBSpan(1, 1), 0, 5)

        #Creando los botones validad y salir
        self.btn_validar = wx.Button(self, wx.ID_ANY, u"VALIDAR", wx.DefaultPosition, wx.DefaultSize, 0)
        pant_login_sizer.Add(self.btn_validar, wx.GBPosition(6, 2), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btn_salir1 = wx.Button(self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0)
        pant_login_sizer.Add(self.btn_salir1, wx.GBPosition(6, 3), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(pant_login_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Conectando los botones antes creados con sus respectivos eventos
        self.btn_validar.Bind(wx.EVT_BUTTON, self.validar_ingreso)
        self.btn_salir1.Bind(wx.EVT_BUTTON, self.salir)

    def __del__(self):
            pass

    #Funciones de los eventos
    def validar_ingreso(self, event):
        print(self.user.GetLineText(0))
        print(self.password.GetLineText(0))
    def salir(self,event):
        print("Salir2")
        #return event
        return True




class pantalla_Opciones(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PROYECTO DE CONMUTACION Y ENRUTAMIENTO", pos=wx.DefaultPosition,
                          size=wx.Size(500, 200), style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        conf_bgp_sizer = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"BIENVENIDOS AL SISTEMA DE CONFIGURARCION DE INTERCONEXION "
                                                            u"ENTRE EMPRESAS O ISP.", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText5.Wrap(-1)
        conf_bgp_sizer.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        conf_bgp_sizer.AddSpacer(5)

        self.btn_bgp = wx.Button(self, wx.ID_ANY, u"CONFIGURAR BGP", wx.DefaultPosition, wx.DefaultSize, 0)
        conf_bgp_sizer.Add(self.btn_bgp, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        conf_bgp_sizer.AddSpacer(5)

        self.btn_redes = wx.Button(self, wx.ID_ANY, u"CONFIGURAR REDES IP", wx.DefaultPosition, wx.DefaultSize, 0)
        conf_bgp_sizer.Add(self.btn_redes, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        conf_bgp_sizer.AddSpacer(5)

        self.btn_salir = wx.Button(self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0)
        conf_bgp_sizer.Add(self.btn_salir, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        conf_bgp_sizer.AddSpacer(5)

        self.SetSizer(conf_bgp_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        #Eventos
        #self.btn_bgp.Bind(wx.EVT_BUTTON, self.configurar_bgp)
    def __del__(self):
        pass

class configurar_BGP(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PROYECTO DE CONMUTACION Y ENRUTAMIENTO", pos=wx.DefaultPosition,
                          size=wx.Size(779, 598), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gconf_bgp_sizer = wx.GridBagSizer(0, 0)
        gconf_bgp_sizer.SetFlexibleDirection(wx.BOTH)
        gconf_bgp_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.staticText_title = wx.StaticText(self, wx.ID_ANY,
                                            u"UD VA A CONFIGURAR EL PROTOCOLO DE ENRUTAMIENTO BGP ",
                                            wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.staticText_title.Wrap(-1)
        gconf_bgp_sizer.Add(self.staticText_title, wx.GBPosition(2, 1), wx.GBSpan(1, 10),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        sconf_bgp_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"NUMERO DE AS  "), wx.VERTICAL)

        self.staticText_numAs = wx.StaticText(sconf_bgp_sizer.GetStaticBox(), wx.ID_ANY, u"INGRESE EL NUMERO DE AS LOCAL",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText_numAs.Wrap(-1)
        sconf_bgp_sizer.Add(self.staticText_numAs, 0, wx.ALL, 5)

        self.numero_as_local = wx.TextCtrl(sconf_bgp_sizer.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        sconf_bgp_sizer.Add(self.numero_as_local, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.staticText_numAsRem = wx.StaticText(sconf_bgp_sizer.GetStaticBox(), wx.ID_ANY, u"INGRESE EL NUMERO DE AS REMOTO",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText_numAsRem.Wrap(-1)
        sconf_bgp_sizer.Add(self.staticText_numAsRem, 0, wx.ALL, 5)

        self.numero_as_remoto = wx.TextCtrl(sconf_bgp_sizer.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        sconf_bgp_sizer.Add(self.numero_as_remoto, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_guardar_as = wx.Button(sconf_bgp_sizer.GetStaticBox(), wx.ID_ANY, u"GUARDAR AS", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        sconf_bgp_sizer.Add(self.btn_guardar_as, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.mostrar = wx.TextCtrl(sconf_bgp_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, wx.TE_READONLY)
        sconf_bgp_sizer.Add(self.mostrar, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gconf_bgp_sizer.Add(sconf_bgp_sizer, wx.GBPosition(4, 2), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.EXPAND | wx.SHAPED, 5)

        vecindad_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"CONFIGURAR VECINDAD"), wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(vecindad_sizer.GetStaticBox(), wx.ID_ANY, u"INGRESE LA DIRECCION IP DEL VECINO",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        vecindad_sizer.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.ip_vecino = wx.TextCtrl(vecindad_sizer.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        vecindad_sizer.Add(self.ip_vecino, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_configurar_vecino = wx.Button(vecindad_sizer.GetStaticBox(), wx.ID_ANY, u"CONFIGURAR VECINO",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        vecindad_sizer.Add(self.btn_configurar_vecino, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gconf_bgp_sizer.Add(vecindad_sizer, wx.GBPosition(4, 4), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.EXPAND | wx.SHAPED, 5)

        self.btn_regresar2 = wx.Button(self, wx.ID_ANY, u"REGRESAR", wx.DefaultPosition, wx.DefaultSize, 0)
        gconf_bgp_sizer.Add(self.btn_regresar2, wx.GBPosition(10, 4), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_salir3 = wx.Button(self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0)
        gconf_bgp_sizer.Add(self.btn_salir3, wx.GBPosition(10, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        conf_red_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"CONFIGURAR REDES"), wx.VERTICAL)

        self.staticText_red_pub = wx.StaticText(conf_red_sizer.GetStaticBox(), wx.ID_ANY, u"INGRESE LAS REDES A PUBLICAR",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticText_red_pub.Wrap(-1)
        conf_red_sizer.Add(self.staticText_red_pub, 0, wx.ALL, 5)

        self.network = wx.TextCtrl(conf_red_sizer.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition,
                                   wx.Size(-1, -1), 0)
        conf_red_sizer.Add(self.network, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_configurar_redes = wx.Button(conf_red_sizer.GetStaticBox(), wx.ID_ANY, u"CONFIGURAR REDES",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        conf_red_sizer.Add(self.btn_configurar_redes, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gconf_bgp_sizer.Add(conf_red_sizer, wx.GBPosition(8, 3), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.SetSizer(gconf_bgp_sizer)
        self.Layout()

        self.Centre(wx.BOTH)






