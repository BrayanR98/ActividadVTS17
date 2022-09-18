""" cre menu 
1.saludar
2.Despedir
3.salir"""

cont=1
while(cont !=0):
    respuesta=int(input("Presione 1 para Saludar"))
    respuesta=int(input("Presione 2 para Despedirse"))
    respuesta=int(input("Presione 3 para Salir"))
    if(respuesta == 1):
      print("Hola")
    elif (respuesta == 2):
      print("Despedir")
    elif(respuesta == 3):
      break
else:
    print("Se acabo..")
