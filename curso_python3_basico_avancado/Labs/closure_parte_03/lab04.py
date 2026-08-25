from pdb import set_trace

# Ola, Ahoy, Hello

def externa(id):
    dic = {'pt': 'olá', 'pi': 'Ahoy', 'en': 'Hello'}
    def interna(nome):
        print('{} {}'.format(dic[id], nome))
    return interna


func = externa('pt')
func('Pedro')
func('Maria')
func('João')

print()
func = externa('pi')
func('Pedro')
func('Maria')
func('João')
