print('='*60)
print('CÁLCULO DE ÁREAS'.center(60))
print('='*60)

f = 1

while f == 1:
    crt = int(input('Qual área você deseja calcular ?\n [1] Círculo\n [2] Triângulo\n [3] Retângulo\n==> '))
    print('_'*60)

    if crt == 1:
        a = int(input('Qual o raio em metros do círculo ? '))
                
        area = 3.14 * a **2
        print(f'A área do seu círculo é de {area}.')
        print('_'*60)

        t = int(input('Deseja calcular outra área ?\n [1] Sim\n [2] Não\n==> '))
        f = t
        if t == 2:
            print('_'*60)
            print('Fim do programa.')

    elif crt == 2:
        b = int(input('Qual a base do triângulo ? '))
        h = int(input('Qual a altura do triângulo ? '))

        area = (b * h)/2
        print(f'A área do seu trângulo é de {area} metros.')
        print('_'*60)

        t = int(input('Deseja calcular outra área ?\n [1] Sim\n [2] Não\n==> '))
        f = t 
        if t == 2:
            print('_'*60)
            print('Fim do programa.')

    elif crt == 3:
        l = int(input('Qual a largura do seu retângulo ? '))
        c = int(input('Qual o comprimento do seu triângulo ? '))

        area = l * c
        print(f'A área do seu retângulo é de {area} metros.')
        print('_'*60)

        t = int(input('Deseja calcular outra área ?\n [1] Sim\n [2] Não\n==> '))
        f = t
        if t == 2:
            print('_'*60)
            print('Fim do programa.')
        
    else:
        print('OPÇÃO INVÁLIDA...')
        t = int(input('Deseja tentar novamente ?\n [1] Sim\n [2] Não\n ==> '))
        f = t
        if t == 2:
            print('_'*60)
            print('Fim do programa.')