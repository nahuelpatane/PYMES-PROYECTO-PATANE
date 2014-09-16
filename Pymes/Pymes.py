#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------Importo Modulos
import sys
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.uic import *
import ConfigParser
#--------------------------------------------Acumulador
acu = 0
#--------------------------------------------Abre la ventana de inicio del programa
class inicio1(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/inicio.ui",self)

#--------------------------------------------Funcion del boton para abrir la ventana de inicio de sesion

    def iniciode(self):
        archivo=claseprin1().show()

        self.close()

#--------------------------------------------Funcion del boton para abrir la ventana de registrarse
    def registrarse(self):
        archivo=registrars().show()
        self.close()

#--------------------------------------------Boton cerrar
    def cancelar(self):
        self.close()
        
        
#--------------------------------------------Abre la ventana de registrarse o formulario  
class registrars(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/formulario.ui",self)
        


#--------------------------------------------Crea un nuevo usuario 
    def registro(self):
        nombre=self.ui.lineEdit.text()
        apellido=self.ui.lineEdit_2.text()
        usuario=self.ui.lineEdit_3.text()
        contrasena=self.ui.lineEdit_4.text()
        
        if (nombre == apellido):
            QtGui.QMessageBox.critical(self, 'Mensaje de sistema', 'No puede repetir el mismo nombre')
            self.ui.lineEdit.setText("")
            self.ui.lineEdit_2.setText("")
                
        else:
            QtGui.QMessageBox.information(self,"Mensaje del sistema","Creado correctamente")
            ventana2=claseprin1().show()
            self.close()
            Config=ConfigParser.ConfigParser()
            cfgfile = open("logs.ini" , "w")
            Config.add_section("login")
            Config.set("login","nombre",nombre)
            Config.set("login","apellido",apellido)
            Config.set("login","usuario",usuario)
            Config.set("login","contrasena",contrasena)
            Config.write(cfgfile)
            cfgfile.close

    def cerrar(self):
        self.close()
        ventana2=claseprin1().show()

#--------------------------------------------Abre la ventana para iniciar sesion
class claseprin1(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/ingresar.ui",self)
        

    def volver(self):
        asd=inicio1().show()
        self.close()

    def ingresar(self):
        usuario=self.ui.txtUser.text()
        contrasena=self.ui.txtPass.text()
        self.archivo = "logs.ini"
        config = ConfigParser.ConfigParser()
        config.read(self.archivo)
        self.userDb = config.get("login", "usuario")
        self.passDb = config.get("login", "contrasena")
       
        if(usuario==self.userDb and contrasena == self.passDb):
            QtGui.QMessageBox.information(self, 'Mensaje de sistema', 'Usted ha ingresado correctamente.')
            self.logueado=1 
            self.close()
#--------------------------------------------Utilize esto para que cuando apriete el boton "ok" entre a "menu.ui"            
            archivo=menu().show()
        else:
            QtGui.QMessageBox.critical(self, 'Mensaje de sistema', 'Error de ingreso.')
            self.logueado=0

#--------------------------------------------Abre opcion1        
class myopcion1(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/opcion1.ui",self)

    def cerrar(self):
        self.close()

#--------------------------------------------Abre opcion2
class myopcion2(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/opcion2.ui",self)
    
    def cerrar(self):
        self.close()

#--------------------------------------------Abre opcion3
class myopcion3(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/opcion3.ui",self)
    
    def cerrar(self):
        self.close()
#--------------------------------------------Abre la ventana de las ventas
class claseprin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/principal.ui",self)
        productoingre = str(self.ui.productoingre.text())
#--------------------------------------------Crea el archivo precios.ini donde se guardaran todos los productos
        self.config = ConfigParser.RawConfigParser()
        self.config.read('precios.ini')
        self.cargarSecciones()
        config = ConfigParser.ConfigParser


#--------------------------------------------Abre la ventana total
    def vender(self):
        ventana = total(self.totaldecom).show()
#--------------------------------------------Limpio el LCD number que contiene todo los articulos acumulados
        self.ui.totaldecom.display("0")
#--------------------------------------------Seteo en 0 el acumulador, para una nueva venta
        global acu
        acu = 0
#--------------------------------------------Limpio el textBox y el display del precio del articulo
        self.ui.txbVentas.clear()
        self.ui.totalar.display("0")

#--------------------------------------------Abre el precios.ini
    def qt(self):
        os.system("xfce4-terminal -x gedit /home/nahuel/Documentos/Programacion/Pymes/precios.ini")

#--------------------------------------------Carga las secciones
    def cargarSecciones(self):
        self.ui.combocate.addItems(self.config.sections())

#--------------------------------------------Abre las ventanas de opciones

    def opcion3(self):
        archivo=myopcion3().show()
    

    def opcion2(self):
        archivo=myopcion2().show()


    def opcion1(self):
        archivo=myopcion1().show()    

#--------------------------------------------Funcion del boton empleados

    def empleados(self):
        archivo=ventanaem().show()


#--------------------------------------------Funcion de combobox de descripcion
    def productoprecio(self):
        count=0
        self.ui.combocate.insertItem(count,"Seleccionar")
#--------------------------------------------Busca lo seleccionado
        va = self.ui.combocate.currentIndex()
#--------------------------------------------Busca la categoria ingresada
        ve = self.ui.combocate.itemText(va)
        variable = self.ui.combodes.currentIndex()
        combo1 = self.ui.combodes.itemText(variable)
        var2 = self.config.get(str(ve),str(combo1))

        self.ui.totalar.display(var2)        
        lista = str(combo1) + "  = " + var2 + "\n----" 
        self.ui.txbVentas.append(lista)
#--------------------------------------------Acumula los precios de los productos
        global acu
        acu = acu + int(var2)
#--------------------------------------------Me muestra en el LCD el acumulado
        self.totalc = self.ui.totaldecom.display(acu)
        
    def returnTotal(self):
        return acu

#--------------------------------------------Funcion del combobox de categoria
    def tipodeprofun(self):
        count=0
        self.ui.combodes.insertItem(count,"Seleccionar")
#--------------------------------------------Busca lo seleccionado
        archivo = self.ui.combocate.currentIndex()
        archivomo= self.ui.combocate.itemText(archivo)

#--------------------------------------------Limpia el combobox      
        self.ui.combodes.clear()
#--------------------------------------------Agrega todos los items seleccionados
        self.config.read('precios.ini')        
        self.ui.combodes.addItems(self.config.options(str(archivomo)))


#--------------------------------------------Agrega todos los productos a el QtextBrowser y al pecios.ini
    def agregarprod(self):
        config = ConfigParser.RawConfigParser()  
        precioingre = self.ui.precioingre.text()
        productoingre = str(self.ui.productoingre.text())
        tipodeproducto = str(self.ui.tipodeproducto.text())
        config.add_section(tipodeproducto)
        config.set(tipodeproducto,productoingre,precioingre)       
        with open('precios.ini', 'a') as configfile:
            config.write(configfile)
#--------------------------------------------Agrega al textbox
	    textoo = self.ui.txbNuevos.toPlainText()
        self.ui.txbNuevos.setText(textoo+productoingre + " = " + str(precioingre) + "\n")
        self.actualizar(self.tipodeproducto,self.productoingre)
#--------------------------------------------Sale del todo
    def salir(self):
        asd=finalizar().show()
        self.close()
#--------------------------------------------Lo utilizo para que se actualizen los Combo Box con los productos ingresados
    def actualizar(self,tipodeproducto,productoingre):
        self.ui.combocate.addItem(self.tipodeproducto.text())
        self.ui.combodes.addItem(self.productoingre.text())    
        
#--------------------------------------------Limpio los LineEdit
        self.ui.productoingre.setText(" ")
        self.ui.tipodeproducto.setText(" ")
        self.ui.precioingre.setText(" ")
#--------------------------------------------Logica de la informacion de las deudas
class ventanaem(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/deudas.ui",self)
        self.filename="deudas.ini"
        self.cargarLista()

    def yaExisteDni(self, dni):
        f = self.getFile()                  
        for line in f:            
            datos = line.split(",")
            if datos[2]==dni:
                f.close()
                return True
        f.close()
        return False
        
    def guardar(self):
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        dni = self.ui.txtDni.text()
        if (not self.yaExisteDni(dni)):
            value=nombre+","+apellido+", Debe:"+dni+",\n"
            f = open(self.filename, "a")
            f.write(value)
            f.close()
            self.ui.txtNombre.setText("")        
            self.ui.txtApellido.setText("")
            self.ui.txtDni.setText("")
            self.cargarLista()
            self.ui.lblResultados.setText("Guardado Correctamente")
        else:
            self.ui.lblResultados.setText("")
    
    def limpiar(self):
        self.ui.txtNombre.setText("")        
        self.ui.txtApellido.setText("")
        self.ui.txtDni.setText("")
        self.ui.lblResultados.setText("")
        
    def buscar(self):
        f = self.getFile()           
        dniCargado=self.ui.cmbPersonas.currentText()
        for line in f:            
            datos = line.split(",")
            if datos[2]==dniCargado:
                self.ui.txtNombre.setText(datos[0])        
                self.ui.txtApellido.setText(datos[1])
                self.ui.txtDni.setText(datos[2])
                self.ui.lblResultados.setText("Datos Cargados")
                return
        self.ui.lblResultados.setText("Datos no encontrados")

    def cargarLista(self):
        f = self.getFile()           
        isEnd = False
        print f
        count=0
        self.ui.cmbPersonas.clear()
        self.ui.cmbPersonas.insertItem(count,"Seleccionar")
        for line in f:
            datos = line.split(",")
            count = count+1
            self.ui.cmbPersonas.insertItem(count,str(datos[2]))            
        f.close()
        
    def getFile(self):
        try:
            f=open(self.filename, "r")            
        except:
            f=open(self.filename, "w")  
        return f


    def cerrar(self):
        self.close()

#--------------------------------------------Abre la ventana de total, donde se ingresa la plata
class total(QtGui.QDialog):
    def __init__(self, apa, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/total.ui",self)
        total = claseprin().returnTotal()
        self.ui.total.display(total)
        self.totaldecom = apa

    def ok(self):
        self.close()
        archivo=resultado().show()

    def vuelto(self):
        paga = self.ui.inpaga.text()
#--------------------------------------------Resta para que me devuelva el vuelto
        vuelto1 = int(paga) - int(self.total.intValue())
        if (paga > self.total.intValue()):
            self.ui.suvuelto.setText("$" + (str (vuelto1)))
#--------------------------------------------Si hay un saldo menor al total avisa
        if (vuelto1 < 0):
            QtGui.QMessageBox.critical(self, 'Pymes Informa', 'Saldo Insuficiente')
            self.ui.suvuelto.setText("")
#--------------------------------------------Abre la ventana resultado
class resultado(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/resultado.ui",self)


    def aceptar(self):
        self.close()
#--------------------------------------------Abre la primera ventana donde informa
class InfoPy(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/infopymes.ui",self)

#--------------------------------------------Acepta y me abre la ventana de ingreso
    def aceptar(self):
        asd=inicio1().show()
        self.close()

#--------------------------------------------Al cerrar, pregunta si queres salir o no
class finalizar(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/cerrar.ui",self)

    def si(self):
        self.close()

    def no(self):
        asd=claseprin().show()
        self.close()        
#--------------------------------------------Abre la ventana de menu

class menu(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("./UI/menu.ui",self)

    def nuevo(self):
        asdds=claseprin().show()
        self.close()

    def salir(self):
        self.close()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp = InfoPy()
    myapp.show()
    sys.exit(app.exec_())
