#DJRoscowski
print('Projeto: Calculadora')

while True:
    n1 = float(input('Digite um número: '))
    calc = input('Qual operador deseja usar? ( +, -, * ou / ): ')
    n2 = float(input('Digite outro número: '))
    if calc == '+':
        resp = n1 + n2
        print('{} + {} = {}'.format(n1, n2, resp))
    elif calc == '-':
        resp = n1 - n2
        print('{} - {} = {}'.format(n1, n2, resp))
    elif calc == '*':
        resp = n1 * n2
        print('{} * {} = {}'.format(n1, n2, resp))
    elif calc == '/':
        resp = n1 / n2
        print('{} / {} = {}'.format(n1, n2, resp))
    elif calc != '+' or '-' or '*' or '/':
        print('Operador inválido. Tente novamente!')
        continue