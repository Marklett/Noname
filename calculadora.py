def suma(val1,val2):
    return val1+val2
def resta(val1,val2):
    return val1-val2
def mult(val1,val2):
    return val1*val2
def div(val1,val2):
    return val1/val2
    
def operation():
    print("Ingrese dos valores")
    x = int(input())
    y = int(input())
    b=bool(True)
    while(b):
        print("\nSeleccione la operacion que desea ingresar")
        print("0 para salir\n1 para suma\n2 para resta\n3 para mult\n para div")
        z=int(input())
        if (z==1):
            print(suma(x,y))
        elif (z==2):
            print(resta(x,y))
        elif (z==3):
            print(mult(x,y))
        elif (z==4):
            print(div(x,y))
        else:
            b = bool(False)

operation()