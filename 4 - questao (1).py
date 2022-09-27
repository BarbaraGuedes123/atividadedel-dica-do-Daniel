n1 = float(input('Digite a 1º número: '))
n2 = float(input("Digite a 2ºª número: "))
n3 = float(input("Digite a 3º número: "))

if n1 > n2 > n3:
    print(f"{n1} > {n2} > {n3}")
elif n1 < n2 > n3:
    print(f'{n2} > {n1} > {n3}')
elif n1 < n2 < n3:
    print(f'{n3} > {n2} > {n1}')
elif n1 > n2 < n3:
    if n1 < n3:
        print(f'{n3} > {n1} > {n2}')
    elif n1 > n3:
        print(f'{n1} > {n3} > {n2}')



