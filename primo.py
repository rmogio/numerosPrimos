x = int(input('Digite um numero maior que 1: '))

div = 2
result = 0
primo = True


if (x == 2):
    print('É primo')

if x > 2:
    while (div < x):
        result = x % div
        if result == 0:
            primo = False
            break
        div += 1

    if primo:
        print('É primo')
    elif not primo:
        print('Não é primo')
