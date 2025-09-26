# functools.wraps의 활용
from functools import wraps

def decorate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'before')
        result = func(*args, **kwargs)
        print(f'after')
        return result
    return wrapper

@decorate
def say_hi(*args, **kwargs):
    return f"{kwargs['name']} {args[0]}"

@decorate
def say_bye(*args, **kwargs):
    return f"{kwargs['name']} {args[0]}"


print(say_hi("say hi~", name = 'tommy'))
print(say_bye("say bye~", name = 'angela'))
print(say_hi.__name__)
print(say_bye.__name__)
