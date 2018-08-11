
import wx.xrc


from ConfiguracionBGP.Ventanas.ventana_Emergente import *

app = wx.App(False)
frame_pantalla_login = pantalla_login(None)
frame_pantalla_Opciones= pantalla_Opciones(None)
frame_configurar_BGP = configurar_BGP(None)
frame_pantalla_login.Show(True)
app.MainLoop()

if(pantalla_login.salir):
    print("Salir")
    frame_pantalla_login.Destroy()

    #



