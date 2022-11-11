print('-' * 25)
print('- SEQUÊNCIA FIBONACCI - ')
print('-' * 25)
termo = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('.'*25)
print(f'\033[31m{t1} -> {t2} ', end='')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(f'\033[31m-> {t3} ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('\033[36m-> FIM!!!')
