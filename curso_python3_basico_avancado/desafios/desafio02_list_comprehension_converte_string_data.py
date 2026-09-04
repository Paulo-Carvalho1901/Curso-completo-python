# Desafio
# você tem uma lista com várias datas de formato
# de string e deseja convertê-las em formato datetime
# do Python, o que vai te permitir ter muito mais
# flexibilidade para lidar como as datas

from datetime import datetime

datas_string = ['01/08/2021', '17/08/2000', '31/01/2000', '26/10/2010']

for data in datas_string:
    data_time = datetime.strptime(data, "%d/%m/%Y")

    print(data_time)
