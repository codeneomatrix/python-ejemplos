
#!/usr/bin/env python
# -*- coding: utf-8 -*-
                        #InfoSistema.py
                      
__author__  = "Wilmer Morel Martinez <wilmermorelmartinez@gmail.com>"
__blog__    = "http://elidiomadelaciencia.blogspot.com/"
__licence__ = "GPL"
                      

import os
import commands
import datetime

#DEPENDENCIAS = geoiplookup del paquete geoip-bin para saber el pais por medio de la IP

#Modulo para Obtener informacion del sistama operativo.
class InfoSistema():
    """Clase para obtener informacion del sistema operativo actual."""
    def GetIpPublica(self):
        """Obtiene la ip publica del sistema, mediante una lectura a la pagina
        web www.showmyip.com extrayendo de ella la ip publica mostrada"""
        import re, urllib2
        s = urllib2.urlopen('http://www.showmyip.com').read()#obtenemos el fuente de la pagina
        #Con expresiones regulares se obtiene todo lo que venga despues del 'displaycopy'
        m = re.search('(?<=displaycopy).*', s) #Esta línea es un pedazo de JS que imprime en la página la IP
        ip = m.group(0)
        #Reemplazamos por nada los datos que no sirven
        ip = ip.replace("('", "")
        ip = ip.replace("');", "")
        return ip

    def GetUsuario(self):
        """Obtiene el nombre del usuario actual"""
        usuario = os.getlogin()
        return usuario
      
    def GetNombreSistema(self):
        """Obtiene el nombre del Sistema"""
        nombre = os.name
        return nombre
  
    def GetSistema(self):
        """Obtiene una tupla con el nombre del sistema operativo, nombre del equipo, 
        version del nucleo fecha de lanzamiento, arquitectura"""
        sistema = os.uname()
        return sistema
  
    def GetFecha(self):
        """Obtiene la fecha y hora actual del Sistema"""
        fecha = datetime.datetime.today()
        return fecha
  
    def GetPais(self, IP=None):
        """Obtiene el pais de la ip publica pasada como parametro por medio del programa en consola 'geoiplookp'
        Si no se especifica una IP como parametro, se usara la ip publica del sistema actual asiendo una llamada
        a la funcion interna self.GetIpPublica()"""
        if IP == None:
            IP = self.GetIpPublica()
        pais = commands.getoutput("geoiplookup "+str(IP))
        if pais == "sh: geoiplookup: not found":
            print("El programa geoiplookup para saber el pais por medio de la ip publica, no esta instalado")
            resp = raw_input("Instalar geoiplookup? s/n ") #Opcion para instalar geoiplookup
            if resp.lower() == "s":
                print("Instalando Espere....")
                os.system("sudo apt-get install geoip-bin") #Instalacion del programa geoiplookup
                pais = commands.getoutput("geoiplookup "+str(IP))
                return pais
            else:
                return None #si el programa geoiplookup no esta instalado se devolvera un valor None
        elif len(str(pais)) > 200:
            print("No se pudo obtener el pais para la IP "+str(IP))
            return False #Si no se puede obtener el pais de la direccion ip, se devolvera False
        else:
            return pais


if __name__ == "__main__":
    print (__blog__)
    print (__author__)
    print("......................................................")
    info = InfoSistema()
    funciones={"1":"info.GetIpPublica()", 
               "2":"info.GetUsuario()", 
               "3":"info.GetNombreSistema()", 
               "4":"info.GetSistema()", 
               "5":"info.GetFecha()", 
               "6":"info.GetPais()",
               "7":"exit()"}
    while True:
        print("Elija:....................")
        elegir = raw_input("Ip Publica: 1 \nUsuario: 2 \nNombre del Sistema: 3 \nSistema: 4 \nFecha: 5 \nPais: 6 \nSalir: 7 \n")
        f = funciones[elegir]
        exec "print("+str(f)+")"