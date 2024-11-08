# ProtejoEBAC
### Calculadora em Shell Script e Calculadora em Python

Sejam bem-vindos ao ProjetoEBAC. Nesse projeto estarei apresentando a vocês dois arquivos que possuem como função ser uma calculadora.
Logo abaixo estarei informando como executar o arquivo "Calculadora.sh" e explicando o arquivo "Calculadora.py".

## Como Executar um Arquivo em Shell Script

Shell scripts são arquivos de texto que contêm uma sequência de comandos para serem executados em um terminal Unix/Linux. Eles são amplamente usados para automatizar tarefas e simplificar processos repetitivos.

### Passo 1: Fazer o download do arquivo
1. Dentro do diretório ProjetoEBAC clique no arquivo "[Calculadora.sh](https://github.com/Rafael-Leandro/ProtejoEBAC/blob/main/Calculadora.sh)".
2. Após abrir o arquivo procure pelos três pontos (...) que estão localizados no canto direito superior.
3. clique nos três pontos (...) e faça o download do arquivo.

OBS: Certifique-se de salvar o arquivo em um local de fácil acesso para você, pois será necessário saber o caminho de acesso para executar o arquivo no terminal.

### Passo 2: Encontrar o arquivo no terminal
1. Abra o terminal e acesse o diretório onde o arquivo baixado foi salvo.
2. Você pode utilizar os comandos 'pwd' e 'cd' para saber em que diretório está e acessar outro diretório respectivamente.
3. Ao acessar o diretório onde o arquivo foi salvo utilize o comando 'ls' para certificar-se que o arquivo se encontra no diretório.

### Passo 3: Executando o arquivo
1. Antes de executar o script, é necessário confirmar se o mesmo já possui a permissão de execução do arquivo.
2. Utilize o comando 'ls -l' e verifique se o arquivo possui a permissão para executar.
3. Caso não possua a permissão, utilize o comando 'chmod +x Calculadora.sh'. Dessa forma o arquivo se torna executável.
4. Com o arquivo já possuindo a permissão de executar basta utilizar o comando './Calculadora.sh'.
5. Pronto. Agora você já consegue utilizar a sua calculadora em Script Shell.


## Explicação da Calculadora.py
A Calculadora.py é um código bem simples mas que aborda conceitos essencias como a interação com o usuário através do 'input', a utilização de operadores aritméticos e relacionais e também a aplicação das condicionais para a escolha da operação matemática.

• O código inicia solicitando ao usuário que informe dois números:
```
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
```

• Após o usuário informar os dois números, uma lista com as quatro operações matemáticas é apresentada na tela para que o usuário possa escolher a operação que deseja utilizando os números de 1 ao 4.
```
print("Qual operação deseja fazer com seus números?")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
escolha = int(input("Escolha um dos números das operações acima: "))
```

• Depois do usuário escolher o número que representa a operação matemática que deseja realizar o código fará, através das condicionais, a verificação da escolha do usuário e irá realizar a operação escolhida.
```
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
```

• Por fim, se o usuário escolher um número que não corresponde a nenhuma das operações matemáticas o código irá apresentar uma mensagem informando que o número escolhido não corresponde a nenhuma das opções.
```
else:
	print('O número escolhido não corresponde a nenhuma das opções!')
```
