'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
 em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
 Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Digite o número da CTPS ou 0 se não tem:  '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

print('\033[36m*-' * 20)
for k, v in dados.items():
    print(f' -  {k} tem o valor {v}. ')
print('*-' * 20)
