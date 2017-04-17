# -*- coding: utf-8 -*-
'''
Created on 22/03/2017

@author: leonardo
'''

def printMatrix():

    for m in range(size):
        print matrix[m]
    
def timePlayerX():
    
    rowAndColumn = raw_input("Vez do Jogador X: ")
    lin, col = map(int, rowAndColumn.split(' '))
    print '\n'
    
    if(matrix[int(lin)][int(col)] == "."):
        matrix[int(lin)][int(col)] = "X"
    else:
        print("Casa Ocupada!")
        timePlayerX()

def timePlayerO():
    
    rowAndColumn = raw_input("Vez do Jogador O: ")
    lin, col = map(int, rowAndColumn.split(' '))
    print '\n'
    
    if(matrix[int(lin)][int(col)] == "."):
        matrix[int(lin)][int(col)] = "O"
    else:
        print("Casa Ocupada!")
        timePlayerO()

def verifyTie():

    if(counter == 9):
        print("Jogo empado!")
        global control
        control = False

def verifyVictory():
    
    # Verify player X rows
    if((matrix[0] == ['X', 'X', 'X']) or (matrix[1] == ['X', 'X', 'X']) or (matrix[2] == ['X', 'X', 'X'])):
        print("Jogador X ganhou!")
        global control
        control = False

    # Verify player X columns
    if((matrix[0][0] == 'X' and matrix[1][0] == 'X' and matrix[2][0] == 'X')):
        print("Jogador X ganhou!")
        global control
        control = False

    if((matrix[0][1] == 'X' and matrix[1][1] == 'X' and matrix[2][1] == 'X')):
        print("Jogador X ganhou!")
        global control
        control = False

    if((matrix[0][2] == 'X' and matrix[1][2] == 'X' and matrix[2][2] == 'X')):
        print("Jogador X ganhou!")
        global control
        control = False

    # Verify player X diagonals
    if((matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X')):
        print("Jogador X ganhou!")
        global control
        control = False

    if((matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix[2][0] == 'X')):
        print("Jogador X ganhou!")
        global control
        control = False
       
    # Verify player O rows
    if((matrix[0] == ['O', 'O', 'O']) or (matrix[1] == ['O', 'O', 'O']) or (matrix[2] == ['O', 'O', 'O'])):
        print("Jogador O ganhou!")
        global control
        control = False
        
    # Verify player O columns
    if((matrix[0][0] == 'O' and matrix[1][0] == 'O' and matrix[2][0] == 'O')):
        print("Jogador O ganhou")
        global control
        control = False

    if((matrix[0][1] == 'O' and matrix[1][1] == 'O' and matrix[2][1] == 'O')):
        print("Jogador O ganhou!")
        global control
        control = False

    if((matrix[0][2] == 'O' and matrix[1][2] == 'O' and matrix[2][2] == 'O')):
        print("Jogador O ganhou!")
        global control
        control = False

    # Verify player O diagonals
    if((matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O')):
        print("Jogador O ganhou!")
        global control
        control = False

    if((matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix[2][0] == 'O')):
        print("Jogador O ganhou!")
        global control
        control = False

##### START EXECUTION #####
size = 3
control = True
counter = 0

# Create matrix
matrix = [['.' for x in range(size)] for y in range(size)]

printMatrix()

while control:
    
    timePlayerX()
    printMatrix()
    verifyVictory()
    counter = counter + 1
    verifyTie()
    
    if(control == False):
        break
    
    timePlayerO()
    printMatrix()
    verifyVictory()
    counter = counter + 1

    if(control == False):
        break

