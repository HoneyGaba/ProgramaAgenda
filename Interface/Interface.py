from time import sleep

def cor(c):
    c = c.strip().lower()
    if c == 'vermelho':     esc = '31'
    elif c == 'azul':       esc = '34'
    elif c == 'amarelo':    esc = '33'
    elif c == 'cinza':      esc = '100'
    elif c == 'verde':      esc = '32'
    elif c == 'roza':       esc = '35'
    elif c == 'padrao':     esc = '0'
    else:                   esc = '0'
    print(f'\033[0;0;{esc}m')


def linha(tam=50):
    print('~'*tam)

def titulo(texto, coloraçao = 'padrao'):
    cor(coloraçao)
    linha()
    print(f'{texto:^50}')
    linha()
    cor('padrao')


def opçoes(*items):
    for i, v in enumerate(items):
        print(f'   {i+1} - {v}')
    print('exit - Para sair!!!')
    

def escolha():
    op = input('\nSua opção: ')
    return op


def menu():
    sleep(0.5)
    titulo('MENU', 'VERDE')
    opçoes('Novo contato', 'Vizualizar agenda', 'Limpar agenda')
    return escolha()

def verificaEscolha(esc):
    sleep(0.5)
    if esc.lower() == 'exit':
        return True
    elif esc in '1234' and esc != '':
        return True
    else:
        cor('vermelho')
        print('Escolha errada, tente novamente...')
        cor('padrao')
        sleep(1)
        return False
    


