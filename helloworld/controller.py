'''No início do seu script, configure o ambiente Django. 
Certifique-se de importar as configurações corretas para
que você possa acessar os modelos e funcionalidades do Django.
 Adicione o seguinte código no início do seu script:'''


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloworld.settings")
import django
django.setup()



from helloworld.models import Funcionario
from time import sleep

#função que cadastra um novo funcionário
def cadastro ():
    funcionario = Funcionario(
        nome = str(input('Nome: ')),
        sobrenome = str(input('Sobrenome: ')),
        cpf = str(input('CPF: ')),
        tempo_de_servico = int(input('Tempo de serviço(h): ')),
        remuneracao = float(input('Remuneração: R$'))
    )

    funcionario.save()

def procurar():
    while True:
        print('Deseja procurar por: ')
        print('[1] - ID')
        print('[2] - Nome')
        print('[3] - Sobrenome')
        print('[4] - CPF')
        print('[5] - Tempo de serviço')
        print('[6] - Remuneração')
        print('[0] - Sair')

        op = int(input('Sua opção: '))
        if op == 0:
            print('Saindo...')
            sleep(1)
            break
        if op == 1:
            ID_dado = int(input('Digite o ID (somente números): '))
            funcionarios = Funcionario.objetos.filter(id=ID_dado).all()
            break
        if op == 2:
            nome_dado = str(input('Digite o nome: '))
            funcionarios = Funcionario.objetos.filter(nome=nome_dado).all()
            break
        if op == 3:
            sobrenome_dado = str(input('Digite o sobrenome: '))
            funcionarios = Funcionario.objetos.filter(sobrenome=sobrenome_dado).all()
            break
        if op == 4:
            cpf_dado = str(input('Digite o CPF: '))
            funcionarios = Funcionario.objetos.filter(cpf=cpf_dado).all()
            break
        if op == 5:
            tempo_dado = int(input('Digite o tempo de serviço (somente números): '))
            funcionarios = Funcionario.objetos.filter(tempo_de_servico=tempo_dado).all()
            break
        if op == 6:
            remuneracao_dado = float(input('Digite a remuneração (somente números e "."): '))
            funcionarios = Funcionario.objetos.filter(remuneracao= remuneracao_dado).all()
            break
        
    return funcionarios



def excluir(lista):
    
    for funcionario in lista:
        funcionario.delete()



#lista_funcionarios = Funcionario.objetos.filter(nome="Vanessa").exclude(id=2).all()
#excluir(lista_funcionarios)

#função para editar algum campo do funcionario
def editar(funcionario):
    while True:
        print('O que deseja alterar: ')
        print('[1] - ID')
        print('[2] - Nome')
        print('[3] - Sobrenome')
        print('[4] - CPF')
        print('[5] - Tempo de serviço')
        print('[6] - Remuneração')
        print('[0] - Sair')

        op = int(input('Sua opção: '))
        if op == 0:
            print('Saindo...')
            sleep(1)
            break
        if op == 1:
            ID_dado = int(input('Digite o novo ID (somente números): '))
            funcionario.id = ID_dado
            

        if op == 2:
            nome_dado = str(input('Digite o novo nome: '))
            funcionario.nome = nome_dado
            

        if op == 3:
            sobrenome_dado = str(input('Digite o novo sobrenome: '))
            funcionario.sobrenome = sobrenome_dado
        if op == 4:
            cpf_dado = str(input('Digite o novo CPF: '))
            funcionario.cpf = cpf_dado

        if op == 5:
            tempo_dado = int(input('Digite o novo tempo de serviço (somente números): '))
            funcionario.tempo_de_servico = tempo_dado

        if op == 6:
            remuneracao_dado = float(input('Digite a nova remuneração (somente números e "."): '))
            funcionario.remuneracao = remuneracao_dado

        print('Deseja alterar mais alguma coisa?')
    funcionario.save()
    

def mostrar(lista):
    for funcionario in lista:
        print(f'\n[Id: {funcionario.id}, Nome: {funcionario.nome + " " + funcionario.sobrenome}, CPF: {funcionario.cpf}, Tempo de Serviço: {funcionario.tempo_de_servico}, Remuneração: {funcionario.remuneracao}]\n')

#Menu#
op = 0
while True:
    print('[1] - Cadastrar Usuário')
    print('[2] - Excluir Usuário')
    print('[3] - Procurar Usuário')
    print('[4] - Alterar dado do funcionario')
    print('[0] - Sair')
    op = int(input('Sua opção: '))
    if op == 0:
        print('Saindo...')
        sleep(1)
        break
    if op == 1:
        cadastro()
        print('Funcionário adicionado com sucesso!')
    elif op == 2:
        lista_funcionarios = procurar()
        excluir(lista_funcionarios)
        print('Funcionário exluido com sucesso!')
    elif op == 3:
        funcio = procurar()
        mostrar(funcio)
    elif op == 4:
        funcio = procurar().first()
        editar(funcio)
    else:
        print('Opção inválida! Digite novamente.')
    