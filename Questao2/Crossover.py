# -*- coding: utf-8 -*-
'''
Created on 22/03/2017

@author: leonardo
'''
from random import randint

s1 = raw_input("Didite uma string: ")
s2 = raw_input("Didite outra string com mesmo tamanho da anterior: ")

p = randint(1, len(s1)-1)
    
print "p = " + str(p)

# gera 2 substring a partir do p gerado aleatório
s1_substring = s1[ p:len(s1) ]
s2_substring = s2[ p:len(s2) ]

# as strings originais recebem substrings da parte inicial do ponto p
s1 = s1[ 0:p ]
s2 = s2[ 0:p ]

# as strings originais recebem as substrings invertidas, para fazer o crossover
s1 = s1 + s2_substring
s2 = s2 + s1_substring

print "s1 = " + s1
print "s2 = " + s2
