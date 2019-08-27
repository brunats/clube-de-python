## Lista exercicios loops e operadores
##  Exercicio 1
#       Faça um Programa que pergunte em que turno você estuda.
#       Peça para digitar M-Matutino, V-Vespertino ou N-Noturno.
#       Imprima a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!" ou "Valor Inválido!", conforme o caso.
## ->
pergunta_do_turno = 'Por favor informe o turno em que estuda:' + \
                    '\n\tM - Matutino' + \
                    '\n\tV - Vespertino' + \
                    '\n\tN - Noturno' + \
                    '\nTurno: '
turno_digitado = input(pergunta_do_turno)
if(turno_digitado == 'M'):
    print('Bom dia!')
elif(turno_digitado == 'V'):
    print('Boa tarde!')
elif(turno_digitado is 'N'):
    print('Boa noite!')
else:
    print('Valor inválido!')
## <-

##  Exercicio 2
#       Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
## ->
for numero in range(1, 21):
    print(numero)
## <-
##  Exercicio 3
#       Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#       O usuário deve informar de qual número ele deseja ver a tabuada.
## ->
resposta = input('Qual o numero que gostaria de gerar a tabuada?\t: ')
numero_requisitado = int(resposta)
print('Tabuada de ', numero_requisitado, ':')
for numero in range(1, 11):
    print('\t', numero_requisitado, 'x', numero, ' = ', numero_requisitado*numero)
## <-
