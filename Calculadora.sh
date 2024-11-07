#!/bin/bash

# Calculadora em Shell Script

# Solicitando ao usuário que insira o primeiro número

echo -n "Digite o primeiro número: "
read num1

# Solicitando ao usuário que insira o operador

echo -n "Digite o operador (+, -, *, /): "
read operador

# Solicitando ao usuário que insira o segundo número

echo -n "Digite o segundo número: "
read num2

# Verificando o operador inserido e realizando a operação correspondente

if [ "$operador" == "+" ]; then
    resultado=$((num1 + num2))

elif [ "$operador" == "-" ]; then
    resultado=$((num1 - num2))

elif [ "$operador" == "*" ]; then
    resultado=$((num1 * num2))

elif [ "$operador" == "/" ]; then
    resultado=$((num1 / num2))

else
    echo "Opção Inválida!"
fi

# Exibindo o resultado

echo "Resultado: $resultado"
