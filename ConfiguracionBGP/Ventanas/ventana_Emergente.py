import wx
import wx.xrc




class pantalla_login(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PROYECTO DE CONMUTACION Y ENRUTAMIENTO",
                          pos=wx.DefaultPosition, size=wx.Size(500, 250),
                          style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gbSizer4 = wx.GridBagSizer(0, 0)
        gbSizer4.SetFlexibleDirection(wx.BOTH)
        gbSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        sbSizer11 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"LOGIN"), wx.VERTICAL)

        gbSizer8 = wx.GridBagSizer(0, 0)
        gbSizer8.SetFlexibleDirection(wx.BOTH)
        gbSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText35 = wx.StaticText(sbSizer11.GetStaticBox(), wx.ID_ANY, u"USUARIO", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gbSizer8.Add(self.m_staticText35, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.user = wx.TextCtrl(sbSizer11.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer8.Add(self.user, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.password1234 = wx.StaticText(sbSizer11.GetStaticBox(), wx.ID_ANY, u"PASSWORD", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.password1234.Wrap(-1)
        gbSizer8.Add(self.password1234, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.password = wx.TextCtrl(sbSizer11.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize,
                                    wx.TE_PASSWORD)
        gbSizer8.Add(self.password, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        sbSizer11.Add(gbSizer8, 1, wx.EXPAND, 5)

        gbSizer4.Add(sbSizer11, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.EXPAND, 5)

        sbSizer12 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        self.m_staticText34 = wx.StaticText(sbSizer12.GetStaticBox(), wx.ID_ANY, u"SISTEMA DE AUTENTICACION",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        sbSizer12.Add(self.m_staticText34, 0, wx.ALL, 5)



        gbSizer4.Add(sbSizer12, wx.GBPosition(1, 3), wx.GBSpan(1, 1), 0, 5)

        self.btn_validar = wx.Button(self, wx.ID_ANY, u"VALIDAR", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.btn_validar, wx.GBPosition(6, 2), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.btn_salir1 = wx.Button(self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer4.Add(self.btn_salir1, wx.GBPosition(6, 3), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(gbSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        def __del__(self):
            pass

class pantalla_Opciones(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PROYECTO DE CONMUTACION Y ENRUTAMIENTO", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"BIENVENIDOS AL SISTEMA DE CONFIGURARCION DE INTERCONEXION "
                                                            u"ENTRE EMPRESAS O ISP.", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText5.Wrap(-1)
        bSizer2.Add(self.m_staticText5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer2.AddSpacer(5)

        self.btn_con_basica = wx.Button(self, wx.ID_ANY, u"CONFIGURAR BGP", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_con_basica, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.AddSpacer(5)

        self.btn_bgp = wx.Button(self, wx.ID_ANY, u"CONFIGURAR REDES IP", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_bgp, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.AddSpacer(5)

        self.btn_salir = wx.Button(self, wx.ID_ANY, u"SALIR", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.btn_salir, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.AddSpacer(5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)


    def __del__(self):
        pass

class configurar_BGP(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"PROYECTO DE CONMUTACION Y ENRUTAMIENTO", pos=wx.DefaultPosition,
                          size=wx.Size(779, 598), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY,
                                            u"UD VA A CONFIGURAR EL PROTOCOLO DE ENRUTAMIENTO BGP ",
                                            wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText12.Wrap(-1)
        gbSizer2.Add(self.m_staticText12, wx.GBPosition(2, 1), wx.GBSpan(1, 10),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"NUMERO DE AS  "), wx.VERTICAL)

        self.m_staticText14 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"INGRESE EL NUMERO DE AS LOCAL",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        sbSizer2.Add(self.m_staticText14, 0, wx.ALL, 5)

        self.numero_as_local = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        sbSizer2.Add(self.numero_as_local, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText15 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"INGRESE EL NUMERO DE AS REMOTO",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        sbSizer2.Add(self.m_staticText15, 0, wx.ALL, 5)

        self.numero_as_remoto = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        sbSizer2.Add(self.numero_as_remoto, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_guardar_as = wx.Button(sbSizer2.GetStaticBox(), wx.ID_ANY, u"GUARDAR AS", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        sbSizer2.Add(self.btn_guardar_as, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.mostrar = wx.TextCtrl(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.DefaultSize, wx.TE_READONLY)
        sbSizer2.Add(self.mostrar, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer2.Add(sbSizer2, wx.GBPosition(4, 2), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.EXPAND | wx.SHAPED, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"CONFIGURAR VECINDAD"), wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"INGRESE LA DIRECCION IP DEL VECINO",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        sbSizer3.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.ip_vecino = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition,
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

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"CONFIGURAR REDES"), wx.VERTICAL)

        self.m_staticText19 = wx.StaticText(sbSizer4.GetStaticBox(), wx.ID_ANY, u"INGRESE LAS REDES A PUBLICAR",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        sbSizer4.Add(self.m_staticText19, 0, wx.ALL, 5)

        self.network = wx.TextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition,
                                   wx.Size(-1, -1), 0)
        sbSizer4.Add(self.network, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_configurar_redes = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"CONFIGURAR REDES",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        sbSizer4.Add(self.btn_configurar_redes, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer2.Add(sbSizer4, wx.GBPosition(8, 3), wx.GBSpan(1, 1), wx.EXPAND, 5)

        self.SetSizer(gbSizer2)
        self.Layout()

        self.Centre(wx.BOTH)