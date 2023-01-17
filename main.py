import random


def jugar(vidas):
    num = random.randint(1, 100)
    num_e = None

    while num_e != num:
        num_e = int(input('Ingrese un numero entre 1 y 100: '))

        if num > num_e:
            print('-' * 30)
            print('|  EL NUMERO ES MAYOR  |')
            print('-' * 30)
            vidas -= 1
        elif num < num_e:
            print('-' * 30)
            print('|  EL NUMERO ES MENOR  |')
            print('-' * 30)
            vidas -= 1
        if vidas == 0:
            print('*' * 30)
            print('PERDISTE... JUEGO TERMINADO')
            print('El numero era:', num)
            print('*' * 30)
            break

        if num == num_e:
            print('*' * 30)
            print('|  !!FELICIDADES LO LOGRASTE!!  |')
            print('*' * 30)
            break

        print(f'Te quedan {vidas} ♥ vidas')


def principal():
    op = 0
    while op != 4:
        print('-' * 30)
        print('|  ADIVINA EL NUMERO  |')
        print('1 - NIVEL FACIL (10 VIDAS)\n'
              '2 - NIVEL MEDIO ( 7 VIDAS)\n'
              '3 - NIVEL DIFICIL (5 VIDAS) \n'
              '4 - SALIR')
        print('-' * 30)
        op = int(input('Ingrese una opcion: '))
        if 0 < op < 5:
            if op == 1:
                jugar(10)
            elif op == 2:
                jugar(7)
            elif op == 3:
                jugar(5)
            elif op == 4:
                print('Cerrando juego....')
        else:
            print('La opcion no es valida!')


if __name__ == '__main__':
    principal()
