import copy

from dados import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novo_produtos = [
    # mapeamento e a copia produnda
   {**p, 'preco': round(p['preco'] * 1.1, 2)} 
    for p in produtos
]

print('Produtos originais')
print(*produtos, sep='\n')
print()
print('Novos produtos aumento de 10%')
print(*novo_produtos, sep='\n')
print()

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print('Produtos ordenados por nome')
print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)