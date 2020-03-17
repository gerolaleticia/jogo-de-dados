from random import randint
from time import sleep
from operator import itemgetter
jogadas = {}
ranking = []
jogadas['jogador1'] = randint(1,6)
jogadas['jogador2'] = randint(1,6)
jogadas['jogador3'] = randint(1,6)
jogadas['jogador4'] = randint(1,6)
print('Valores sorteados: ')
sleep(1)
for k, v in jogadas.items():
    sleep(1)
    print(f'O {k} tirou o número {v} no dado')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True) #para colocar na ordem é preciso importar itemgetter
print('-='*30)
print('RANKING GERAL')
print('-='*30)
for c, v in enumerate(ranking):
    print(f'{c+1}o lugar: {v[0]} com {v[1]} pontos')
    sleep(1)