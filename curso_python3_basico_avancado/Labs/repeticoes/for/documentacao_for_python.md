# Estrutura de Repetição `for` em Python

A estrutura de repetição `for` em Python é usada para percorrer **sequências** e executar um bloco de código repetidamente para cada elemento.

Ela é ideal quando você **sabe antecipadamente quantas vezes** o código deve se repetir.

---

## ✅ Conceito

O `for` funciona como um **“para cada”**.

> Para cada elemento dentro de uma sequência, o bloco de código será executado.

---

## ✅ Sintaxe básica

```python
for variavel in sequencia:
    # código executado para cada item
```

Exemplo:

```python
for numero in range(5):
    print(numero)
```

Saída:

```
0
1
2
3
4
```

---

## ✅ A função `range()`

A função `range()` gera uma sequência de números, muito usada com `for`.

```python
range(inicio, fim, passo)
```

Exemplos:

```python
range(1, 6)     # de 1 até 5
range(0, 10, 2) # apenas números pares
```

---

## ✅ Exemplos práticos

### 🔹 Contando de 1 a 5

```python
for i in range(1, 6):
    print(i)
```

### 🔹 Percorrendo uma lista

```python
nomes = ["Ana", "Carlos", "Mariana"]

for nome in nomes:
    print(nome)
```

### 🔹 Percorrendo uma string

```python
palavra = "Python"

for letra in palavra:
    print(letra)
```

---

## ✅ `for` x `while`

### Usando `for`

```python
for i in range(5):
    print(i)
```

### Usando `while`

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

📌 O `for` costuma ser mais **simples e legível** quando a quantidade de repetições é conhecida.

---

## ✅ Quando usar `for`?

Use `for` quando:

- Você sabe quantas vezes o laço deve se repetir
- Está percorrendo listas, strings ou `range()`
- Quer um código mais claro e organizado

---

## ✅ Exercícios para praticar

### 🔹 Exercício 1

Imprima os números de **1 a 10** usando `for`.

### 🔹 Exercício 2

Peça ao usuário para digitar **5 números** e mostre a soma no final.

### 🔹 Exercício 3

Crie uma lista com nomes de 5 pessoas e imprima cada nome.

### 🔹 Exercício 4 (extra)

Imprima apenas os números **pares de 0 a 20** usando `for`.

---

🚀 **Bons estudos com Python!**
