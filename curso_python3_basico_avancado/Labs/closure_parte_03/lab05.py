# Closures

def outer_fuc(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_fuc('Hi')
hello_func = outer_fuc('Hello')

hi_func()
hello_func()