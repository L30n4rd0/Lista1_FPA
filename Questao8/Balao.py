# -*- coding: utf-8 -*-
'''
Created on 30 de mar de 2017

@author: leonardo
'''
import time

def print_matrix(matrix_param):
    matrix_width = len(matrix_param[0])
    matrix_height = len(matrix_param)
     
    for row in range(matrix_height-1, -1, -1):
        str_row = ''
         
        for column in range(matrix_width):
            str_row = str_row + '  ' + str(matrix_param[row][column])
             
        print str_row + '\n'
     
    print '       1  2  3  4  5  6  7  8  9  10 11\n'
  
def create_obstacles(matrix_param, segment_param):
    
    for coordinate in segment_param:
        segment_row = coordinate[0]
        segment_column = coordinate[1]
        matrix_param[segment_row][segment_column] = '#'
        
def create_margin(matrix_param):
    matrix_width = len(matrix_param[0])
    matrix_height = len(matrix_param)
     
    # top
    for j in range(matrix_width):
        matrix_param[matrix_height-1][j] = '#'
         
    # bottom
    for j in range(matrix_width):
        matrix_param[0][j] = '#'
      
    # left
    for i in range(matrix_height):
        if i > 0 and i < matrix_height-1:
            matrix_param[i][0] = str(i) + ' #'
             
        else:
            matrix_param[i][0] = '  #'
     
    #right
    for i in range(matrix_height):
        matrix_param[i][matrix_width-1] = '#'
        
def validate_segment(segment):
    
    initial_coordinate = [segment[0], segment[1]]
    final_coordinate = [segment[2], segment[3]]
    
    resulting_segment = []
    
    # growing segment
    if (initial_coordinate[1] < final_coordinate[1]):
        # validate angle 45 grads
        if ( abs(initial_coordinate[0] - initial_coordinate[1]) ==
            abs(final_coordinate[0] - final_coordinate[1]) ):
            
            range_X_coordinates = range(initial_coordinate[0], final_coordinate[0] + 1);
            range_Y_coordinates = range(initial_coordinate[1], final_coordinate[1] + 1);
            
            # insert the coordinates between initial and final coordinates to resulting_segment
            for i in range(len(range_X_coordinates)):
                # converting coordinate 'x, y' to 'row, column'
                resulting_segment.append([ range_Y_coordinates[i], range_X_coordinates[i] ])
        
        else:
            resulting_segment.append(False)
            resulting_segment.append('A reta não tem um ângulo de 45 ou 135 ou 180 graus\n')
        
    # decreasing segment
    elif (initial_coordinate[1] > final_coordinate[1]):
        
        # validate angle 135 grads
        if (abs(initial_coordinate[0] + initial_coordinate[1]) ==
            abs(final_coordinate[0] + final_coordinate[1])):
            
            range_X_coordinates = range(initial_coordinate[0], final_coordinate[0] + 1);
            range_Y_coordinates = range(initial_coordinate[1], final_coordinate[1] - 1, -1);
            
            # insert the coordinates between initial and final coordinates to resulting_segment
            for i in range(len(range_X_coordinates)):
                # converting coordinate 'x, y' to 'row, column'
                resulting_segment.append([ range_Y_coordinates[i], range_X_coordinates[i] ])
                
        else:
            resulting_segment.append(False)
            resulting_segment.append('A reta não tem um ângulo de 45 ou 135 ou 180 graus\n')
        
    # horizontal segment
    else:
        range_X_coordinates = range(initial_coordinate[0], final_coordinate[0] + 1);
        
        # insert the coordinates between initial and final coordinates to resulting_segment
        for i in range(len(range_X_coordinates)):
            # converting coordinate 'x, y' to 'row, column'
            resulting_segment.append([ initial_coordinate[1], range_X_coordinates[i] ])
    
    return resulting_segment
        
# **** EXECUTION**************

# create matrix
matrix = [['.' for x in range(13)] for y in range(8)]

# create matrix margin
create_margin(matrix)

# show matrix 
print_matrix(matrix)

# insert number of segments and queries
segments_and_queries_numbers = raw_input('Digite o número de segmentos e consultas separados por espaço: ')
segments_and_queries_numbers = map(int, segments_and_queries_numbers.split(' '))

# get the segments coordinates
for i in range(segments_and_queries_numbers[0]):
    validated_segment = [False]
    
    while (not validated_segment[0]):
        segment_coordinates = raw_input('Digite as coordenadas do segmento %d separadas por espaço (X1 Y1 X2 Y2): ' % (i+1))
        segment_coordinates = map(int, segment_coordinates.split(' '))
        
        validated_segment = validate_segment(segment_coordinates)
        
        if (validated_segment[0]):
            create_obstacles(matrix, validated_segment)
            print_matrix(matrix)
            
        else:
            print "\nO segmento inserido não é valido!"
            print validated_segment[1]

queries_numbers = []
for i in range(segments_and_queries_numbers[1]):
    queries_numbers.append(
        input('Digite a coordenada que será realizada a consulta %d: ' % (i +1))
    )

final_report = {}

for querie_number in queries_numbers:
    balloon_column = querie_number
    balloon_row = 1
    
    for second in range(3, -1, -1):
        print 'Iniciando a consulta na coordenada %d em: %d segundos' % (querie_number, second)
        time.sleep(1)

    while True:
        time.sleep(1)
          
        # verifica se tem obstaculo a sua direta e nao tem nada a sua esquerda e possui obstaculo acima
        if(matrix[balloon_row][balloon_column+1] == '#' and 
           matrix[balloon_row][balloon_column-1] == '.' and 
           matrix[balloon_row+1][balloon_column] == '#'):
              
            matrix[balloon_row][balloon_column] = '.'
            balloon_column = balloon_column - 1
            balloon_row = balloon_row + 1
            matrix[balloon_row][balloon_column] = 0
              
        elif(matrix[balloon_row][balloon_column-1] == '#' and 
             matrix[balloon_row][balloon_column+1]== '.' and 
             matrix[balloon_row+1][balloon_column] == '#'):
              
            matrix[balloon_row][balloon_column] = '.'
            balloon_column = balloon_column + 1
            balloon_row = balloon_row + 1
            matrix[balloon_row][balloon_column] = 0
              
        elif(matrix[balloon_row][balloon_column-1] == '.' and 
             matrix[balloon_row][balloon_column+1]== '.' and 
             matrix[balloon_row+1][balloon_column] == '#' and 
             matrix[balloon_row+1][balloon_column+1] == '#' and 
             matrix[balloon_row+1][balloon_column-1] == '.'):
              
            matrix[balloon_row][balloon_column] = '.'
            balloon_column = balloon_column - 1
            balloon_row = balloon_row - 1
            matrix[balloon_row][balloon_column] = 0
              
        elif(matrix[balloon_row][balloon_column-1] == '.' and 
             matrix[balloon_row][balloon_column+1]== '.' and 
             matrix[balloon_row+1][balloon_column] == '#' and 
             matrix[balloon_row+1][balloon_column+1] == '.' and 
             matrix[balloon_row+1][balloon_column-1] == '#'):
              
            matrix[balloon_row][balloon_column] = '.'
            balloon_column = balloon_column + 1
            balloon_row = balloon_row + 1
            matrix[balloon_row][balloon_column] = 0
              
        elif(matrix[balloon_row][balloon_column-1] == '.' and 
             matrix[balloon_row][balloon_column+1]== '.' and 
             matrix[balloon_row+1][balloon_column] == '#' and 
             matrix[balloon_row+1][balloon_column+1] == '#' and 
             matrix[balloon_row+1][balloon_column-1] == '#'):
            
            # converting coordinate 'row, column' to 'x, y'
            if (balloon_row == 6):
                final_report[querie_number] = [balloon_column, '']
                
            else:
                final_report[querie_number] = [balloon_column, balloon_row]
                
            matrix[balloon_row][balloon_column] = '.'
            
            break
        
        else:
            matrix[balloon_row][balloon_column] = '.'
            balloon_row = balloon_row + 1
            matrix[balloon_row][balloon_column] = 0
          
        print print_matrix(matrix)
        
print '****Resultado final das consultas:****'

for querie_number in queries_numbers:
    print 'Consulta na coordenda' + str(querie_number) + ' -> posição final do balão: [' + str(final_report[querie_number][0]) + ', ' + str(final_report[querie_number][1]) + ']'
