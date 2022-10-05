from time import sleep


def escreveArquivo(texto):
    try:            
        with open('Agenda.txt', 'a') as arquivo:
            arquivo.write(texto)
    except:
        print('a escrita deu errado!')


def lerArquivo():
    try:
        with open('Agenda.txt', 'r') as arquivo:
            print(arquivo.read())
    except:
        print('Algo de errado na leitura...')


def mensagemErro(msg):
    from Interface.Interface import cor
    cor('vermelho')
    print(msg)
    cor('padrao')                
                


def conferePadrao(frase, intervalo):
    while True:
        dado = input(frase)
        if dado in intervalo and dado != '' and len(dado) == 1:
            return dado
        else:    
            mensagemErro('Informação errada\nTente novamente!')


def confereNumero(frase):
    while True:
        try:
            dado = int(input(frase))
        except:
            mensagemErro('Dado passado não é um número \nTente novamente!')
        else:
            dado = str(dado)
            return dado


def novoContato():
    sleep(0.5)
    print('Criando novo contato...')
    infoContato = ['nome', 'idade', 'sexo']
    for i in infoContato:
        if i == 'idade':
            var = confereNumero(f'Digite {i} do contato: ')
        elif i == 'sexo':
            var = conferePadrao(f'Digite o sexo\n[M] Masculino [F] Feminino\n{i}: ',
             'mfMF').upper()
        else:
            var = input(f'Digite {i} do contato: ')
            var = var.replace(';', '')
        escreveArquivo(var + ';')
    escreveArquivo('\n')  


def verAgenda():
    sleep(0.5)
    print('Vizualizando agenda...')
    lerArquivo()


def limpaAgenda():
    sleep(0.5)
    print('Limpando agenda...')


