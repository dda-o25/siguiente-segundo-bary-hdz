"""
Bruce de Bary Hernández Robles
12 de septiembre de 2025

Calcular la hora correspondiente al siguiente segundo 
El programa recibirá 
tres números enteros que representan, respectivamente, las horas, minutos y 
segundos correspondientes a un momento dado y deberá calcular los números que 
representan las horas, minutos y segundos correspondientes a la hora que sería 
después de haber transcurrido un segundo después de la hora proporcionada como 
entrada. La hora se representa en formato de 24 horas y la entrada corresponde 
a una hora válida.
"""

# Declaraciones
max_hora = 24
max_minutos = 60
max_segundos = 60

# Entradas
print("Hora inicial: ")
hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
segundo = int(input("Segundo: "))

# Proceso
if hora < max_hora and minuto < max_minutos and segundo < max_segundos:
    segundo = segundo + 1
    if segundo == 60:
        segundo = 0
        minuto = minuto +1
        if minuto == 60:
            minuto = 0
            hora = hora +1
            if hora == 24:
                hora = 0

    # Salidas
    print("Hora final: ")
    print("Hora:", hora)
    print("Minuto:", minuto)
    print("Segundo:", segundo)

else:
    #Salidas
    print("Ingrese valores validos")