from random import randint
from time import sleep


opcoes = ['Pedra', 'Papel', 'Tesoura']
n = int(input('Suas opções: \n[1] - Pedra\n[2] - Papel\n[3] - Tesoura\nQual é a sua jogada? ')) - 1
print(f'\nVocê escolheu \"{opcoes[n]}\".\n')
sleep(2)
n1 = randint(1, 3) - 1
print(f'O computador escolheu \"{opcoes[n1]}\".\n')
sleep(2)
if n == n1:
    print(f'O jogo empatou, ambos os jogadores escolheram \"{opcoes[n]}\".')
elif (n == 0 and n1 == 1) or (n == 1 and n1 == 2) or (n == 2 and n1 == 0):
    print(f'\033[1;30;41mVocê perdeu!\033[m \"{opcoes[n1]}\" ganha de \"{opcoes[n]}\".')
else:
    print(f'\033[1;30;42mVocê ganhou!\033[m \"{opcoes[n]}\" ganha de \"{opcoes[n1]}\".')
