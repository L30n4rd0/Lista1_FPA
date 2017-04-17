# -*- coding: utf-8 -*-
'''
Created on 29/03/2017

@author: leonardo
'''

def printMagicSquare(magicSquare):

    for row in range(len(magicSquare)):
        str_row = ''
        for column in range(len(magicSquare)):
            str_row = str_row + ' %02d |' % magicSquare[row][column]
        print str_row

def Insert_next_value(value):
    global balloon_row, balloon_column

    # Check if the row above and column on the right side is free.
    if (balloon_row-1 < 0 and balloon_column+1 < matrix_size):
        
        if (magicSquare[matrix_size - 1][balloon_column + 1] == 0):
            balloon_row = matrix_size - 1
            balloon_column = balloon_column + 1
            
            magicSquare[balloon_row][balloon_column] = value
        else:
            balloon_row = balloon_row + 1
            balloon_column = balloon_column
            
            magicSquare[balloon_row][balloon_column] = value
    
    # Check if there is enough column to enter the value
    elif (balloon_row-1 >= 0 and balloon_column+1 == matrix_size):
        
        if (magicSquare[balloon_row - 1][0] == 0):
            balloon_row = balloon_row - 1
            balloon_column = 0
            
            magicSquare[balloon_row][balloon_column] = value
        else:
            balloon_row = balloon_row + 1
            balloon_column = balloon_column
            
            magicSquare[balloon_row][balloon_column] = value
    
    # In case it is correct and can add a value based on the rule of origin
    elif (balloon_row-1 >= 0 and balloon_column+1 < matrix_size):
        if (magicSquare[balloon_row - 1][balloon_column + 1] == 0): 

            balloon_row = balloon_row - 1
            balloon_column = balloon_column + 1
            
            magicSquare[balloon_row][balloon_column] = value
        else:
            
            balloon_row = balloon_row + 1
            balloon_column = balloon_column
            
            magicSquare[balloon_row][balloon_column] = value
    
    # If there is no column and no row
    elif (balloon_row-1 < 0 and balloon_column+1 == matrix_size):
    
        balloon_row = balloon_row + 1
        balloon_column = balloon_column
        
        magicSquare[balloon_row][balloon_column] = value
        
# **** EXECUTION****
magicSquare = [[0 for x in range(5)] for y in range(5)]
matrix_size = len(magicSquare)

balloon_row = 0
balloon_column = len(magicSquare)/2

# insert the first value to matrix (row 1 and column 3)
magicSquare[balloon_row][balloon_column] = 1

for valor in range(2, (matrix_size**2)+1):
    Insert_next_value(valor)

print printMagicSquare(magicSquare)
