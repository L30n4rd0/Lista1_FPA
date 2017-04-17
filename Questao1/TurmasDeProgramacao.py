# -*- coding: utf-8 -*-
'''
Created on 21/03/2017

@author: leonardo
'''
classes = {
          "A" : {
                 "students_number" : 4,
                 "students" : {
                             "01" : "P",
                             "02" : "P",
                             "03" : "P",
                             "04" : "A"
                             }
                 },
          
          "B" : {
                 "students_number" : 3,
                 "students" : {
                             "05" : "P",
                             "06" : "P",
                             "07" : "P"
                             }
                 },
          
          "C" : {
                 "students_number" : 5,
                 "students" : {
                             "08" : "P",
                             "09" : "A",
                             "10" : "P",
                             "11" : "P",
                             "12" : "P"
                             }
                 },
          
          "D" : {
                 "students_number" : 5,
                 "students" : {
                             "13" : "P",
                             "14" : "A",
                             "15" : "A",
                             "16" : "A",
                             "17" : "P"
                             }
                 },
          
          "E" : {
                 "students_number" : 5,
                 "students" : {
                             "18" : "P",
                             "19" : "A",
                             "20" : "P",
                             "21" : "P",
                             "22" : "P"
                             }
                 }
          }

for class_item in classes.items():
    count_students_absence = 0.0
     
    dictAlunos = {}
    dictAlunos = class_item[1]["students"]
     
    for statusPresenca in dictAlunos.values():
        if (statusPresenca == "A"):
            count_students_absence += 1.0
    
    absence_percentage = (count_students_absence / class_item[1]["students_number"]) * 100
    
    class_item[1]["absence"] = absence_percentage
    
print "Porcentagem de ausência em todas as turmas"
for class_item in classes.items():
    print class_item[0] + " : " + str(class_item[1]["absence"]) + "%"
    
print "\nTurmas com porcentagem de ausência maior que 5%"
for class_item in classes.items():
    if (class_item[1]["absence"] > 5.0):
        print class_item[0] + " : " + str(class_item[1]["absence"]) + "%"
    
    