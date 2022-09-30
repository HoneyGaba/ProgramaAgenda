import os
from time import sleep
print('\n'*2000)
os.system('cls')

import Interface.Interface as it
import Funcionalidade.Funcionalidade as fu


it.titulo('AGENDA', 'vermelho')

while True:   
    while True:    
        escolha = it.menu()
        if it.verificaEscolha(escolha):
            #os.system('cls')
            break
    if escolha.lower() == 'exit':
        break
    elif escolha == '1':
        it.titulo(f'OPÇAO {escolha} = Criando novo contato...')
        fu.novoContato()
    elif escolha == '2':
        it.titulo(f'OPÇAO {escolha} = Vizualizando agenda...')
        fu.verAgenda()
    elif escolha == '3':
        it.titulo(f'OPÇAO {escolha} = Limpando agenda...')
        fu.limpaAgenda()
    





it.titulo('******    ATÉ MAIS, OBRIGADO!!!    ******',  'azul')


print()
print('~'*50)
