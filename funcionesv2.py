print("\nMás sobre funciones")
# Aqui se escriben las funciones

def sumaab(a,b):
    s=a+b
    return s

def res(c,d):
    r=c-d
    return r

def multi(e,f):
    m=e*f
    return m

def div(g,h):
    d=g/h
    return d

#Llamadas a funciones

print("calculando suma")
n1=float(input("ingresa el primer numero: "))
n2=float(input("ingresa el segundo numero: "))
suma=sumaab(n1,n2)
print(f"la suma de {n1} + {n2} es: {suma}")

print("\ncalculando resta")
nr1=float(input("ingresa el primer numero: "))
nr2=float(input("ingresa el segundo numero: "))
resta=res(nr1,nr2)
print(f"La resta de {nr1} - {nr2} es: {resta}")

print("\n Calculando multiplicacion")
nm1=float(input("ingresa el primer numero: "))
nm2=float(input("ingresa el segundo numero: "))
multiplicacion=multi(nm1,nm2)
print(f"La resta de {nm1} * {nm2} es: {multiplicacion}")

print("\n Calculando division")
nd1=float(input("ingresa el primer numero: "))
nd2=float(input("ingresa el segundo numero: "))
division=div(nd1,nd2)
print(f"Ladivision de {nd1} / {nd2} es: {division}")

print("\n")