# Solicitando dois números para o usuário

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Opções de cálculos

print("Qual operação deseja fazer com seus números?")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
escolha = int(input("Escolha um dos números das operações acima: "))

# Condições para cada escolha

# Adição
if escolha == 1:
	soma = n1 + n2
	print(f'A soma de {n1} e {n2} é igual a {soma}.')

# Subtração
elif escolha == 2:
	sub = n1 - n2
	print(f'A subtração de {n1} e {n2} é igual a {sub}.')

# Multiplicação
elif escolha == 3:
	multi = n1 * n2
	print(f'A multiplicação de {n1} por {n2} é igual a {multi}.')

# Divisão
elif escolha == 4:
	div = n1 / n2
	print(f'A divisão de {n1} por {n2} é igual a {div}.')

# Número não correspondente
else:
	print('O número escolhido não corresponde a nenhuma das opções!')
