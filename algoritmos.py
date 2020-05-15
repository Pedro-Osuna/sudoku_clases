#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resolucion de sudoku 

.-En este fichero he desarrollado las clases y las funciones necesarias para el
programa.
.-Para procesar se deben de dar un minimo de 20 numeros al inicio.
.-Con un poco de retoque puede funcionar sin necesidad de la parte visual (sudoku_c.pyw)
.-Es la primera vez que realizo un programa con clases, concretamente de este
programa tengo uno realizado sin clases, y es mucho mas pesado que este.
.-Me embarque en hacerlo con clases para coger experiencia, asi que si alguien lo
ve y considera que es mejorable, pues eso me lo propone y a mejorar.
.-En cada funcion he generado una pequeña documentacion de los que hace, se que 
se podria mejorar, pero  bueno acepto cualquier sugerencia.

Verion de Python   => 3.7.4
Version de Tkinter => 8.6
"""

import os

sposibles = []
for fi in range(9):
    sposibles.append([[]]* 9)
print('')

#=============================================================================   
class Celda():
    def __init__(self, fi, co, va):
        self.fi = fi
        self.co = co
        self.va = va
        

    def determinar_zona_celda(self, fi, co):
        """
        PARAMETROS:
            fi la fila de la celda
            co la columna de la celda
        PROCESO:
            por los valores de (fi,co) determinamos las tres filas y las tres 
            columnas de la zona a la que pertenece la celda.
        DEVUELVE:
            dos listas, una con las filas y otra con las columnas
        """
        # buscamos de la fila    
        if fi < 3:
            filas = [0,1,2]
        elif fi < 6:
            filas = [3,4,5]
        else:
            filas = [6,7,8]
        # buscamos de la columna    
        if co < 3 :
            columnas = [0,1,2]
        elif co < 6:
            columnas = [3,4,5]
        else:
            columnas = [6,7,8]
        return [filas, columnas]        
        
    def controla_valor_correcto_celda(self,ssudoku, fi, co, valor):
        """
        PARAMETROS:
            fi la fila de la celda
            co la columna de la celda
            valor el valor de la celda
        PROCESO:
            controlamos que el valor de la celda cumpla las normas del sudoku
            en las tres fase: la fila, columna y zona
        DEVUELVE:
            si las cumple devuelve True en caso contrario False
        """    

        """ LA FILA:comprobamos cada celda de la fila indicada por (fi), 
        exceptuando la celda que estamos controlando. Si el valor de la celda 
        coincide con (valor) devolveremos False pues nos indica que
        dicho valor esta repetido en la fila, en caso contrario pasamos al control
        de la columna"""
        for x in range(9):
            if ssudoku[fi][x] != 0:
                if x != co :
                    if ssudoku[fi][x] == valor:
                        # el valor esta repetido en la fila
                        print('Valor {} repetido en la fila {}'.format(valor, fi))
                        return False
        
        """ LA COLUMNA: comprobamos cada celda de la columna indicada por (co),
        exceptuando la celda que estamos controlando. Si el valor de la celda
        coincide con (valor) devolveremos False pues nos indica que dicho valor
        esta repetido en la columna, en caso contrario pasamos al control de
        la zona """
        for y in range(9):
            if ssudoku[y][co] != 0:
                if y != fi :
                    if ssudoku[y][co] == valor:
                        # el valor esta repetido en la columna
                        print('Valor {} repetido en la columna {}'.format(valor, co))
                        return False 
        
        """ LA ZONA:comprobamos cada celda de la zona  indicada segun (fi,co) 
        exceptuando la celda que estamos controlando. Si el valor de la celda
        coincide con (valor) devolveremos False pues nos indica que
        dicho valor esta repetido en la zona, en caso contrario devolvemos True """
        lista = self.determinar_zona_celda(fi, co)
        # print('fi=> {} co=> {}'.format(fi, co))
        # print('lista0=> {} lista1=> {}'.format(lista[0], lista[1]))
        for y in lista[0]:
            for x in lista[1]:
                if y != fi or x != co:
                    if ssudoku[y][x] != 0:
                        if ssudoku[y][x] == valor:
                            # el valor esta repetido en la zona
                            print('Valor {} repetido en zona fila {} columna {}'.format(valor, y, x))
                            return False
                #print('Fila {} columna {}'.format(y, x))
        return True
    
#=============================================================================   
class Fila():
    num_celdas = 9
    def __init__(self, cla_celda):
        self.cla_celda = cla_celda
    
    def poner_numeros_de_fila_sin_ceros_en_lista(self,ssudoku, fila):
        """
        PARAMETROS:
            fila la fila a tratar
        PROCESO:
            leemos las celdas de la fila obteniendo su valor siempre que sea
            mayor que cero
        DEVOLVEMOS:
            devolvemos la lista con los numeros sin ceros.
        """
        lista = []
        for x in range(9):
            valor = ssudoku[fila][x]
            if valor != 0:
                lista.append(valor) 
        return lista
    
    
    def determinar_zona_fila(self, fila):
        """
        PARAMETROS:
            fi la fila de la celda
        PROCESO:
            por los valores de (fi) determinamos las tres filas a la que 
            pertenece la fila.
        DEVUELVE:
            lista, con las tres filas de la zona
        """
        # buscamos de la fila    
        if fila < 3:
            filas = [0,1,2]
        elif fila < 6:
            filas = [3,4,5]
        else:
            filas = [6,7,8]
        return filas

    def fila_con_par_de_celdas_con_dos_posibles_iguales(self,sudoku, fila):
        """
        PARAMETROS:
            fila donde se busca
        PROCESO:
            Buscamos en la fila todas los pares de celdas que tengan dos numeros
            posibles y sean iguales en las dos celdas, guardaremos en la lista 
            (celdas_dobles) la columna dentro de la fila de las dos celdas 
        DEVOLVEMOS:
            la lista de las columnas que tienen (celdas_dobles)
        """
        celdas_dobles = []
        # recorremos la fila pero solo hasta la celda 7
        for x in range(8): 
            if len(sposibles[fila][x]) == 2: 
                x1 = x + 1
                # recorremos la columna empezando por la celda siguiente a la
                # que estamos en el for anterior
                for xx in range(x1,9):
                    if len(sposibles[fila][xx]) == 2: 
                        # comprobamos si las dos celdas son iguales, si es asi 
                        # guardamos la posicion de una de ellas en la tabla
                        if sposibles[fila][xx] == sposibles[fila][x]:
                           celdas_dobles.append(x)
                           celdas_dobles.append(xx)
                           break
        return celdas_dobles
    
#=============================================================================   
class Columna():
    num_celdas = 9
    def __init__(self, cla_celda):
        self.cla_celda = cla_celda
   
    def poner_numeros_de_columna_sin_ceros_en_lista(self,ssudoku, columna):
        """
        PARAMETROS:
            columna la columna a tratar
        PROCESO:
            leemos las celdas de la columna obteniendo su valor siempre que sea
            mayor que cero
        DEVOLVEMOS:
            devolvemos la lista con los numeros sin ceros.
        """
        lista = []
        for y in range(9):
            valor = ssudoku[y][columna]
            if valor != 0:
                lista.append(valor) 
        return lista
    
    def poner_posibles_columna_en_lista(self, columna):
        """ 
        PARAMETROS:
            columna es la fila a tratar
        PROCESO:
            generamos por cada celda de la columna un elemento en la lista con los
            numeros posibles de la celda.
        DEVOLVEMOS:
            la lista con los posibles
        """
        lposi = []
        for y in range(9):
            valor = sposibles[y][columna]
            lposi.append(valor) 
        return lposi
    
    def determinar_zona_columna(self, columna):
        """
        PARAMETROS:
            columna la columna de la celda
        PROCESO:
            por los valores de (columna) determinamos las tres columnas a la que 
            pertenece la columna.
        DEVUELVE:
            lista, con las tres columnas de la zona
        """
        # buscamos de la fila    
        if columna < 3:
            columnas = [0,1,2]
        elif columna < 6:
            columnas = [3,4,5]
        else:
            columnas = [6,7,8]
        return columnas

    def columna_con_par_de_celdas_con_dos_posibles_iguales(self,ssudoku, columna):
    #def celdas_con_dos_posibles_iguales(self, columna):
        """
        PARAMETROS:
            columna donde se busca
        PROCESO:
            Buscamos en la columna todas los pares de celdas que tengan dos numeros
            posibles y sean iguales en las dos celdas, guardaremos en la lista 
            (celdas_dobles) la fila dentro de la columna de las dos celdas 
        DEVOLVEMOS:
            la lista de las filas que tienen (celdas_dobles)
        """
        co = columna
        celdas_dobles = []
        # recorremos la fila pero solo hasta la celda 7
        for y in range(8): 
            if len(sposibles[y][columna]) == 2: 
                y1 = y + 1
                # recorremos la columna empezando por la celda siguiente a la
                # que estamos en el for anterior
                for yy in range(y1,9):
                    if len(sposibles[yy][columna]) == 2: 
                        # comprobamos si las dos celdas son iguales, si es asi 
                        # guardamos la posicion de una de ellas en la tabla
                        if sposibles[yy][columna] == sposibles[y][columna]:
                           celdas_dobles.append(y)
                           celdas_dobles.append(yy)
                           break
        return celdas_dobles
    
#=============================================================================   
class Sudoku():
    nfi = 9
    nco = 9
    lnum_posi =[0,1,2,3,4,5,6,7,8,9]
    
    def __init__(self, cla_celda):
        self.cla_celda = cla_celda

    # comprobamos todos los valores del sudoku
    def verificar_solucion_sudoku(self, ssudoku):
        """
        PARAMETROS:
            el sudoku
        PROCESO:
            Recorremos el sudoku celda a celda comprobando que el numero cumple
            con las normas del sudoku 
        LA FUNCION DEVUELVE
            True si todas las celdas son correctas
            False si alguna celda es incorrecta
        """
        for y in range(self.nfi):
            for x in range(self.nco):
                if ssudoku[y][x] != 0:
                    if not s_celda.controla_valor_correcto_celda(ssudoku, y, x, ssudoku[y][x]):
                        #print('el valor {} de la fila {} columna {} esta repetido'.format(ssudoku[y][x], y, x))
                        return False
                else:
                    return  False
        return True

    # sudoku todavia con ceros
    def busco_ceros_en_sudoku(self, ssudoku):
        """
        PARAMETROS:
            el sudoku
        PROCESO:
            Recorremos el sudoku celda a celda 
            si encontramos una celda con valor cero, salimos devolvemos la 
            cantidad de ceros
        DEVUELVE:
            devolvemos la cantidad de ceros que tiene el sudoku
        """
        cant = 0
        for y in range(self.nfi):
            for x in range(self.nco):
                if ssudoku[y][x] == 0:
                    cant += 1    
        return cant

    def buscar_celdas_con_un_unico_posible(self, ssudoku):
        """
        PARAMETROS:
            ninguno
        PROCESO:
            Recorremos posibles buscando celdas donde solo tengamos un numero como 
            posible, si es asi, estampamos en el sudoku el numero y en posibles
            ponemos una lista vacia
            La funcion la ejecutamos hasta que no encontremos ninguna celda
            en posibles con un numeros posible unico.
        DEVUELVE
            nada        
        """
        volver = True
        while volver:
            volver = False
            for y in range(self.nfi):
                for x in range(self.nco):
                    if len(sposibles[y][x]) == 1:
                        num = sposibles[y][x]
                        ssudoku[y][x] = num[0]
                        sposibles[y][x] = []
                        self.recomponer_posibles(ssudoku)
                        volver = True
                        break
                if volver:
                    break
        return

    def recomponer_posibles(self, ssudoku):
        """
        PARAMETROS:
            el sudoku
        PROCESO:
        Hacemos un recorrido del sudoku de forma que por cada celda que encontremos
        con un cero, generamos una lista con los numeros posibles en esa celda que 
        cumplan las normas de resolucion del sudoku, y la guardamos en la misma celda
        pero de posibles:
        DEVUELVE:
            nada        
        """
        for y in range(self.nfi):
            for x in range(self.nco):
                if ssudoku[y][x] == 0:
                    r_zona = s_zonafc.poner_numeros_sin_ceros_de_la_zona_en_lista(ssudoku, y, x)    
                    r_columna = s_columna.poner_numeros_de_columna_sin_ceros_en_lista(ssudoku, x)
                    r_fila = s_fila.poner_numeros_de_fila_sin_ceros_en_lista(ssudoku, y)
                    lista1 = list(sorted(set(r_zona + r_columna + r_fila)))
                    lista = []
                    for num in range(1,10):
                        if num not in  lista1:
                           lista.append(num) 
                    sposibles[y][x] = lista
                else:
                    sposibles[y][x] = []
        return 


#=============================================================================   
class Zona_tres_filas_tres_columnas():
    num_celdas = 9
    def __init__(self, cla_celda):
        self.cla_celda = cla_celda
        
    def poner_numeros_sin_ceros_de_la_zona_en_lista(self,ssudoku, fila, columna):
        """
        PARAMETROS:
            fila fila de la celda
            columna de la celda
        PROCESO:
            leemos las celdas obteniendo su valor siempre que sea mayor que cero
        DEVOLVEMOS:
            devolvemos la lista con los numeros sin ceros.
        """
        resul = []
        lista_zona = self.cla_celda.determinar_zona_celda(fila, columna) 
        for y in lista_zona[0]:
            for x in lista_zona[1]:
                if ssudoku[y][x] != 0:
                    resul.append(ssudoku[y][x])
        return resul   
        
    def poner_numeros_con_ceros_de_la_zona_en_lista(self,ssudoku, fila, columna):
        """
        PARAMETROS:
            fila fila de la celda
            columna de la celda
        PROCESO:
            leemos las celdas obteniendo su valor incluso los ceros
        DEVOLVEMOS:
            devolvemos la lista con los numeros.
        """
        resul = []
        lista_zona = self.cla_celda.determinar_zona_celda(fila, columna) 
        for y in lista_zona[0]:
            for x in lista_zona[1]:
                resul.append(ssudoku[y][x])
        return resul   


    def poner_posibles_zona_en_lista(self,ssudoku, fila, columna):
        """ 
        PARAMETROS:
            fila es la fila de la celda
            columna es la columna de la celda
        PROCESO:
            generamos por cada celda de la zona un elemento en la lista con los
            numeros posibles de la celda.
        DEVOLVEMOS:
            la lista con los posibles
        """
        resul = []
        lista_zona = self.cla_celda.determinar_zona_celda(fila, columna) 
        for y in lista_zona[0]:
            for x in lista_zona[1]:
                if sposibles[y][x] != 0:
                    resul.append(sposibles[y][x])
        return resul   

    
    def zona_con_par_de_celdas_con_dos_posibles_iguales(self, fi, co):
        """
        PARAMETROS:
            fila junto con la columna nos determinara la zona a trabajar
            columna junto con la fila nos determinara la zona a trabajar
        PROCESO:
            Buscamos en la zona todas los pares de celdas que tengan solo dos numeros
            posibles y sean iguales en las dos celdas, guardaremos en la lista 
            (celdas_dobles) la fila y columna de las dos celdas iguales 
        DEVOLVEMOS:
            la lista (celdas_dobles) 
        """
        # determinamos las filas y las zonas de la zona
        lcolumnas = s_columna.determinar_zona_columna(co)
        lfilas = s_fila.determinar_zona_fila(fi)
        #recorremos la zona buscando dos celdas con dos numeros posibles iguales
        celdas_dobles = []
        for y in lfilas:
            for x in lcolumnas:
                if len(sposibles[y][x]) == 2:
                    for y1 in lfilas:
                        for x1 in lcolumnas:
                            if y1 != y or x1 != x:
                                if sposibles[y][x] == sposibles[y1][x1]:
                                    celdas_dobles.append(y)
                                    celdas_dobles.append(x)
                                    celdas_dobles.append(y1)
                                    celdas_dobles.append(x1)
                                    return celdas_dobles
        return celdas_dobles

#=============================================================================   
s_celda = Celda(3,7,8)
s_fila = Fila(s_celda)
s_columna = Columna(s_celda)
s_sudoku = Sudoku(s_celda)
s_zonafc = Zona_tres_filas_tres_columnas(s_celda)


# comprobamos todos los valores del sudoku cumplen las normas
def verificar_datos_iniciales_sudoku(ssudoku):
    """
    PARAMETROS:
        ninguno
    PROCESO:
        Recorremos el sudoku saltandonos las celdas que contengan cero
        comprobando que el numero cumple con las normas del sudoku 
    LA FUNCION DEVUELVE
        True si todas las celdas son correctas
        False si alguna celda es incorrecta
    """
    for y in range(9):
        for x in range(9):
            if ssudoku[y][x] != 0:
                if not s_celda.controla_valor_correcto_celda(ssudoku, y, x, ssudoku[y][x]):
                    #print('el valor {} de la fila {} columna {} esta repetido'.format(ssudoku[y][x], y, x))
                    return False
    return True


# comprobamos todos los valores del sudoku
def verificar_solucion_sudoku(ssudoku):
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
    for y in range(9):
        for x in range(9):
            if ssudoku[y][x] != 0:
                if not s_celda.controla_valor_correcto_celda(ssudoku, y, x, ssudoku[y][x]):
                    #print('el valor {} de la fila {} columna {} esta repetido'.format(ssudoku[y][x], y, x))
                    return False
            else:
                return  False
    return True
    
def estampar_en_zonas_de_tres_filas(ssudoku, fila):
    """
    PARAMETROS:
        fila => fila nos sirve para determinar la zona de tres filas a trabajar
    PROCESO:
        Buscamos en la tres filas numeros que esten en dos filas y en la otra 
        fila no este. Para ello tendremos que probar las tres posibilidades que
        nos ofrecen las tres filas:
        (fila1,fila2,fila3); (fila1,fila3,fila2); (fila2,fila3,fila1)
        Comprobaremos si en la fila que no esta el numero, podemos estamparlo
        en alguna celda
        La funcion la ejecutamos hasta que no hallamos podido estampar ningun
        numero
    DEVUELVE
        nada        
    """
    volver = True
    while volver:
        volver = False
        # ponemos en lfilas, los numeros de las  tres filas de la zona
        lfilas = s_fila.determinar_zona_fila(fila)
        # creamos tres listas con los numeros de cada una de las filas de la zona
        lista1 = s_fila.poner_numeros_de_fila_sin_ceros_en_lista(ssudoku, lfilas[0])
        lista2 = s_fila.poner_numeros_de_fila_sin_ceros_en_lista(ssudoku, lfilas[1])
        lista3 = s_fila.poner_numeros_de_fila_sin_ceros_en_lista(ssudoku, lfilas[2])
        # pongo en lbuscar las tres filas de posibles donde detectar si puedo
        # implementar algun numero en el ssudoku
        lbuscar = [sposibles[lfilas[2]], sposibles[lfilas[1]],sposibles[lfilas[0]]]
        # pongo en lcombi la tres combinaciones de las filas de la zona a trabajar,
        # y la fila de posibles a buscar
        lcombi = [[lista1,lista2,lista3,lbuscar[0]],[lista1,lista3,lista2,lbuscar[1]],
                  [lista2,lista3,lista1,lbuscar[2]]]
        # me sirve para saber en que fila ha encontrado un numero
        llfilas = [lfilas[2],lfilas[1],lfilas[0]]
        for x in range(3):
            # pongo en llcombi las tres filas del sudoku, y la de posibles con las que voy a  trabajar
            llcombi = lcombi[x]
            # ponemos el resul los numeros comunes de llcombi[0] y llcombi[1]
            resul = list(set(llcombi[0]) & set(llcombi[1]))
            # quitamos en resul los numeros que esten en llcombi[2]
            resul = list(set(resul) - set(llcombi[2]))
            # pongo en fi la fila que estoy trabajando
            fi = llfilas[x]
            if resul != []:
                fi_posi = llcombi[3]   
                for num in resul:
                    cant = 0
                    n = 0
                    for posi in fi_posi:
                        if num in posi:
                            cant += 1
                            posi_celda = n
                        n += 1
                    if cant == 1:
                        #print('ESTOY EN FILAS ==> Fila=> {} columna =>{} numero {}'.format(fi,posi_celda,num))
                        ssudoku[fi][posi_celda] = num
                        s_sudoku.recomponer_posibles(ssudoku)
                        volver = True
                        break
        if volver:
            break
    return

def estampar_en_zonas_de_tres_columnas(ssudoku, columna):
    """
    PARAMETROS:
        columna => columna nos sirve para determinar la zona de tres filas a trabajar
    PROCESO:
        Buscamos en la tres columnas numeros que esten en dos columnas y en la otra 
        columna no este. Para ello tendremos que probar las tres posibilidades que
        nos ofrecen las tres filas:
        (columna1,columna2,columna3); (columna1,columna3,columna2);
        (columna2,columna3,columna1)
        Comprobaremos si en la columna que no esta el numero, podemos estamparlo
        en alguna celda
        La funcion la ejecutamos hasta que no hallamos podido estampar ningun
        numero
    DEVUELVE
        nada        
    """
    volver = True
    while volver:
        volver = False
        # ponemos en lcolumnas, los numeros de las  tres columnas de la zona
        lcolumnas = s_columna.determinar_zona_columna(columna)
        # creamos tres listas con los numeros de cada una de las columnas de la zona
        lista1 = s_columna.poner_numeros_de_columna_sin_ceros_en_lista(ssudoku, lcolumnas[0])
        lista2 = s_columna.poner_numeros_de_columna_sin_ceros_en_lista(ssudoku, lcolumnas[1])
        lista3 = s_columna.poner_numeros_de_columna_sin_ceros_en_lista(ssudoku, lcolumnas[2])
        # pongo en lbuscar las tres columnas de posibles donde detectar si puedo
        # implementar algun numero en el ssudoku
        lbuscar1 = s_columna.poner_posibles_columna_en_lista(lcolumnas[0])
        lbuscar2 = s_columna.poner_posibles_columna_en_lista(lcolumnas[1])
        lbuscar3 = s_columna.poner_posibles_columna_en_lista(lcolumnas[2])
        
        lcombi = [[lista1,lista2,lista3,lbuscar3],[lista1,lista3,lista2,lbuscar2],
                  [lista2,lista3,lista1,lbuscar1]]
        # me sirve para saber en que columna ha encontrado un numero
        llcolumnas = [lcolumnas[2],lcolumnas[1],lcolumnas[0]]
        
        for x in range(3):
            # pongo en llcombi las tres columnas del sudoku, y la de posibles con las que voy a  trabajar
            llcombi = lcombi[x]
            # ponemos el resul los numeros comunes de llcombi[0] y llcombi[1]
            resul = list(set(llcombi[0]) & set(llcombi[1]))
            # quitamos en resul los numeros que esten en llcombi[2]
            resul = list(set(resul) - set(llcombi[2]))
            # pongo en co la columna que estoy trabajando
            co = llcolumnas[x]
            if resul != []:
                co_posi = llcombi[3]   
                for num in resul:
                    cant = 0
                    n = 0
                    for posi in co_posi:
                        if num in posi:
                            cant += 1
                            posi_celda = n
                        n += 1
                    if cant == 1:
                        #print('ESTOY EN COLUMNAS ==> Fila=> {} columna =>{} numero {}'.format(posi_celda,co,num))
                        ssudoku[posi_celda][co] = num
                        s_sudoku.recomponer_posibles(ssudoku)
                        volver = True
                        break
        if volver:
            break
    return
    
def numero_posible_unico_en_toda_la_fila(ssudoku, fila):
    """ 
    PARAMETROS:
        fila => la fila, donde trabajara la funcion 
    PROCESO:
        dentro de la fila comprobamos si alguna celda tiene algun numero posible
        que no este en ninguna de las otras celdas de la fila.
        Si es asi lo estampamos en la misma celda del sudoku que lo hemos encontrado
        en posibles.
        La funcion la ejecutamos hasta que no hallamos podido estampar ningun
        numero
    DEVUELVE
        nada        
    """
    volver = True
    while volver:
        volver = False
        for x in range(8): # es solo hasta el 8 porque ya hemos comprobado del 0 al 7
            if sposibles[fila][x] != []:
                lposibles = sposibles[fila][x]
                for num in lposibles:
                    esta = 0
                    for zz in range(9):
                        if zz != x:
                            if sposibles[fila][zz] != []:
                                if num in sposibles[fila][zz]:
                                    esta += 1
                                    break
                    if esta == 0:
                        ssudoku[fila][x]= num
                        sposibles[fila][x] = []
                        s_sudoku.recomponer_posibles(ssudoku)
                        volver = True
                        break
                if volver:
                    break
    return
            
def numero_posible_unico_en_toda_la_columna(ssudoku, columna):
    """ 
    PARAMETROS:
        columna => la columna, donde trabajara la funcion 
    PROCESO:
        dentro de la columna comprobamos si alguna celda tiene algun numero posible
        que no este en ninguna de las otras celdas de la columna.
        Si es asi lo estampamos en la misma celda del sudoku que lo hemos encontrado
        en posibles.
        La funcion la ejecutamos hasta que no hallamos podido estampar ningun
        numero
    DEVUELVE
        nada        
    """
    volver = True
    while volver:
        volver = False
        for y in range(8): # es solo hasta el 8 porque ya hemos comprobado del 0 al 7
            if sposibles[y][columna] != []:
                lposibles = sposibles[y][columna]
                for num in lposibles:
                    esta = 0
                    for zz in range(9):
                        if zz != y:
                            if sposibles[zz][columna] != []:
                                if num in sposibles[zz][columna]:
                                    esta += 1
                                    break
                    if esta == 0:
                        ssudoku[y][columna]= num
                        sposibles[y][columna] = []
                        s_sudoku.recomponer_posibles(ssudoku)
                        volver = True
                        break
                if volver:
                    break
    return

def numero_posible_unico_en_toda_la_zona(ssudoku, fi, co):
    """ 
    PARAMETROS:
        fi => la fila, nos sirve para determinar junto con la columna la zona 
        co => la columna, nos sirve para determinar junto con la fila la zona 
    PROCESO:
        dentro de la zona comprobamos si alguna celda tiene algun numero posible
        que no este en ninguna de las otras celdas de la zona.
        Si es asi lo estampamos en la misma celda del sudoku que lo hemos encontrado
        en posibles.
        La funcion la ejecutamos hasta que no hallamos podido estampar ningun
        numero
    DEVUELVE
        nada        
    """
    volver = True
    while volver:
        volver = False
        lfilas =  s_fila.determinar_zona_fila(fi)
        lcolumnas = s_columna.determinar_zona_columna(co)
        lposibles = s_zonafc.poner_posibles_zona_en_lista(ssudoku, fi, co)
        for y in lfilas:
            for x in lcolumnas:
                if y != lfilas[2] or x != lcolumnas[2]:
                    if sposibles[y][x] != []:
                        lposibles = sposibles[y][x]
                        for num in lposibles:
                            esta = 0
                            for yy in lfilas:
                                for xx in lcolumnas:
                                    if yy != y or xx != x:
                                        if num in sposibles[yy][xx]:
                                            esta += 1
                                            break
                            if esta == 0:
                                ssudoku[y][x]= num
                                sposibles[y][x] = []
                                s_sudoku.recomponer_posibles(ssudoku)
                                volver = True
                                break
                        if volver:
                            break
            if volver:
                break
    return                            


def fila_con_dos_celdas_de_dos_posibles_iguales(ssudoku, fi):
    """ 
    PARAMETROS:
        fi => la fila, donde trabaja la funcion 
    PROCESO:
        recorro la fila buscando dos celdas que tengan dos numeros posibles y solo 
        dos, iguales
        Los borro de las otras celdas con posibles de la fila, y si queda alguna
        celda con un unico numero posible, lo estampo en la misma celda en el sudoku.
    DEVUELVE
        nada      
    """
    celdas_dobles = s_fila.fila_con_par_de_celdas_con_dos_posibles_iguales(ssudoku, fi)
    # miro todas las  celdas menos las que tienen los dos posibles iguales
    if len(celdas_dobles) > 0:
        # cojo los valores de uno de los dos
        ldobles = sposibles[fi][celdas_dobles[0]] 
        for co in range(9):
            if  co != celdas_dobles[0] and co != celdas_dobles[1]:
                if ldobles[0] in sposibles[fi][co]:
                        sposibles[fi][co].remove(ldobles[0])
                if ldobles[1] in sposibles[fi][co]:
                        sposibles[fi][co].remove(ldobles[1])
                if len(sposibles[fi][co]) == 1:
                    num = sposibles[fi][co]
                    ssudoku[fi][co] = num[0]
                    sposibles[fi][co] = []
    return 

def columna_con_dos_celdas_de_dos_posibles_iguales(ssudoku, co):
    """ 
    PARAMETROS:
        co => la columna, donde trabaja la funcion 
    PROCESO:
        recorro la columna buscando dos celdas que tengan dos numeros posibles y solo 
        dos, iguales
        Los borro de las otras celdas con posibles de la columna, y si queda alguna
        celda con un unico numero posible, lo estampo en la misma celda en el sudoku.
    DEVUELVE
        nada       
    """
    celdas_dobles = s_columna.columna_con_par_de_celdas_con_dos_posibles_iguales(ssudoku, co)
    # miro todas las  celdas menos las que tienen los dos posibles iguales
    if len(celdas_dobles) > 0 :
        # cojo los valores de uno de los dos
        ldobles = sposibles[celdas_dobles[0]][co]
        # miro todas las  celdas menos las que tienen los dos posibles iguales
        for fi in range(9):
            if  fi != celdas_dobles[0] and fi != celdas_dobles[1]:
                if ldobles[0] in sposibles[fi][co]:
                        sposibles[fi][co].remove(ldobles[0])
                if ldobles[1] in sposibles[fi][co]:
                        sposibles[fi][co].remove(ldobles[1])
                if len(sposibles[fi][co]) == 1:
                    num = sposibles[fi][co]
                    ssudoku[fi][co] = num[0]
                    sposibles[fi][co] = []
    return 


def zona_con_dos_celdas_de_dos_posibles_iguales(ssudoku, fi, co):
    """ 
    PARAMETROS:
        fi => la fila, nos sirve para determinar junto con la columna la zona 
        co => la columna, nos sirve para determinar junto con la fila la zona 
    PROCESO:
        recorro en la zona buscando dos celdas que tengan dos numeros posibles
        y solo dos iguales
        Los borro de las otras celdas con posibles de la zona, y si queda alguna
        celda con un unico numero posible, lo estampo en la misma celda en el sudoku.
    DEVUELVE
        nada       
    """
    # Busco celdas que tengan dos numeros posibles y las guardo
    celdas_dobles = s_zonafc.zona_con_par_de_celdas_con_dos_posibles_iguales(fi, co)
    if len(celdas_dobles) != 0:
        lnumeros_zona = s_zonafc.poner_numeros_con_ceros_de_la_zona_en_lista(ssudoku, fi, co)
    #    # detecto las filas y las columnas correspondientes a la zona segun fi, co
        lfilas =  s_fila.determinar_zona_fila(fi)
        lcolumnas = s_columna.determinar_zona_columna(co)
        # borramos los numeros posibles en las otras celdas
        lvalores = sposibles[celdas_dobles[0]][celdas_dobles[1]]
        y1 = celdas_dobles[0]
        x1 = celdas_dobles[1]
        y2 = celdas_dobles[2]
        x2 = celdas_dobles[3]
        for y in lfilas:
            for x in lcolumnas:
                if len(sposibles[y][x]) > 1:
                    if  y != y1 or x != x1:
                        if y != y2  or x != x2:
                            if  lvalores[0] in sposibles[y][x]:
                                sposibles[y][x].remove(lvalores[0])
                            if  lvalores[1] in sposibles[y][x]:
                                sposibles[y][x].remove(lvalores[1])   
        # Ahora ya trabajamos con las filas y columnas
        for y in lfilas:
            fila_con_dos_celdas_de_dos_posibles_iguales(ssudoku, y)
        for x in lcolumnas:
            columna_con_dos_celdas_de_dos_posibles_iguales(ssudoku, x)
    return 

def proceso_de_filas_con_par_celdas_de_dos_numeros_iguales(ssudoku):
    """
    PARAMETROS:
        nada
    PROCESO:
        recorremos las filas buscando un par de celdas que tenga el mismo par 
        de numeros posibles.
            Guardaremos el sudoku actual
            .-en una de las celdas estamparemos uno de los numeros, en la otra celda 
            estamparemos el otro.
            .-hacemos pasadas de los algoritmos, tendremos tres posibilidades:
                que en dos pasadas sucesivas nos devuelva los mismos ceros.
                que resuelva sudoku correctamente.
                que resuelva sudoku incorrectamente.
    DEVUELVE:
        True si se resolvio el sudoku y False en caso contrario
    """
    sssudoku = []
    for fi in range(9):
        sssudoku.append([0]* 9)
    # guardamos el estado actual del sudoku
    for y in range(9):
        for x in range(9):
            sssudoku[y][x] = ssudoku[y][x]
    # buscamos filas con dos celdas con dos y solo dos numeros, iguales            
    for fila in range(9):
        celdas_dobles = s_fila.fila_con_par_de_celdas_con_dos_posibles_iguales(ssudoku, fila)     
        total = len(celdas_dobles)
        if len(celdas_dobles) > 0:
            for cc in range(0,total,2):
                co1 = celdas_dobles[cc]
                co2 = celdas_dobles[cc+1]
                numeros = sposibles[fila][co1]           
                # probamos los numeros de las celdas que los tienen iguales
                for num in range(2): 
                    if num == 0:    
                        ssudoku[fila][co1] = numeros[0]
                        ssudoku[fila][co2] = numeros[1]
                    else:
                        ssudoku[fila][co1] = numeros[1]
                        ssudoku[fila][co2] = numeros[0]
                    if algoritmos(ssudoku):
                        return True
                    else:
                        # ponemos el sudoku a su estado anterior
                        for y in range(9):
                            for x in range(9):
                                    ssudoku[y][x] = sssudoku[y][x]
                        s_sudoku.recomponer_posibles(ssudoku)

    return False

def proceso_de_columnas_con_par_celdas_de_dos_numeros_iguales(ssudoku):
    """
    PARAMETROS:
        nada
    PROCESO:
        recorremos las columnas buscando un par de celdas que tenga el mismo par 
        de numeros posibles.
            Guardaremos el sudoku actual
            .-en una de las celdas estamparemos uno de los numeros, en la otra celda 
            estamparemos el otro.
            .-hacemos pasadas de los algoritmos, tendremos tres posibilidades:
                que en dos pasadas sucesivas nos devuelva los mismos ceros.
                que resuelva sudoku correctamente.
                que resuelva sudoku incorrectamente.
    DEVUELVE:
        True si se resolvio el sudoku y False en caso contrario
    """
    sssudoku = []
    for fi in range(9):
        sssudoku.append([0]* 9)
    # guardamos el estado actual del sudoku
    for y in range(9):
        for x in range(9):
            sssudoku[y][x] = ssudoku[y][x]
    # buscamos columnas con dos celdas de dos y solo dos numeros iguales            
    for columna in range(9):
        celdas_dobles = s_columna.columna_con_par_de_celdas_con_dos_posibles_iguales(ssudoku, columna)     
        total = len(celdas_dobles)
        if len(celdas_dobles) > 0:
            for cc in range(0,total,2):
                fi1 = celdas_dobles[cc]
                fi2 = celdas_dobles[cc+1]
                numeros = sposibles[fi1][columna]           
                # probamos los numeros de las celdas que los tienen iguales
                for num in range(2): 
                    if num == 0:    
                        ssudoku[fi1][columna] = numeros[0]
                        ssudoku[fi2][columna] = numeros[1]
                    else:
                        ssudoku[fi1][columna] = numeros[1]
                        ssudoku[fi2][columna] = numeros[0]
                    if algoritmos(ssudoku):
                        return True
                    else:
                        # ponemos el sudoku a su estado anterior
                        for y in range(9):
                            for x in range(9):
                                ssudoku[y][x] = sssudoku[y][x]
                        s_sudoku.recomponer_posibles(ssudoku)

    return False

def proceso_con_celdas_de_dos_numeros(ssudoku):
    """
    PARAMETROS:
    PROCESO:
        recorremos las celdas con dos numeros posibles y los guardamos.
        de cada celda hacemos pruebas con los numeros posibles de cada una de ellas
        esperando que termine resolviendose el sudoku.
   DEVUELVE:
       True si sudoku no contiene ceros, en caso contrario devuelve False
    """
    sssudoku = []
    for fi in range(9):
        sssudoku.append([0]* 9)
    # guardamos el estado actual del sudoku
    for y in range(9):
        for x in range(9):
            sssudoku[y][x] = ssudoku[y][x]
    # buscamos celdas con dos numeros posibles y solo dos            
    lfilas = []
    lcolumnas = []
    for y in range(9):
        for x in range(9):
            if len(sposibles[y][x]) == 2:
                lfilas.append(y)
                lcolumnas.append(x)
    # recorremos las celdas con solo dos numeros posibles
    cant = len(lfilas)
    if cant != 0:
        for indice in range(cant):
            valores = sposibles[lfilas[indice]][lcolumnas[indice]]            
            for num in valores:
                # estampamos num  en el sudoku
                ssudoku[lfilas[indice]][lcolumnas[indice]] = num
                if algoritmos(ssudoku):
                    return True
                else:
                    # ponemos el sudoku a su estado anterior
                    for y in range(9):
                        for x in range(9):
                            ssudoku[y][x] = sssudoku[y][x]
                    s_sudoku.recomponer_posibles(ssudoku)
    return False
   
def algoritmos(ssudoku):
    hacer = 0
    cant_ant = 1

    while hacer < 8 :
        s_sudoku.recomponer_posibles(ssudoku)
        for fi in [1,3,6]:
            estampar_en_zonas_de_tres_filas(ssudoku, fi)
        
        for co in [1,3,6]:
            estampar_en_zonas_de_tres_columnas(ssudoku, co)
        
        for x in range(9):
            numero_posible_unico_en_toda_la_fila(ssudoku, x)
        
        for x in range(9):    
            numero_posible_unico_en_toda_la_columna(ssudoku, x)
        
        for y in [1,3,6]:
            for x in [1,3,6]:
                numero_posible_unico_en_toda_la_zona(ssudoku, y, x)

        for fi in range(9):
            fila_con_dos_celdas_de_dos_posibles_iguales(ssudoku, fi)  
            s_sudoku.recomponer_posibles(ssudoku)   
        
        for co in range(9):
            columna_con_dos_celdas_de_dos_posibles_iguales(ssudoku, co)
            s_sudoku.recomponer_posibles(ssudoku)   

        for y in [0,3,6] :
            for x in [0,3,6]:
                zona_con_dos_celdas_de_dos_posibles_iguales(ssudoku, y, x)
        s_sudoku.buscar_celdas_con_un_unico_posible(ssudoku)        
        cant = s_sudoku.busco_ceros_en_sudoku(ssudoku)
        # si se repite la cantidad cant, salimos 
        if cant_ant != cant:
            if cant > 0:   
                #print('Hacer => {} ceros => {}'.format(hacer, cant))
                cant_ant = cant
                hacer += 1
            else:
                #print('Hacer => {} ceros => {}'.format(hacer, cant))
                return True
        else:
            print('salir de Hacer => {} ceros => {}'.format(hacer, cant))
            return False
                        
                 
def inicio(ssudoku):
    
    if algoritmos(ssudoku):
        salida = True
    else:
        # procesos especiales con celdas de dos numeros posibles
        print('procesos especiales')
        if proceso_de_filas_con_par_celdas_de_dos_numeros_iguales(ssudoku):
            salida = True
        else:
            if proceso_de_columnas_con_par_celdas_de_dos_numeros_iguales(ssudoku):
                salida = True
            else:
                if proceso_con_celdas_de_dos_numeros(ssudoku):
                    salida = True
                else:
                    salida = False
                
    # ofrecemos salida segun variable (salida)
    if salida:     
        if s_sudoku.verificar_solucion_sudoku(ssudoku):
            print('FINALIZADO CORRECTAMENTE')
            print('!!!!  E U R E K A  ¡¡¡¡¡ ') 

        else:
            print('!!!!           no tiene ceros             ¡¡¡¡¡ ') 
            print('!!!! pero no cumple las normas del sudoku ¡¡¡¡¡ ') 
    else:
            print('!!!!    cumple las normas del sudoku      ¡¡¡¡¡ ') 
            print('!!!!          pero quedan ceros           ¡¡¡¡¡ ') 
    print('')
    return 