# try, execpt, else, and finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
   print('Abril o arquivo')
   # 8 / 0
except ZeroDivisionError:
   print('Dividiu por zero.')
else:
   print('Não deu erro...')
finally: # sempre executado
   print('Fechar aquivo...')
