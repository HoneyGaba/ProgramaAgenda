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


def conferePadrao(frase, intervalo):
    while True:
        dado = input(frase)
        if dado in intervalo and dado != '':
            return dado
        else:    
            from Interface.Interface import cor

            cor('vermelho')
            print('Informação incorreta, tente novamente...')
            cor('padrao')


def novoContato():
    sleep(0.5)
    print('Criando novo contato...')
    infoContato = ['nome', 'idade', 'sexo']
    for i in infoContato:
        if i == 'idade':
            var = conferePadrao(f'Digite {i} do contato: ', '1234567890')
        elif i == 'sexo':
            var = conferePadrao(f'Digite o sexo [M] Masculino [F] Feminino\n{i}: ',
             'mf').upper()
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


