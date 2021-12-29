import random

def generar_matriz_oculta(tamano: int) -> list:
    '''
    Pre: Recibe un tamaño.
    Post: retorna una matriz del tamaño dado con las cartas dadas vuelta.
    '''
    matriz_oculta = []
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            fila.append("*")
        matriz_oculta.append(fila)
 
    return matriz_oculta

def generar_matriz(tamano_matriz: int) -> list:
    '''
    Pre: Recibe un tamaño.
    Post: Genera una matriz del tamaño dado compuesta de pares de numeros iguales y organizado aleatoriamente.
    '''
    matriz_tablero = []
    acumulador = 1
    aumentar=0
    tamano = 0
    if tamano_matriz == 4:
        tamano = 4 
    elif tamano_matriz == 8:
        tamano = 8
    else:
        tamano = 12
    
    for i in range(tamano):
        fila = []
        for j in range(tamano):
            if aumentar == 2:
                acumulador+=1
                aumentar=0
            fila.append(acumulador)
            aumentar+=1
        aumentar=0    
        acumulador+=1
        matriz_tablero.append(fila)
    
    for i in range(tamano):
        for j in range(tamano):
            i_aleatorio = random.randint(0, tamano - 1)
            j_aleatorio = random.randint(0, tamano - 1)
            matriz_temporal= matriz_tablero[i][j]
            matriz_tablero[i][j] = matriz_tablero[i_aleatorio][j_aleatorio]
            matriz_tablero[i_aleatorio][j_aleatorio] = matriz_temporal
    
    return  matriz_tablero

def imprimir_matriz(matriz: list, tamano: int) -> None:
    '''
    Pre: Recibe una matriz y un tamaño.
    Post: Imprime la matriz recibida.
    '''
    for i in range(tamano):
        for j in range(tamano):
            print('|',matriz[i][j], end='|  ')
        print('')
        
def cartas(matriz: list,matriz_oculta: list,matriz_temporal: list, tamanio: int,carta: str) -> list:
    '''
    Pre: Recibe las matrices, tamaño y una carta.
    Post: Segun el nombre de la carta, este modifica las tres matrices y los devuelve en una lista
    '''
    lista_matriz=[]
    fila_revertida=[]
    matriz_re = []
    matriz_oculta_re = []
    matriz_temporal_re = []
    lista_matrices = []
    
    if carta == 'toti':
        numero = random.randint(0, 1)
        if numero == 0:
            for i in range(tamanio):
                fila_revertida = list(reversed(matriz[i]))
                matriz_re.append(fila_revertida)
                fila_revertida = []
                fila_revertida = list(reversed(matriz_oculta[i]))
                matriz_oculta_re.append(fila_revertida)
                fila_revertida = []
                fila_revertida = list(reversed(matriz_temporal[i]))
                matriz_temporal_re.append(fila_revertida)
            
            lista_matriz.append(matriz_re)
            lista_matriz.append(matriz_oculta_re)
            lista_matriz.append(matriz_temporal_re)
            
            return lista_matriz
        else:  
            fila=[]
            matriz_ver = []
            matriz_oculta_ver = []
            matriz_temporal_ver = []
            cont=0
            
            for i in range(tamanio):
                cont+=1
                fila = matriz[tamanio-cont]
                matriz_ver.append(fila)
                fila = []
                fila = matriz_oculta[tamanio-cont]
                matriz_oculta_ver.append(fila)
                fila = []
                fila = matriz_temporal[tamanio-cont]
                matriz_temporal_ver.append(fila)
                fila=[]
            
            lista_matriz.append(matriz_ver)
            lista_matriz.append(matriz_oculta_ver)
            lista_matriz.append(matriz_temporal_ver)
            
            return lista_matriz
        
    elif carta == 'fatality':    
        
        matriz_tras = []
        for i in range(len(matriz[0])):   
            matriz_tras.append([])
            for j in range(len(matriz)):
                matriz_tras[i].append(matriz[j][i])
        
        matriz_oculta_tras = []
        for i in range(len(matriz_oculta[0])):       
            matriz_oculta_tras.append([])
            for j in range(len(matriz)):               
                matriz_oculta_tras[i].append(matriz_oculta[j][i])           
        
        matriz_temporal_tras = []
        for i in range(len(matriz_temporal[0])):   
            matriz_temporal_tras.append([])  
            for j in range(len(matriz_temporal)):           
                matriz_temporal_tras[i].append(matriz_temporal[j][i])
        
        lista_matriz.append(matriz_tras)
        lista_matriz.append(matriz_oculta_tras)
        lista_matriz.append(matriz_temporal_tras)
        
        return lista_matriz
    
    elif carta == 'layout':
        
        for i in range(tamanio): 
            for j in range(tamanio):
                
                i_aleatorio = random.randint(0, tamanio - 1)
                j_aleatorio = random.randint (0, tamanio - 1)
                
                matriz_tempo1= matriz[i][j]
                matriz_tempo2= matriz_oculta[i][j]
                matriz_tempo3= matriz_temporal[i][j]
            
                matriz[i][j] = matriz[i_aleatorio][j_aleatorio]
                matriz[i_aleatorio][j_aleatorio] = matriz_tempo1
            
                matriz_oculta[i][j] = matriz_oculta[i_aleatorio][j_aleatorio]
                matriz_oculta[i_aleatorio][j_aleatorio] = matriz_tempo2
            
                matriz_temporal[i][j] = matriz_temporal[i_aleatorio][j_aleatorio]               
                matriz_temporal[i_aleatorio][j_aleatorio] = matriz_tempo3      
        
        lista_matriz.append(matriz)
        lista_matriz.append(matriz_oculta)
        lista_matriz.append(matriz_temporal)
        
        return lista_matriz
    
def tablero_juego(matriz: list, matriz_oculta: list,matriz_temporal: list,contador: int,jugador: int,tamanio: int) -> list:
    '''
    Pre: Recibe las variables para jugar.
    Post: Imprime un turno de juego y devuelve una lista con la cantidad de pares encontrados y el turno del siguiente jugador.
    '''
    fila1=0
    columna1=0
    turno=0
    imprimir_matriz(matriz_oculta,tamanio)
    turno_contador = []
        #Selecciona y muestra la matriz dos veces
    for i in range(2):
            #####
        fila1 = int(input ("Ingrese una fila: "))-1
        columna1 = int(input("Ingrese una columna: "))-1         
        if columna1 > tamanio or fila1 > tamanio :
            print('El numero ingresado no es valido. Ingrese de nuevo')
            while fila1 > tamanio or columna1 > tamanio:                
                fila1 = int(input ("Ingrese una fila: "))-1
                columna1 = int(input("Ingrese una columna: "))-1
                if fila1 > tamanio or columna1 > tamanio:
                    print('El numero ingresado no es valido. Ingrese de nuevo')
        if i == 0:
            matriz_oculta [fila1][columna1] = matriz [fila1][columna1]
            columna2 = columna1
            fila2 = fila1         
            imprimir_matriz(matriz_oculta,tamanio)
                  
        else:
                
            if columna1 != columna2 or fila1 != fila2:            
                matriz_oculta [fila1][columna1] = matriz [fila1][columna1]
                imprimir_matriz(matriz_oculta,tamanio)   
            ######
    if matriz_oculta[fila1][columna1] == matriz_oculta[fila2][columna2]:     
        print('Felicidades encontraste un par')
        for i in range(tamanio):
            for j in range(tamanio):
                matriz_temporal[i][j] = matriz_oculta[i][j]
        contador+=1
        if jugador == 1:
            turno = 1
        else:
            turno = 2
        turno_contador.append(contador)
        turno_contador.append(turno)
        return turno_contador
    else:
        print('Los numeros no coinciden, es turno del otro jugador')
        for i in range(tamanio):
            for j in range(tamanio):
                matriz_oculta[i][j] = matriz_temporal[i][j]
        if jugador == 1:
            turno = 2
        else:
            turno = 1
        turno_contador.append(contador)
        turno_contador.append(turno)
        return turno_contador
    
def jugar(nombre1:str, nombre2:str, tamanio: int, probabilidades: list) -> list:
    '''
    Pre: Recibe los nombres de los jugadores y el tamaño del tablero.
    Post: Usa la función tablero_juego hasta que uno de los jugadores gane,
    y tambien la funcion cartas para modificar el tablero del rival,
    y retorna el resultado de la partida.
    '''
    matriz = generar_matriz(tamanio)
    matriz_oculta = generar_matriz_oculta(tamanio)
    matriz_temporal =  generar_matriz_oculta(tamanio)
    lista_auxiliar = []
    contador=0
    turno=1
    jugador=0
    matriz2 = generar_matriz(tamanio)
    matriz_oculta2 = generar_matriz_oculta(tamanio)
    matriz_temporal2 =  generar_matriz_oculta(tamanio)
    lista_auxiliar2 = []
    contador2 = 0
    score = []
    resultado = 0
    resultado2 = 0
    cartarandom = ['replay','layout','toti','fatality']
    cartas1 = []
    cartas2 = []
    dado = 0
    carta_seleccionada = ''
    turno_carta1 = 0
    turno_carta2 = 0

    
    while contador < tamanio*2 and contador2 < tamanio*2 :
        
        if turno == 1:
            modificar_matriz = 0
            print('JUGADOR 1: ',nombre1)
            
            jugador = 1
            lista_auxiliar = tablero_juego(matriz,matriz_oculta,matriz_temporal,contador,jugador,tamanio)
            contador = lista_auxiliar[0]
            turno = lista_auxiliar[1]
            dado = random.randint(0, 1)
            if turno_carta1 == 0:
                if dado == 1:
                    carta_seleccionada = random.choice(cartarandom)
                    if probabilidades[cartarandom.index(carta_seleccionada)] >= random.random():
                        cartas1.append(carta_seleccionada)
                        print('TE HA TOCADO: ',carta_seleccionada)
                    else:
                        print('No toco carta')    
                else:
                    print('No toco carta')
            
            if len(cartas1) >= 1:
                
                cant_replay = cartas1.count('replay')
                cant_layout = cartas1.count('layout')
                cant_toti = cartas1.count('toti')
                cant_fatality = cartas1.count('fatality')
                print('Cartas disponibles:')
                print('Replay:',cant_replay,' Layout:',cant_layout,' Toti:',cant_toti,' Fatality:',cant_fatality)
                
                usar = int(input('Desea usar una carta?: [1]Si  [2]No\n'))
                if usar == 1:
                    print('Seleccione su carta:')
                    opcion=int(input('\n[1]Replay\n[2]Layout\n[3]Toti\n[4]Fatality\n'))-1
                    
                    while opcion < 0 or opcion > 3:
                        print('La carta seleccionada no existe. Intente de nuevo')
                        opcion=int(input('\n[1]Replay\n[2]Layout\n[3]Toti\n[4]Fatality\n'))-1
                    
                    if opcion == 0 and cartas1.count(cartarandom[opcion]) >= 1:
                        cartas1.remove(cartarandom[opcion])
                        turno = 1                       
                        print('Se ha usado la carta replay')
                        modificar_matriz=1
                    elif opcion == 1 and cartas1.count(cartarandom[opcion]) >= 1:
                        cartas1.remove(cartarandom[opcion])
                        lista_matriz = []                       
                        lista_matriz = cartas(matriz2,matriz_oculta2,matriz_temporal2,tamanio,cartarandom[opcion])
                        print('Se ha usado la carta layout')
                    elif opcion == 2 and cartas1.count(cartarandom[opcion]) >= 1:
                        cartas1.remove(cartarandom[opcion])
                        lista_matriz = []                       
                        lista_matriz = cartas(matriz2,matriz_oculta2,matriz_temporal2,tamanio,cartarandom[opcion])
                        print('Se ha usado la carta toti')
                    elif opcion == 3 and cartas1.count(cartarandom[opcion]) >= 1:
                        cartas1.remove(cartarandom[opcion])
                        lista_matriz = []                       
                        lista_matriz = cartas(matriz2,matriz_oculta2,matriz_temporal2,tamanio,cartarandom[opcion])
                        print('Se ha usado la carta fatality')
                    if modificar_matriz != 1:                                               
                        matriz2 = lista_matriz[0]                     
                        matriz_oculta2 = lista_matriz[1]
                        matriz_temporal2 = lista_matriz[2]
                        modificar_matriz=1
                
                turno_carta1 = 1 
                turno_carta2 = 0                      
            if contador == tamanio:
                resultado = 1
            
        if turno == 2:
            
            modificar_matriz = 0
            print('JUGADOR 2: ',nombre2)
            jugador = 2
            lista_auxiliar2 = tablero_juego(matriz2,matriz_oculta2,matriz_temporal2,contador2,jugador,tamanio)
            contador2 = lista_auxiliar2[0]
            turno = lista_auxiliar2[1]
            dado = random.randint(0, 1)
    
            if turno_carta2 == 0:
                if dado == 1:
                    carta_seleccionada = random.choice(cartarandom)
                    if probabilidades[cartarandom.index(carta_seleccionada)] >= random.random():
                        cartas2.append(carta_seleccionada)
                        print('TE HA TOCADO: ',carta_seleccionada)
                    else:
                        print('No toco carta')
                else:
                    print('No toco carta')
            if len(cartas2) >= 1:
                
                cant_replay = cartas2.count('replay')
                cant_layout = cartas2.count('layout')
                cant_toti = cartas2.count('toti')
                cant_fatality = cartas2.count('fatality')
                print('Cartas disponibles:')
                print('Replay:',cant_replay,' Layout:',cant_layout,' Toti:',cant_toti,' Fatality:',cant_fatality)
                usar=int(input('Desea usar una carta?: [1]Si  [2]No\n'))
                
                if usar == 1:
                    print('Seleccione su carta:')
                    opcion=int(input('\n[1]Replay\n[2]Layout\n[3]Toti\n[4]Fatality\n'))-1
                    
                    while opcion < 0 or opcion > 3:
                        print('La carta seleccionada no existe. Intente de nuevo')
                        opcion=int(input('\n [1]Replay\n[2]Layout\n[3]Toti\n[4]Fatality\n'))-1
                                   
                    if opcion == 0 and cartas2.count(cartarandom[opcion]) >= 1:
                        cartas2.remove(cartarandom[opcion])
                        turno = 2
                        print('Se ha usado la carta replay')
                        mod_matriz=1
                        turno_carta2 = 1
                    elif opcion == 1 and cartas2.count(cartarandom[opcion]) >= 1:
                        cartas2.remove(cartarandom[opcion])
                        lista_matriz = []                       
                        lista_matriz = cartas(matriz,matriz_oculta,matriz_temporal,tamanio,cartarandom[opcion])
                        print('Se ha usado la carta layout')
                    elif opcion == 2 and cartas2.count(cartarandom[opcion]) >= 1:
                        cartas2.remove(cartarandom[opcion])
                        lista_matriz = []                       
                        lista_matriz = cartas(matriz,matriz_oculta,matriz_temporal,tamanio,cartarandom[opcion])
                        print('Se ha usado la carta toti')
                    elif opcion == 3 and cartas2.count(cartarandom[opcion]) >= 1:
                        cartas2.remove(cartarandom[opcion])
                        lista_matriz = []                       
                        lista_matriz = cartas(matriz,matriz_oculta,matriz_temporal,tamanio,cartarandom[opcion])
                        print('Se ha usado la carta fatality')
                    if modificar_matriz != 1:
                        matriz = lista_matriz[0]
                        matriz_oculta = lista_matriz[1]
                        matriz_temporal = lista_matriz[2]            
                        modificar_matriz = 1
            
            turno_carta2 = 1
            turno_carta1 = 0            
            if contador2 == tamanio:
                resultado2 = 1
        
        if contador == tamanio*2 or contador2 == tamanio*2:
            
            score.append(resultado)
            score.append(resultado2)
            
            return score

def score(matriz: list,nombre1: str,nombre2: str) -> None:
    '''
    Pre:Recibe el resultado de las partidas, la cantidad de partidas y los nombres de los jugadores.
    Post: Imprime quien gano más en las últimas 4 partidas, y la cantidad de partidas jugadas.
    '''
    cantidad_de_partidas= len(matriz[0])
    acumulador_1=0
    acumulador_2=0
    
    if cantidad_de_partidas <= 4:
        for i in range(2):
            for j in range(cantidad_de_partidas):
                if i == 0:
                    acumulador_1 += matriz[i][j] 
                else:
                    acumulador_2 += matriz[i][j]
    else:
        ultimos_4_jugador_1 = []
        ultimos_4_jugador_2 = []
        ultimos_4_jugador_1 = list(matriz[0][-4:])
        ultimos_4_jugador_2 = list(matriz[1][-4:])

        for i in range(4):
            acumulador_1 += ultimos_4_jugador_1[i] 
            acumulador_2 += ultimos_4_jugador_2[i]
                    
    if acumulador_1  > acumulador_2:
        print('El jugador:',nombre1,' gano mas partidas en las ultimas 4 rondas, Partidas jugadas:',cantidad_de_partidas)
    elif acumulador_1 < acumulador_2:
        print('El jugador:',nombre2,' gano mas partidas en las ultimas 4 rondas, Partidas jugadas:',cantidad_de_partidas)
    else:
        print(nombre1,' y ',nombre2,' estan empatados, Partidas jugadas:',cantidad_de_partidas)

def parametros(option: int,tamanio: int, lista_probabilidades: list) -> list:
    '''
    Pre: Imprime los parametros que se pueden modificar por el usuario.
    Post: Llama a la función elegida que modifica la duración del juego o el porcentaje de probabilidad de cartas.
    '''
    if option == 1:
        print("Elija la duracion de la partida: Ingrese el numero según corresponda:")
        duracion = int(input("\n[4] duracion corta\n[8] duracion media \n[12] duracion larga\n "))
        duracion_l = []
        while duracion != 4 and duracion != 8 and duracion !=12 :
            print ("Ingreso un valor incorrecto, intentelo nuevamente")
            duracion = int(input("\n[4] duracion corta\n[8] duracion media \n[12] duracion larga\n "))
        duracion_l.append(duracion)
        return duracion_l
    else:
        salir = 0
        while salir != 1:
            print('Elija la carta que quiere modificar sus probabilidad')
            elegir = int(input('[1]Carta Replay\n[2]Carta Layout\n[3]Carta Toti\n[4]Carta Fatality\n[5]Salir\n'))
            if elegir == 1:
                probabilidad =int(input('Ingrese una probabilidad del 1 al 100 de la carta replay\n'))/100
                lista_probabilidades[elegir-1] = probabilidad
            elif elegir == 2:
                probabilidad =int(input('Ingrese una probabilidad del 1 al 100 de la carta layout\n'))/100
                lista_probabilidades[elegir-1] = probabilidad
            elif elegir == 3:
                probabilidad =int(input('Ingrese una probabilidad del 1 al 100 de la carta toti\n'))/100
                lista_probabilidades[elegir-1] = probabilidad
            elif elegir == 4:
                probabilidad =int(input('Ingrese una probabilidad del 1 al 100 de la carta fatality\n'))/100
                lista_probabilidades[elegir-1] = probabilidad
            elif elegir == 5:
                salir = 1
            else:
                print ("Ingreso un valor incorrecto, intentelo nuevamente")      
        return lista_probabilidades
def main() -> None:
    '''
    Pre: Imprime un menú con opciones para el usuario. 
    Post: Según las opciones elegidas llama a las funciones indicadas, y el programa finaliza cuando se elige la opción de salir
    '''
    matriz =[]
    opciones = 0
    salir = 0
    lista_aux=[]
    partidas=0
    tamanio = 4
    nombre1 = ''
    nombre2= ''
    lista_probabilidades = [0.99,0.99,0.99,0.99]
    
    while salir !=1:
        opciones=int(input('Bienvenido al Memotest, Ingrese:\n[1]Para jugar\n[2]Parametros\n[3]Mostrar score\n[4]Salir\n'))
        if opciones == 1:
            if partidas == 0:
                nombre1=input('Ingrese el nombre de jugador 1: ')
                nombre2=input('Ingrese el nombre de jugador 2: ')  
            lista_aux = jugar(nombre1,nombre2,tamanio,lista_probabilidades)
            print('JUEGO TERMINADO')
            partidas += 1
            if partidas == 1:
                for i in range(2):
                    fila = []
                    for j in range(1):
                        if i == 0:
                            fila.append(lista_aux[0])
                        else:
                            fila.append(lista_aux[1])
                    matriz.append(fila)        
            else:
                for i in range(2):
                    matriz[i].append(lista_aux[i])
        elif opciones == 2:
            option = int(input('Ingrese:\n[1] Modificar duracion\n[2] Modificar probabilidades de las cartas\n'))
            while option != 1 and option != 2:
                print('Ingreso un valor incorrecto, intentelo nuevamente')
                option = int(input('Ingrese:\n[1] Modificar duracion\n[2] Modificar probabilidades de las cartas\n'))
            if option == 1:
                tamanio = parametros(option,tamanio,lista_probabilidades)[0]
            else:
                lista_probabilidades = parametros(option,tamanio,lista_probabilidades)            
        elif opciones == 3:
            score(matriz,nombre1,nombre2)
        elif opciones == 4:
            salir = 1
              
main()  