class AhorcadoController(object):
    palabra = ""
    array_adivinar = []
    array_juego = []
    max_intentos = 6
    array_letras_usadas = []
    letra_introducida = ""
    game_over = 0
    turno = 0
    error_visual = ["", " O", " O\n |", " O\n-|", " O\n-|-", " O\n-|-\n /", " O\n-|-\n /\\"]

    #Mostramos el inicio del juego
    def start(self):
        print("Bienvenido al ahorcado! \n")

    #Pedimos una palabra para poder jugar
    def pedir_palabra(self):
        self.palabra = input("introduce una palabra: \n")
    
    #Asignamos algunas variables relacionadas con la palabra
    def procesar_palabra(self):
        self.array_adivinar = list(self.palabra)
        self.array_juego = ["-"] * len(self.palabra)

    #Pedimos la letra que se quiere jugar
    def pedir_letra(self):
        self.letra_introducida = input("introduce una letra \n")

    #Miramos en que posicion esta el caracter, si esta claro
    def encontrar_letra(self):
        contador = 0
        array_posiciones = []
        for caracter in self.array_adivinar:
            if self.letra_introducida == caracter:
                array_posiciones.append(contador)
            contador += 1
        return array_posiciones

    #Desvelamos la posicion de la letra
    def poner_letra(self, array_posiciones):
        for posicion in array_posiciones:
            self.array_juego[posicion] = self.letra_introducida
            self.array_letras_usadas.append(self.letra_introducida)

    #Buscamos si hay guinoes en la palabra, si no hay es que todo esta solucionado
    def comprobar_palabra_completa(self):
        return "-" in self.array_juego
    
    #Comprobamos que la palabra sea un string (Creo que adminte 2 numeros juntos, pero bueno)
    def comprobar_palabra(self):
        return self.palabra.isalpha()

    #Comprobamos si se ha introducido 1 caracter solo, si es un string y si no se ha usado anteriormente
    def comprobar_letra(self):
        continuar = -1
        if len(self.letra_introducida) == 1:
            if self.letra_introducida.isalpha():
                if self.letra_introducida not in self.array_letras_usadas:
                    continuar = 0
                else:
                    continuar = -2
        else:
            continuar = -3
        return continuar
    
    #Mostramos como va la partida actualmente
    def mostrar_palabra_actual(self):
        print(''.join(self.array_juego));

    #Mostramos por pantalla los prints de errores y game over
    def ha_fallado(self):
        self.turno += 1
        if (self.turno >= self.max_intentos):
            game.game_over = 1
            print(self.error_visual[self.turno])
            print("######## GAME OVER!! ########")

        else:
            print("######## HAS FALLADO ########")
            print(''.join(self.error_visual[self.turno]))


######################################################
# #Inicializacion del juego
game= AhorcadoController()
game.start()
palabra_correcta = 0
game.pedir_palabra()

#Pedimos una palabra, si no es corraecta la pedimos hasta que cunda
while palabra_correcta != 1:
    if game.comprobar_palabra():
        palabra_correcta = 1
    else:
        print("######## ERROR!! solo letras! ########")
        game.pedir_palabra()

#Si es correcta la procesamos
game.procesar_palabra()

while game.game_over != 1:
    #mostramos como va la palabra
    game.mostrar_palabra_actual()

    game.pedir_letra()
    error_letra = game.comprobar_letra()
    #miramos si la letra esta mal y la pedimos tantas veces haga falta
    while error_letra < 0:
        if error_letra == -1:
            print("######## ERROR!! solo letras! ########")
        elif error_letra == -2:
            print("######## Esa letra ya la has usado! Cambia!! ########")
        game.pedir_letra()
        error_letra = game.comprobar_letra()

    #Miramos si la letra no esta o esta en la palabra
    if not game.encontrar_letra():
        game.ha_fallado()
    else:
        game.poner_letra(game.encontrar_letra())
    
    #Miramos si la palabra esta completa
    if not game.comprobar_palabra_completa():
        print("######## Has ganado!! la palabra era: ########")
        game.game_over = 1
#Al llegar aqui mostramos que palabra era
print(game.palabra)
