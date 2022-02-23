import re
import funciones as ft
archivo = open("input.txt")
lineas = archivo.readlines()
ControlParentesis = 0
variables = {}
tokens = []
direccionesturn = ["rigth", "left", "arround"]
direccionesFace = ["north","south","east","west"]
boc=["Balloons","Chips"]
direccionesMove = ["front","rigth","left","back"]
comandos = ["defvar", "=", "move", "turn", "face","put", "pick","move-dir","run-dirs","move-face","skip"]
condiciones = ["facing", "can-put","can-pick","can","not"]
def Analisis(InstruccionAprocesar,i,tokens,controlParentesis):
    centinela = controlParentesis
    j = i+1
    while centinela !=0:
        itemAprocesar = tokens[j]
        if itemAprocesar == "(":
            centinela += 1
        if itemAprocesar != ")" and itemAprocesar != "(":
            InstruccionAprocesar.append(itemAprocesar)
        elif itemAprocesar == ")":
            centinela -=1
        j +=1
    return InstruccionAprocesar
def Verificar (lista,variables,direccionesFace,direccionesMove,direccionesturn,boc,comandos,condiciones):
    i = 0
    while i < len(lista):
        item = lista[i]
        if item in comandos:
            if item =="defvar":
                defvar = ft.defvar(lista,i+1)
                if defvar == False:
                    return False
                else:
                    variables[defvar[0]]= defvar[1]
            elif item =="=":
                asignacion = ft.asignar(lista,i+1,variables)
                if asignacion ==False:
                    return False
                
            elif item =="move":
                move = ft.avance(lista,i+1,variables)
                if move == False:
                    return False
            elif item =="turn":
                turn = ft.turn(lista,i+1,direccionesturn)
                if turn ==False:
                    return False
            elif item =="face":
                face = ft.turn(lista,i+1,direccionesFace)
                if face == False:
                    return False
            elif item =="put":
                put = ft.put(lista,i+1,variables,boc)
                if put == False:
                    return False
            elif item =="pick":
                pick=ft.put(lista,i+1,variables,boc)
                if pick== False:
                    return False
            elif item =="move-dir":
                movedir=ft.moveDir(lista,i+1,direccionesMove,variables)
                if movedir==False:
                    return False
            elif item =="run-dirs":
            elif item =="move-face":
            elif item =="skip":

        elif item =="defun":
        elif item =="if":
        elif item =="repeat":
        else:
            return False

        
        i+=1

for line in lineas:
        line = line.replace('(',' ( ')
        line = line.replace(')',' ) ')
        token = line.strip().split()
        for tok in token:
            tokens.append(tok)
i = 0
while i < len(tokens):
    lista =[]
    if ControlParentesis == 0:
        elemento = tokens[i]
        if elemento == "(":
            ControlParentesis +=1
    elif ControlParentesis >  0:
        lista = Analisis(lista,i,tokens,ControlParentesis)
        centinela = Verificar(lista,variables,direccionesFace,direccionesMove,direccionesturn,boc,comandos,condiciones)






    else:
        lista.append(elemento)

    i+=1





