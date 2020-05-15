#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 07:31:54 2019

@author: popscra
"""
# ============================================ < EXPERTO > ======================

sudoku = []
for fi in range(9):
    sudoku.append([0]*9)
#print(sudoku)
def llenar_sudoku_con_datos_en_modu00():
    sudoku[0][0] = 0  
    sudoku[0][1] = 0 #
    sudoku[0][2] = 0 #
    sudoku[0][3] = 0 #
    sudoku[0][4] = 0 #  
    sudoku[0][5] = 4 #
    sudoku[0][6] = 7 #
    sudoku[0][7] = 0 #
    sudoku[0][8] = 0
    
    sudoku[1][0] = 0 
    sudoku[1][1] = 0 # 
    sudoku[1][2] = 0 #
    sudoku[1][3] = 0 
    sudoku[1][4] = 0 # 
    sudoku[1][5] = 0 
    sudoku[1][6] = 6 #
    sudoku[1][7] = 0 #
    sudoku[1][8] = 3 #
    
    sudoku[2][0] = 4 #
    sudoku[2][1] = 0 #
    sudoku[2][2] = 1  
    sudoku[2][3] = 0 
    sudoku[2][4] = 0
    sudoku[2][5] = 0 #
    sudoku[2][6] = 0 
    sudoku[2][7] = 0 #
    sudoku[2][8] = 0 #
    
    sudoku[3][0] = 0 # 
    sudoku[3][1] = 5 
    sudoku[3][2] = 0 #  
    sudoku[3][3] = 0 # 
    sudoku[3][4] = 6
    sudoku[3][5] = 0 # 
    sudoku[3][6] = 0 #
    sudoku[3][7] = 0 #
    sudoku[3][8] = 0 #  
    
    sudoku[4][0] = 0 # 
    sudoku[4][1] = 0 # 
    sudoku[4][2] = 0
    sudoku[4][3] = 0 # 
    sudoku[4][4] = 0
    sudoku[4][5] = 0
    sudoku[4][6] = 3 #
    sudoku[4][7] = 8 #
    sudoku[4][8] = 0 #
    
    
    sudoku[5][0] = 0 
    sudoku[5][1] = 3 #
    sudoku[5][2] = 0 #
    sudoku[5][3] = 5 #5
    sudoku[5][4] = 7 #
    sudoku[5][5] = 0 #
    sudoku[5][6] = 0 #
    sudoku[5][7] = 0 #
    sudoku[5][8] = 0 #
    
    
    sudoku[6][0] = 9 
    sudoku[6][1] = 0 
    sudoku[6][2] = 0 #
    sudoku[6][3] = 4 
    sudoku[6][4] = 0 #
    sudoku[6][5] = 0 #
    sudoku[6][6] = 0 #
    sudoku[6][7] = 0  
    sudoku[6][8] = 0 #
     
    sudoku[7][0] = 8 #
    sudoku[7][1] = 0 #
    sudoku[7][2] = 0 #
    sudoku[7][3] = 0 # 
    sudoku[7][4] = 0 #
    sudoku[7][5] = 0 # 
    sudoku[7][6] = 0 
    sudoku[7][7] = 9 #9
    sudoku[7][8] = 2 #
    
    sudoku[8][0] = 0 #
    sudoku[8][1] = 0 #
    sudoku[8][2] = 0 #
    sudoku[8][3] = 3 #
    sudoku[8][4] = 5 
    sudoku[8][5] = 0 
    sudoku[8][6] = 0 
    sudoku[8][7] = 0 #
    sudoku[8][8] = 0 
    
    return sudoku


