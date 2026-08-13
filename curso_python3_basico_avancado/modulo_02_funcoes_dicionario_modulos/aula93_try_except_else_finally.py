# try, execpt, else, and finally

try:
   print('Abril o arquivo')
   # 8 / 0
except ZeroDivisionError:
   print('Dividiu por zero.')
else:
   print('Não deu erro...')
finally: # sempre executado
   print('Fechar aquivo...')
