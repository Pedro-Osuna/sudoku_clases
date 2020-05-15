#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:04:11 2019

@author: popscra

Verion de Python   => 3.7.4
Version de Tkinter => 8.6

.-El proyecto viene con un fichero (datos01.txt) con el que se pueden hacer 
pruebas, sin tener que hacer entradas a mano, para activarlo deberemos hacer lo
siguiente:
    poner almohadilla en el inicio de las lineas siguientes:
        263
        420
    quitar las almohadillas en las lineas siguientes:
        416
        417
.- si se añade alguna linea, es evidente que esos numeros variaran.
"""

from tkinter import *

from algoritmos import inicio, verificar_datos_iniciales_sudoku, verificar_solucion_sudoku     

import sys
import tkinter as tk

root = tk.Tk()
root.geometry("510x650") # +100+100")
root.title("Controlando entradas")

# Definimos variables
lista = StringVar()
numeros = StringVar()
difi = StringVar()
nota = StringVar()

# definimos el frame de informacion Personal
control=Frame(root)
control.config(width="200", height="150") #cambiar tamaño
control.config(bg='aquamarine')
control.config(bd=5) #cambiar el grosor del borde
control.config(relief="sunken") 
control.place(x=5, y=5) #snow3

# definimos el frame de informacion
control=Frame(root)
control.config(width="310", height="150") #cambiar tamaño
control.config(bg='aquamarine')
control.config(bd=5) #cambiar el grosor del borde
control.config(relief="sunken") 
control.place(x=197, y=5) #snow3
              
#definimos el frame que contiene la matriz del sudoku
master=Frame(root)
master.config(width="500", height="480") #cambiar tamaño
master.config(bg='gold')
master.config(bd=5) #cambiar el grosor del borde
master.config(relief="sunken") 
master.place(x=5, y=160) 


"""En esta lista de una dimension y 81 posiciones donde mantenenmos los datos 
de cada widget del sudoku osea los 81 cuadrados con el siguiente formato y datos,
es una cadena que consta de dos partes, separadas por una coma (,) la primera 
parte nos indica el numero del widget, la segunda la fila y la columna donde 
esta situado ese widget. """

obj = []
for fi in range(81):
    obj.append(fi)

""" Es la matriz para los datos que se visualizan en pantalla """
sud = []
for fi in range(9):
    sud.append([0]*9)

""" Es la matriz para los datos que mantiene sudoku en la ejecucion """
sudoku = []
for fi in range(9):
    sudoku.append([0]*9)


"""---Inicio---FUNCIONES DE MOVIMIENTO POR EL SUDOKU---"""
def determinar_ny_nx(event):
    """funcion que pasado el evento nos devuelve la fila ny y la columna nx
    de la entrada actual """
    # obtenemos el nombre del widget. nos interesa su numero
    event1 = str(event.widget)
    num = event1[15:]
    """si no tiene numero, nos interesan los datos del primer widget, que los 
    hemos guardado en la lista obj """
    if num == '' :
        dato = obj[0]
    else:
        dato = obj[int(num)-1]
    coordenas = dato.split(',')
    coordenas = coordenas[1]
    ny = int(coordenas[:1])
    nx = int(coordenas[1:])
    return [ny,nx]    


def izquierda(event):
    """ controlamos el movimiento hacia la izquierda """
    fi_co = determinar_ny_nx(event)
    ny = fi_co[0]
    nx = fi_co[1]
    if ny == 0 and nx == 0:
        sud[8][8].focus_set()
    elif nx != 0:
        sud[ny][nx-1].focus_set()
    else:
        sud[ny-1][nx+8].focus_set()
    return

        
def derecha(event):
    """ controlamos el movimiento hacia la derecha """
    fi_co = determinar_ny_nx(event)
    ny = fi_co[0]
    nx = fi_co[1]
    if ny == 8 and nx == 8:
        sud[0][0].focus_set()
    elif nx != 8:
        sud[ny][nx+1].focus_set()
    else:
        sud[ny+1][0].focus_set()
    return
        

def arriba(event):
    """" controlamos el movimiento hacia arriba """
    fi_co = determinar_ny_nx(event)
    ny = fi_co[0]
    nx = fi_co[1]
    if ny == 0 :
        sud[8][nx].focus_set() 
    else:
        sud[ny-1][nx].focus_set()
    return


def abajo(event):
    """ controlamos el movimiento hacia abajo """
    fi_co = determinar_ny_nx(event)
    ny = fi_co[0]
    nx = fi_co[1]
    if ny == 8:
        sud[0][nx].focus_set()
    else:
        sud[ny+1][nx].focus_set()
    return


def aceptar(event):
    fi_co = determinar_ny_nx(event)
    ny = fi_co[0]
    nx = fi_co[1]

    if ny == 8 and nx == 8:
        sud[0][0].focus_set()
    elif nx != 8:
        sud[ny][nx+1].focus_set()
    else:
        sud[ny+1][0].focus_set()
    return


def retroceso(event):
    """ controlamos el movimiento hacia abajo """
    fi_co = determinar_ny_nx(event)
    ny = fi_co[0]
    nx = fi_co[1]
    return

def mueve(event):
    fi_co = determinar_ny_nx(event)
    ny = fi_co[0]
    nx = fi_co[1]
    if ny == 8 and nx == 8:
        sud[0][0].focus_set()
    elif nx != 8:
        sud[ny][nx+1].focus_set()
    else:
        sud[ny+1][0].focus_set()
    return
"""---Fin---FUNCIONES DE MOVIMIENTO POR EL SUDOKU---"""


def quit():
    """ Abortamos el programa """
    root.destroy()
    exit()
    return


def llenamos_el_sudoku_con_los_datos_entrados(sud, sudoku):
    """
    Rellena las celdas con los numeros entrados a mano del sudoku a resolver
    """
    # leemos los datos entrados
    nume = IntVar()
    for y in range(9):
        for x in range(9):
            nume = sud[y][x].get()
            if nume == '':
                nume = 0
            else:
                nume = int(nume)
            sudoku[y][x] = nume
    return   


def llenamos_el_sudoku_con_los_datos_encontrados(sud, sudoku):
    """
    llena el sudoku con todos los numeros encontrados al ejecutar el programa
    colocandolos en sus celdas
    """
    # leemos los datos entrados
    nume = IntVar()
    for y in range(9):
        for x in range(9):
            nume = sudoku[y][x]
            sud[y][x].insert(0,nume)
    return    


def iniciar_proceso():
    boton1.config(state='disabled')   # nuevo sudoku
    boton2.config(state='disabled')   # comprobar incoherencias
    boton3.config(state='disabled')   # Iniciar Proceso
    boton4.config(state='disabled')   # Comprobar Sudoku
    inicio(sudoku)
    boton4.config(state='normal')   # Comprobar Sudoku
    llenamos_el_sudoku_con_los_datos_encontrados(sud, sudoku)
    return


def nuevo_sudoku():
    """ poner sudoku y sud a inicio (todas las casillas a cero en el sudoku
    y a blancos en la pantalla """
    for y in range(9):
        for x in range(9):
            sudoku[y][x] = 0
            """ Borra la entrada  indicada  del entry """
            sud[y][x].delete(0, END)
    nota.set('Introduzca los valores del sudoku')
    difi.set('')
    boton1.config(state='disabled')   # nuevo sudoku
    boton2.config(state='normal')     # comprobar incoherencias
    boton3.config(state='disabled')   # Iniciar Proceso
    boton4.config(state='disabled')   # Comprobar Sudoku
    boton5.focus()
    return

def comprobar_incoherencias():
    """ comprobamos las incoherencias de los datos entrados en el sudoku """
    #  ++++++++++++++++++++++++   IMPORTANTE   +++++++++++++++++++++++++++
    """ ---- SACAR LA ALMOHADILLA  PARA EJECUTAR ENTRANDO DATOS a MANO -----"""
    llenamos_el_sudoku_con_los_datos_entrados(sud, sudoku)
    #  ++++++++++++++++++++++++   IMPORTANTE   +++++++++++++++++++++++++++
    
    dificultad = cantidad_de_numeros_iniciales(sudoku)
    #difi.set(dificultad)
    boton1.config(state='disabled')  # nuevo sudoku
    boton4.config(state='disabled')  # Comprobar Sudoku
    if dificultad != 'Datos iniciales menos de 20 => Fuera de lógica':
        if  verificar_datos_iniciales_sudoku(sudoku):
            nota.set('&&&- ENTRADAS CORRECTAS -&&&') 
            boton2.config(state='disabled')  # comprobar incoherencias
            boton3.config(state='normal')    # Iniciar Proceso
            boton3.focus()  # Iniciar Proceso
        else:
            nota.set('Se deben modificar los datos del sudoku')
            boton2.config(state='normal')  # comprobar incoherencias
            boton3.config(state='disabled') # Iniciar Proceso   
            boton2.focus()  # comprobar incoherencias
    else:
            boton3.config(state='disabled') # Iniciar Proceso
            nota.set('Datos iniciales menos de 20 => Fuera de lógica') 

    return

# comprobamos todos los valores del sudoku
def comprobar_sudoku():
    
    """
    PARAMETROS:
        ninguno
    PROCESO:
        Recorremos el sudoku celda a celda comprobando que el numero cumple
        con las normas del sudoku 
    LA FUNCION DEVUELVE
        True si todas las celdas son correctas
        False si alguna celda es incorrecta
    """
    if verificar_solucion_sudoku(sudoku):
        boton1.config(state='normal')   # nuevo sudoku
        boton2.config(state='disabled') # comprobar incoherencias
        boton3.config(state='disabled') # Iniciar Proceso   
        boton4.config(state='disabled') # Comprobar Sudoku
        nota.set('---- SUDOKU CORRECTO ------') 
    return True

def cantidad_de_numeros_iniciales(tabla):
    cantidad = 0
    difi = 'Facil'
    for fi in range(9):
        for co in range(9):
            if tabla[fi][co] != 0:
                cantidad += 1
    if cantidad <= 18:
        difi =  'Datos iniciales menos de 20 => Fuera de lógica'
    elif cantidad <= 21:
        difi = str(cantidad) + ' Extrema'
    elif cantidad < 24:
        difi = str(cantidad) + ' Experto'
    elif cantidad <  27:
        difi = str(cantidad) + ' Dificil'
    else:
        difi = str(cantidad) + ' Facil'
    return difi


# funcion que nos permite validar las entradas en el sudoku
def is_valid_date(action, char, text, indice):
    # Solo chequear cuando se añade un carácter.
    if action != "1":
        return True
    return char in "123456789 " and len(text) < 1
    

def visualizamos_y_dibujamos_sudoku(sudoku, sud, obj):
    # construimos el sudoku 
    saltox=0
    saltoy=0
    posi = 1
    for r in range(0, 9):
        for c in range(0, 9):
            if c == 3 or c == 6:
                saltox += 45
            else:
                saltox += 30
            sud[r][c] = Entry(master, validate = "key", width = 2, justify= CENTER,validatecommand=(validatecommand, "%d", "%S", "%s", "%i"))
            sud[r][c].place(x=60+saltox, y=40 + saltoy)
            obj[posi-1] = str(posi) + ','+str(r) + str(c)
            posi += 1
            nume = sudoku[r][c]
            sud[r][c].insert(0, nume)
        if r == 2 or r == 5:
            saltoy += 45
        else:
            saltoy += 30
        x = 60
        saltox = 0
        sud[0][0].focus()
    return


validatecommand = root.register(is_valid_date)

Label00 = Label(root, text="Autor: Pedro Osuna ",anchor = 'sw', bg='snow3') #Creación del Label
Label00.place(x=10, y=11, width='180', height='15')

Label01 = Label(root, text="Versión: con CLASES", anchor = 'sw', bg='snow3') #Creación del Label
Label01.place(x=10, y=26, width='180', height='15')

Label02 = Label(root, text="Inicio Proyecto: 18/04/2020", anchor = 'sw', bg='snow3') #Creación del Label
Label02.place(x=10, y=41, width='180', height='15')
              
Label07 = Label(root, text="Dificultad =>", justify=LEFT ,bg='snow3') #Creación del Label
Label07.place(x=15, y=554, width ='90', height ='15')
lista07 = Entry(root, textvariable = difi, validate = "key", width = 15, justify = LEFT)
lista07.place(x=110, y=549)

Label08 = Label(root, text="Nota =>", justify=LEFT ,bg='snow3') #Creación del Label
Label08.place(x=15, y = 583, width = '50', height='15')
lista08 = Entry(root, textvariable = nota, validate = "key", width = 45, justify = LEFT)
lista08.place(x=70, y=578)

boton1=Button(control, text="      Nuevo  Sudoku      ", command=nuevo_sudoku)
boton1.place(x=70, y=5, width='180', height='25')

boton2=Button(control, text=" Comprobar incoherencias ", command=comprobar_incoherencias)
boton2.place(x=70, y=32, width='180', height='25')

boton3=Button(control, text="    Resolver Sudoku      ", command=iniciar_proceso)
boton3.place(x=70, y=59, width='180', height='25')

boton4 = Button(control, text="   Verificar Sudoku    ", command=comprobar_sudoku)
boton4.place(x=70, y=86, width='180', height= '25')

boton5 = Button(control, fg="red", text="  Salir del programa   ", command=quit)
boton5.place(x=70, y=113, width='180', height= '25')


root.bind_all("<KeyPress>",mueve)
root.bind_all("<KeyPress-Left>",izquierda)
root.bind_all("<KeyPress-Right>",derecha)
root.bind_all("<KeyPress-Down>",abajo)
root.bind_all("<KeyPress-Up>",arriba)
root.bind_all("<KeyPress-Return>",aceptar)
root.bind_all("<BackSpace>", retroceso)

boton1.config(state='disabled')   # nuevo sudoku
boton2.config(state='normal')     # comprobar incoherencias
boton3.config(state='disabled')   # Iniciar Proceso
boton4.config(state='disabled')   # Comprobar Sudoku


#  ++++++++++++++++++++++++   IMPORTANTE   +++++++++++++++++++++++++++
"""-SACAR LAS ALMOHADILLAS SI QUEREMOS CARGAR EL FICHERO PARA SOLUCIONAR--"""
#from datos01 import *    # 215 de sudokus  
#sudoku = llenar_sudoku_con_datos_en_modu00()
#  ++++++++++++++++++++++++   IMPORTANTE   +++++++++++++++++++++++++++
"""-PONER LA ALMOHADILLA SI QUEREMOS CARGAR EL FICHERO PARA SOLUCIONAR--"""
nota.set('Introduzca los valores iniciales del sudoku')
#  ++++++++++++++++++++++++   IMPORTANTE   +++++++++++++++++++++++++++

visualizamos_y_dibujamos_sudoku(sudoku, sud, obj) 
root.mainloop()