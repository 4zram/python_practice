def auth(fn):
    def wrapper(*args, **kwargs):
        message = fn (*args, **kwargs) if args[0]['valid'] else print('Unauthorised user')
        return message
    return wrapper

@auth
def sso(u1):
    print('Your message has been printed')

users = {'name':'Azram', 'valid':True}
sso(users)