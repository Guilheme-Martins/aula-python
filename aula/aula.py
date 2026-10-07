# nome = 'Guilherme'
# idade = 14
# cidade = 'maringa'
# estado = 'parana'

# print(f'meu nome é {nome}, tenho {idade} de idade, moro em {cidade} no estado do {estado}')

# n1 = int(input('digite o primeiro numero: '))
# n2 = int(input('digite o primeiro numero: '))
# soma = n1 + n2
# print(soma)

# nome = input('qual seu nome:  ')
# curso = input('qual se curso:  ')

# print(f"ola meu nome é {nome} e faço o curso {curso}")

# n1 = int(input("me de um numero: "))
# n2 = int(input("me de um numero: "))
# soma = n1 + n2
# sub= n1 - n2
# div= n1 / n2
# rest= n1 % n2
# expon= n1 ** n2
# inte = n1 // n2
# print(f"a soma é: {soma}")
# print(f"a subtraçao é: {sub}")
# print(f"a divisao é: {div}")
# print(f"a o resto da divisao é: {rest}")
# print(f"a exponiensiaçao é: {expon}")
# print(f"a a divisao inteira é: {inte}")
# numeroSecreto = 10
# tentativas = 10
# while tentativas:     
#     chute = int(input("tente acertar um numero de 1 a 10: "))

#     if chute == numeroSecreto:
#         print("voce acertou")
#         break
#     elif chute < numeroSecreto:
#         print("errou, o numero e maior")
#         tentativas -= 1
#     elif chute > numeroSecreto:
#         print("errou, numero é menor")
#         tentativas -= 1
#     else :
#         print(f"suas tentativas acabaram o numero era: {numeroSecreto}") 
        
# numeroSecreto = 10
# while True:     
#     chute = int(input("tente acertar um numero de 1 a 10: "))

#     if chute == numeroSecreto:
#         print("voce acertou")

import random
nome = input("qual seu nome: ")
quem = ['meu cachorro', 'meu primo','o wifi','o professor de matematiaca','meu gato']
acao = ['comeu','apagou','escondeu','hackeou','derrubou cafe']
alvo = ['meu caderno', 'meu notebook', 'minha tarefa', 'meu pen drive']

sorteio_quem = random.choice(quem)
sorteio_acao = random.choice(acao)
sorteio_alvo = random.choice(alvo)
print(f"professor, desculpa!{sorteio_quem.capitalize()} {sorteio_acao} {sorteio_alvo}")
print(f"aassinado: {nome}")