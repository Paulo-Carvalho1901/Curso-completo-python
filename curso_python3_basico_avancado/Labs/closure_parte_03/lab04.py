from pdb import set_trace

def externa():
    # set_trace()
    def interna():
        print(42)
    return interna


func = externa()
func()
