from tabnanny import check
from art import logo
from random import randint
#import a logo do arquivo art e o metodo para gerar um inteiro aleatorio da biblioteca random

#funcao que checa a distancia entre o numero alvo e a tentativa
def checkNumber(target,guess):
    #recebe dois parametros, o alvo e a tentativa
    if guess > target:
        print("Too high")
        return False
    if guess < target:
        print("Too low")
        return False
    #compara os numeros, caso nao sejam os mesmos, retorna falso e mostra se esta acima ou abaixo
    else:
        #informa que o usuario acertou
        print("You got it! That's the correct number")
        return True        
      
#variavel flag para controlar as repeticoes do jogo
gameIsOn = True

#variavel que guarda o numero de tentativas
attempts = 0

#enquanto gameIsOn for igual a verdadeiro, o jogo vai continuar rodando
print(logo)

while gameIsOn:
    print("I'm thinking about a number between 1 and 100")
    
    #variavel que recebe um numero aleatorio entre 1 e 100
    targetNumber = randint(1,100)

    #variavel flag para controlar dificuldade
    difficulty = str(input("Type 'hard' or 'easy' to define your gameplay difficulty. "))
    
    #transforma para minusculo para tratamento de excecoes
    difficulty = difficulty.lower()

    #condicao para setar o numero de tentativas de acordo com a dificuldade
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    #loop que vai agir enquanto sobrarem tentativas
    while attempts != 0:
        print(f"Attempts left: {attempts}")
        #pede para o usuario entrar com uma tentativa
        guess = int(input("Enter with a number: "))
        #chama a funcao para checar a distancia da tentativa para o numero alvo e armazena o return dela
        guessStatus = checkNumber(targetNumber,guess)

        if guessStatus == False:
            attempts -= 1
        elif attempts:
            restart = input("Do you want to play again?? (Y/N) ")
            restart = restart.lower()
            if restart == 'n':
                gameIsOn = False
            

    if attempts==0:
        print(f"The number was {targetNumber}")
        restart = input("Do you want to play again?? (Y/N) ")
        restart = restart.lower()
        if restart == 'n':
            gameIsOn = False    





    


