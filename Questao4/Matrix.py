# -*- coding: utf-8 -*-
'''
Created on 22/03/2017

@author: leonardo
'''
from random import randint

def initMatrix():
    i = 0
    global biggertElement
    global smallerElement
    
    while (i < len(matrix)):
        j = 0
        while (j < len(matrix[i])):
            
            # new random element of 0 to 99
            newElement = randint(0, 99)
            
            # if new random element exists into matrix, other new element is generated
            while (containesElement(newElement)):
                newElement = randint(0, 99)
            
            # new random element inserted into matrix
            matrix[i][j] = newElement
            
            if (newElement > biggertElement):
                biggertElement = newElement
             
            if (newElement < smallerElement):
                smallerElement = newElement
            
            j += 1
        
        i += 1
     
def containesElement(element):
    # this method check if element already exists in the matrix
    for column in matrix:
        if (column.count(element)):
            return True
        
    return False

def normalizeElement(element):
    return float(element) / (biggertElement - smallerElement)

def normalizeMatrix():
    i = 0
    
    while (i < len(matrix)):
        j = 0
        while (j < len(matrix[i])):
            
            matrix[i][j] = normalizeElement(matrix[i][j])
            
            j += 1
        
        i += 1
        
def printMatrix(matrixParam):

    for row in range(len(matrixParam)):
        str_row = ''
        for column in range(len(matrixParam)):
            str_row = str_row + ' %.02f |' % matrixParam[row][column]
        print str_row

##### START EXECUTION #####

matrix = [[0 for x in range(5)] for y in range(5)] #create matrix 5x5
biggertElement = 0
smallerElement = 100

initMatrix()

print 'Matriz inicial:'
printMatrix(matrix)

normalizeMatrix()

print 'Matriz normalizada:'
printMatrix(matrix)
