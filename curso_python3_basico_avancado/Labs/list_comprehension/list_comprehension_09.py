# Pegue uma lista de nomes e
# altere apenas a ultima letra para maiusculo

nomes = ['paulo', 'andreia', 'davi', 'vitoria', 'daniel']

novos_nomes = [f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in nomes]

print(novos_nomes)
