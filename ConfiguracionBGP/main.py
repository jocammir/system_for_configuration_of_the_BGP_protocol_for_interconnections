
import wx.xrc
from Ventanas.ventana_Emergente import *



app = wx.App(False)
frame = pantalla_Opciones(None)
frame1 = pantalla_login(None)
frame2 = configurar_BGP(None)
frame2.Show(True)
app.MainLoop()
