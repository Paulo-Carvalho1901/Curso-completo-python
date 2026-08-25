from pdb import set_trace
var = 7

def func():
    # print(var)
    global var # criado efeto colateral na função
    print(var)
    var = 18
    print(var)
    # set_trace()


func()
print(var)
