# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# TABULEIRO DE JOGO DA FORCA
tabuleiro = ['''

>>>>>>>>>>Jogo da Forca<<<<<<<<<<

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


# Classe
class Jogo_da_Forca:

	# Método que inicia o jogo da forca:
	def __init__(self, palavra):
		self.palavra = palavra
		self.letras_erradas = []
		self.guessed_letras = []
		
	# Método para adicionar/adivinhar/errar a letra:
	def guess(self, letra):
		if letra in self.palavra and letra not in self.guessed_letras:
			self.guessed_letras.append(letra)
		elif letra not in self.palavra and letra not in self.guessed_letras:
			self.guessed_letras.append(letra)
		else:
			return False
		return True

	# Método para verificar se o jogo terminou
	def Jogo_da_Forca_over(self):
		return self.Jogo_da_Forca_won() or (len(self.letras_erradas) == 6)
		
	# Método para verificar se o jogador venceu
	def Jogo_da_Forca_won(self):
		if '__' not in self.hide_palavra():
			return True
		return False

	# Método para não mostrar a letra no board
	def hide_palavra(self):
		adv = ''
		for letra in self.palavra:
			if letra not in self.guessed_letras:
				adv += '_'
			else:
				adv += letra
		return adv
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print (tabuleiro[len(self.guessed_letras)])
		print ('\nPalavra:' + self.hide_palavra())
		print ('\nErros: ',)
		for letra in self.letras_erradas:
			print (letra,)
		print ()
		print ('Acertos:',)
		for letra in self.guessed_letras:
			print (letra,)
		print ()

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Jogo_da_Forca(rand_palavra())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.Jogo_da_Forca_over():
		game.print_game_status()
		user_input = input ('\n Digite uma letra:')
		game.guess (user_input)

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.Jogo_da_Forca_won():
		print ('\nParabéns! Você venceu!!')
		print('A palavra era ' + game.palavra)
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.palavra)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
