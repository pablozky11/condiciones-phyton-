nombreUsuario = input("Digita tu nombre: ")
edadUsuario = int(input("Digita tu edad: "))

if edadUsuario>=0 and edadUsuario <= 15:
    print(f"Querido {nombreUsuario}, usted es niño")
elif edadUsuario >15 and edadUsuario <= 28:
    print ( f'Querido {nombreUsuario}, usted es adolecente')
elif edadUsuario >28 and edadUsuario <= 60:
    print (f"Querido {nombreUsuario}, usted es un adulto")
elif edadUsuario > 60 and edadUsuario <=110:
    print (f"Querido {nombreUsuario}, usted es un suggar")
else: 
    print ("Si existes???????")
