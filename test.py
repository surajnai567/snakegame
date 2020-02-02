

def token(token):
    if token == 0 :
        return True
    else:
        return False


def auth(fun):
    def wrap(*arg, **kwargs):
        if token(arg[0]):
            return arg, kwargs
        else: return 'fail'

    return wrap


@auth
def view(token, input):
    return input

print(view(0, "i"))




