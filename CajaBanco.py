Usuarios = {}

Usuarios["Milena"] = 400.00
Usuarios["Lenna"] = 200.00
Usuarios["Gustavo"] = 600.00

def registrar_usuario():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in Usuarios:
        print("Usuario registrado")
    else:
        Usuarios[nombre] = 0.00
    print(f"Usuario {nombre} agregado correctamente")
    

def depositar():
     nombre = input("Introduce el nombre del usuario: ")
     
     if nombre in Usuarios:
        monto = float(input("Introduce el monto a depositar: "))
        Usuarios[nombre] += monto
     else:
         print(f"Usuario {nombre} no existe")

def retirar():
    nombre = input("Ingrese el nombre del usuario: ")
    
    if nombre in Usuarios:
        retiro = float(input("Ingrese el monto de retiro: "))
        if retiro > Usuarios[nombre]:
            print("Valor insuficiente")
        else:
            Usuarios[nombre] -= retiro
    
    else:
        print("Usuario no existente en el sistema")
registrar_usuario()

print(Usuarios)

print(Usuarios)

# Usuarios = []
# Cuenta_bancaria = []
# Cuentas = []

# Usuario = {"nombre":"Milena", "estado": "A"}
# Usuarios.append(Usuario)

# Cuenta = {"nombre":"Milena" , "valor":400.00}
# Cuentas.append(Cuenta)

# def depositar():
#     nombre = input("Introduce el nombre del Usuario: ")
#     monto = float(input("Introduce el monto adepositar: "))
#     for Cuenta_guardada in Cuentas:
#         if(Cuenta_guardada["nombre"] == nombre):
#             Cuenta_guardada["valor"] += monto
    

# print(Cuentas)
# depositar()
# print(Cuentas)


    