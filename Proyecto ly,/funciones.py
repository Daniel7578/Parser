import re
from xml.dom.minidom import Element
from numpy import empty, true_divide


def defvar(archivo, id):
    nombreVar= ""
    valorVar= 0
    nombre = archivo[id]
    valor = archivo[id+1]
    tipoN = type(nombre)
    tipoV = type(valor)
    if tipoN == str:
        nombreVar = nombre
    if tipoV == str:
        try: 
            x = int(valor)
            valorVar = x 
        except ValueError:
            return False
    return nombreVar,valorVar
def asignar (archivo,id,variables):
    valorVar=0
    variable=archivo[id]
    valor=archivo[id+1]
    tipoV = type(valor)
    if tipoV == str:
        try: 
            x = int(valor)
            valorVar = x 
        except ValueError:
            return False
    if variable in variables:
        variables[variable]=valorVar
        return True
    else:
        return False

def avance(archivo,id,variables):
    lineas=archivo[id]
    tipoN = type(lineas)
    if lineas in variables:
        return True
    elif tipoN ==str:
        try: 
            x = int(lineas)
            return True
        except ValueError:
            return False
def turn (archivo,id,direcciones):
    lineas=archivo[id]
    if lineas in direcciones:
        return True
    else:
        return False
def put(archivo,id,variables,boc):
    x=archivo[id]
    valor = archivo[id+1]
    tipoV = type(valor)
    if x in boc:
        if valor in variables:
            return True
        elif tipoV == str:
            try: 
                c = int(valor)
                return True
            except ValueError:
                return False
def moveDir (archivo,id,direcciones,variables):
    linea = archivo[id]
    dir=archivo[id+1]
    tipon=type(linea)
    if linea in variables:
        if dir in direcciones:
            return True
    elif tipon==str:
        try:
            c=int(linea)
            return True
        except ValueError:
            return False
    else: 
        return False
def runDirs (archivo,id,direcciones):
    linea = archivo[id]
    elementos = linea.split()
    lista = elementos[1]
    if len(lista) != 0:
        for instruccion in lista:
            if instruccion is not direcciones:
                return False
        return True

def moveface(archivo,id,variables,direcciones):
    linea=archivo[id]
    elementos=linea.split(" ")
    presencia=var(1,variables,elementos)
    if presencia==True:
        if elementos[2] in direcciones:
            return True
        else:
            return False

def var (id,variables,linea):
    valor=linea[id]
    valorsin=linea[id].strip(")")
    if valorsin in variables:
        return True
    elif ")" in valor:
        a = valor.strip(")")
        try: 
            c = int(a)
            return True
        except ValueError:
            return False
    


        
    

    
    
    




    
