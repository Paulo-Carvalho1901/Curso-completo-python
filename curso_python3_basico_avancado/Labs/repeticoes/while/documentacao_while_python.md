
# Estrutura de Repetição `while` em Python

A estrutura `while` em Python é utilizada para repetir um bloco de código **enquanto** uma condição for verdadeira. Ela é muito útil quando não sabemos previamente quantas vezes o laço deve ser executado.

## ✅ Conceito
O `while` verifica uma condição lógica (True ou False). Enquanto a condição for **True**, o bloco interno continua sendo executado.

### Sintaxe básica
```python
while condição:
    # bloco de código a ser executado repetidamente
```

## ✅ Funcionamento
1. A condição é avaliada.
2. Se for **True**, o bloco é executado.
3. Ao final do bloco, a condição é avaliada novamente.
4. O ciclo continua até que a condição se torne **False**.

⚠️ **Atenção:**
Certifique-se de que algo dentro do laço modifique a condição. Caso contrário, o laço poderá se tornar infinito.

Exemplo:
```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

## ✅ Quando usar `while` em vez de `for`?
Use `while` quando:
- O número de repetições **não é conhecido** de antemão.
- Você depende de uma condição externa para finalizar o laço.

Exemplo típico: esperar entrada válida do usuário.
```python
senha = "1234"
digito = ""

while digito != senha:
    digito = input("Digite a senha: ")

print("Acesso permitido!")
```

---

# ✅ Exercícios para Praticar
A seguir, três exercícios básicos para fixar o uso do `while`.

## 🔹 Exercício 1
Peça para o usuário digitar números até que ele digite **0**. Ao final, exiba a soma de todos os números digitados.

## 🔹 Exercício 2
Imprima os números de **1 a 20** usando um `while`.

## 🔹 Exercício 3
Faça um programa que continue pedindo uma senha ao usuário até que ele acerte. Quando acertar, exiba uma mensagem de sucesso.

---

Bom estudo e boa prática! 🚀
