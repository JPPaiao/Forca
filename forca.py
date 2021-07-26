import random

board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

def abrir():
    a = []
    arq = open("C:\\Users\\USUARIO\\Documents\\MeuRep\\vspy\\game\\Forca\\palavras.txt","r")
    for p in arq:
        a.append(p)
    palavra = random.choice(a)
    return palavra
    arq.close()

class Forca():
    con = 0
    o = 0

    def __init__(self, palavra):
        print(board[0])
        self.chave = palavra
        self.certa = []
        self.errada = []
        self.ok = False


    def letras(self):
        while True:
            print('=='*15)
            letra = str(input('Digite uma letra: '))
            if letra in self.chave:
                self.certa.append(letra)
                self.status()
            else:
                self.con += 1
                if self.con == len(board)-1:
                    
                    print(board[self.con])
                    self.perdeu()
                    break
                self.errada.append(letra)
                print(board[self.con])
                self.status()
            if self.ok == True:
                break
            print()

    def status(self):
        i = []
        for l in range(1, len(self.chave)):
                i.append('_')
        if 0 == self.o:
            print(f'Palavras:', end=' ')
            print(*i)
            self.o += 1
        elif self.o > 0:
            for num, letra in enumerate(self.chave):
                self.chave.split()
                if letra in self.certa:
                    i.insert(num, letra)
                    i.pop(-1)
            print('Palavra: ', end='')
            print(*i)
        print(f'Letras certas: ')
        for i in self.certa:
            print(i, end=' ')
        print()
        print(f'Letras erradas: ') 
        for i in self.errada:
            print(i, end=' ')
        self.ganhou(i)

    def perdeu(self):
        print('Game Over!!!')
        print('Você perdeu, a palavra certa era ' + self.chave)

    def ganhou(self, *x):
        ver = []
        for num, letra in enumerate(self.chave):
                self.chave.split()
                if letra in self.certa:
                    ver.append(letra)
        cont = len(ver) + 1
        v = len(self.chave)
        if cont == v:
            self.ok = True
            print()
            print(board[self.con])
            print('Win!!!')
            print('Parabéns, você ganhou')


def game():
    forca = Forca(abrir())
    forca.status()
    forca.letras()


game()