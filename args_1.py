def greet(name, *args):
    return f"Hello, {name}!" if not args else f"Hello, {name} and {' and '.join(args)}!"

'''
def greet(name, *args):
    return f'Hello, {" and ".join((name,) + args)}!'
    
    
def greet(name, *args):
    return f'Hello, {" and ".join((name, *args))}!'
'''