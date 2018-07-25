#validar una ip entre el rango de 0 a 255

def validarFormatoIP(ipAddress):
 # Validar el ingreso de la dirreccion ip, que contenga los cuatro octetos y que cada uno este dentro del rango(0-255)
 flag=False
 try:
     if (len(ipAddress.split("."))) != 4:
         print("ERROR: Ingrese una direcccion IP valida!!!")
     elif (int(ipAddress.split(".")[0]) < 0 or int(ipAddress.split(".")[0]) > 255):
         print("ERROR: Ingrese una direcccion IP valida!!!")
     elif (int(ipAddress.split(".")[1]) < 0 or int(ipAddress.split(".")[1]) > 255):
         print("ERROR: Ingrese una direcccion IP valida!!!")
     elif (int(ipAddress.split(".")[2]) < 0 or int(ipAddress.split(".")[2]) > 255):
         print("ERROR: Ingrese una direcccion IP valida!!!")
     elif (int(ipAddress.split(".")[3]) < 0 or int(ipAddress.split(".")[3]) > 255):
         print("Ingrese una direcccion IP (valida!!!")
     else:
         flag=True
 except ValueError:
     print("ERROR: La direccion IP debe ser numerica")

 return(flag)
