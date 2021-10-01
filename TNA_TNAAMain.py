# Este es un programa que nos permite obtener una TE "tasa efectiva" dada una TNA / TNAA
# a un tiempo determinado x. 
#Año = 365 días.

#ACLARACIÓN: Este es mi segundo codigo. Voy a utiliar muchos loops con el objetivo
#de que si el usuario se equivoca, pueda volver a tipear sin tener que abrir todo el
#programa nuevamente. 
#Al ser mi segundo codigo, tambien se veran muchos comentarios.

#El codigo se dividirá en 3 secciones:
    #PRIMERA SECCIÓN --> Input
    #SEGUNDA SECCIÓN --> Calculo
    #TERCERA SECCIÓN --> Pasaje entre tasas efectivas 
#--------------------------------------------------------------------------------

#PRIMER SECCIÓN: Input de la información por parte del usuario. 

y = 0 # Uso y como un flag
while (y == 0):
    tasa = float(input('Ingrese su TNA / TNAA en %: '))
    if tasa >= 0 and tasa <= 100:
        id = input('Es una TNA o una TNAA? [TNA], [TNAA]: ').upper() #id = identificación de tasa (TNA o TNAA)
        if id == 'TNA' or id == 'TNAA':
            y = 1
        else:
           print("Error, debe de indicar alguna de las tasas. Intente nuevamente.\n")
    continue
y = 0
while y == 0:
    choice = input('¿Quiere ingresar un lapso de tiempo ya establecido? Si [S], no [N]: ').upper() #Se le da la opcion al usuario entre usar lapsos comunes
    if choice == 'S':                                                                                  #o ingresar un tiempo personalizable.
        tiempo = int(input('¿De que plazo es su tasa? [30], [90], [180], [365]?: ')) 
        y = 1
    elif choice == 'N':
        tiempo = int(input('Ingrese su tipo de tasa personalizada: '))
        y = 1
    else:
        print("Error de tipeo. Vuelva a intentarlo\n")
        continue
y = 0
while y == 0:
    check = input(f'Su {id} es de {tasa}% a {tiempo} días ¿Es correcto? Si [S], no [N]: ' ).upper() #Checking point.
    if check == 'S':
        y = 1   
    elif check == 'N':
        print("Vuelva a iniciar el programa.")
        quit = input('¿Desea cerrar el programa? Presione [Q]: ').upper()
        if quit == 'Q': 
            y = 1
            exit()
    else:
        print('Error de tipeo. Vuelva a elegir la opción.\n')
        continue
#--------------------------------------------------------------------------------

#SEGUNDA SECCIÓN: Calculo de la tasa efectiva a partir de la información dada.
#Nota: Hay dos tipos de tasa:
# La tasa vencida efectiva ligada al TNA  (i) -- Usaremos esta variable
# La tasa efectiva de descuento ligada a TNAA (d)
# Ambas se calculan igual con respecto a la TNA y la TNAA

tasa = tasa/100     # Pasamos el valor de la tasa en porcentaje a valor decimal
i = (tasa*tiempo)/365 # te = tasas efectiva en el tiempo estipulado || 
i = (i*100)
i = round(i,4)

print(f'\nSu tasa efectiva es de {i}%:\n')

y = 0
while y == 0:
    choice = input('¿Desea hacer un pasaje entre tasas efectivas? si [S], no [N]: ').upper()
    if choice == 'N':
        print("Gracias por usar este programa!")
        input('Si desea salir presione cualquier tecla.')
        exit() 
    elif choice != 'S':
        print('Error de tipeo. Vuelva a elegir la opción\n')
        continue
    else:
        y = 1
#--------------------------------------------------------------------------------

#TERCERA SECCIÓN: Pasaje entre tasas efectivas. 
#Regla memotecnica del "Quiero sobre tengo". Por ende, las nuevas variables seran Q (quiero) y T(tengo).

y = 0
while y == 0:
    choice = input('Desea ingresar un lapso de tiempo ya establecido? Si [S], no [N]: ').upper()
    if choice == 'S':
        z = 0
        while z == 0:        # Se crea un segundo loop en caso de que el usuario quira calcular la misma tasa.
            Q = int(input('¿De que plazo desea su tasa? [30], [90], [180], [365]?: '))
            if Q == tiempo:
                print('\nUsted ya acaba de calcular esta tasa. Vuelva a ingresar otro plazo\n')
                continue
            else:
                y = 1 
                z = 1 
    elif choice == 'N':
        y = 1
        z = 0
        while z == 0:
            Q = int(input('Ingrese el nuevo lapso de tiempo al que quiere calcular la tasa efectiva: '))
            if Q == tiempo:
                print('\nUsted ya acaba de calcular esta tasa. Vuelva a ingresar otro plazo\n')
                continue
            else:
                z = 1
                y = 1
    else:
        print('\nErro de tipeo. Vuelva a intetarlo.\n')
        continue

i = i/100
i = round(i,4) 
T = tiempo
nueva_tasa =  (1+i)**((Q/T))-1
nueva_tasa = round(nueva_tasa*100,4)
print(f'\nSu nueva tasa efectiva a {Q} días es de {nueva_tasa}%\n')

print('Muchas gracias por usar el programa. Espero que le haya sido util!\n'
    '\nSaludos:'
    '\nAndrea!\n')
y = 0
while y == 0:
    exit = input('Para salir del programa presione [Q]: ').upper()
    if exit == 'Q':
        exit()
    else:
        continue

