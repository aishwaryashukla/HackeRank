import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

print(randomly_greet("aishwarya"))

def do_multiple(num):
    def decorate_multi(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                val = func(*args, **kwargs)
        return wrapper
    return decorate_multi


@do_multiple(3)
def hi_hello(name):
    print(f'hello hi {name}')


hi_hello("Sam")

def try_decorate(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@try_decorate
def print_once(name):
    print(f'Hello say it once {name}')

print_once("kewal ek bar")