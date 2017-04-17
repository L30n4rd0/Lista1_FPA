# -*- coding: utf-8 -*-
'''
Created on 22/03/2017

@author: leonardo
'''

listA = []
listB = []
differenceList = []
unionList = []
intersectionList = []

insert = True
menuText = "Digite um número para inserir na listaA\nDigite 'exit' para finalizar inserção:\n"

while (insert):
    element = raw_input(menuText)
    if (element != "exit"):
        listA.append( int(element) )
    
    else:
        insert = False


insert = True
menuText = "Digite um número para inserir na listaB\nDigite 'exit' para finalizar inserção:\n"

while (insert):
    element = raw_input(menuText)
    if (element != "exit"):
        listB.append( int(element) )
    
    else:
        insert = False

print listA
print listB

for element in listA:
    
    # add listA's elements to unionList
    if ( not(unionList.count(element)) ):
            unionList.append(element)
            
    # add commons listA and listB elements to intersectionList
    if (listB.count(element)):
        if ( not(intersectionList.count(element)) ):
            intersectionList.append(element)
            
    # add the not presents elements in listB to differenceList
    if ( not(listB.count(element)) ):
        if ( not(differenceList.count(element)) ):
            differenceList.append(element)
    
for element in listB:
    
    # add the listB's elements to unionList
    if ( not(unionList.count(element)) ):
            unionList.append(element)

print 'A união B: ' + str(unionList)
print 'A intersecção B: ' + str(intersectionList)
print 'A - B: ' + str(differenceList)

