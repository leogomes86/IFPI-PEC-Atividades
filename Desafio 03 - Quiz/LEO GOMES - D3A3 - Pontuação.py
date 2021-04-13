score = 0
#Question 01
print('em que ano o plano real foi posto em prática no brasil?')
r = input()

if r == '1994':
    print('parabéns! você acertou!')
    score = score + 1
else:
    print('que pena... você errou a resposta!')

#Question 02
print('qual foi a frase mais famosa proferida por Darth Vader em "O Império Contra-Ataca"?')
r = input().lower()

if r == 'luke, eu sou seu pai':
    print('parabéns! resposta correta!')
    score = score + 1
else:
    print('resposta errada!')

#Questão 03
print('quanto é 385 vezes 548?')
r = input()

if r == '210980':
    print('resposta correta! parabéns!')
    score = score + 1
else:
    print('que pena... sua resposta está errada!')

print(f'total de pontos:{score}')
