# -*- coding: utf-8 -*-
'''
Created on 29/03/2017

@author: leonardo
'''

# o usuario fornece um tamanho para fita
tape_size = input('Digite o tamanho da fita: ')
original_tape = raw_input('Digite os elementos da fita separados por espaço: ')
original_tape = map(int, original_tape.split(' '))

# verifica se o tamanho da fita fornecida pelo usuario eh menor que 15 e maior ou igual a 1
if (tape_size >=1 and tape_size <= 15):
      
    # o usuario fornece o tamanho para do corte que sera realizado
    final_tape_size = input('Digite o tamanho da fita dobrada: ')
    final_tape = raw_input('Digite os elementos da fita dobrada separados por espaço: ')
    final_tape = map(int, final_tape.split(' '))
    
    helper_tape = []
    point_court = len(original_tape)
    
    while (helper_tape != final_tape and point_court >= 0):
        tape_left_point_court = original_tape[ :point_court]
        tape_right_point_court = original_tape[point_court: ]
        
        tape_right_point_court.reverse()
        
        if (len(tape_left_point_court) > len(tape_right_point_court)):
            range_para_for = range(-len(tape_right_point_court), 0, 1)
            helper_tape = tape_left_point_court
        
        else:
            range_para_for = range(-len(tape_left_point_court), 0, 1)
            helper_tape = tape_right_point_court
        
        # sum croped tapes
        for i in range_para_for:
            helper_tape[i] = tape_left_point_court[i] + tape_right_point_court[i]
        
        point_court -= 1
        
    if (helper_tape == final_tape):
        print "\nResultado: S"
        
    else:
        print "\nResultado: N"
          
else:
    print 'Tamanho da fita invalido! Forneca um valor menor que 15!\n\nResultado: N'

