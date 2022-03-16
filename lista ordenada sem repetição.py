""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

valores = list()
for cont in range(0, 5):
    valor = (int(input(f'Digite um valor: ')))
    if cont == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-='*30)
print(f'Você digitou os valores: {valores}')
