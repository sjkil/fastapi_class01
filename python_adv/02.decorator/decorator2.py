# 기본 데코레이터 사용법
def decorate(func):
    def wrapper():
        print(f'before')
        func()
        print(f'after')
    return wrapper

@decorate
def say_hi():
    print("Hi~")

@decorate
def say_bye():
    print('Say bye~')

say_hi()
say_bye()

# argument가 있으면 받아서 그대로 넘기기

def decorate(func):
    def wrapper(*args, **kwargs):
        print(f'before')
        func(*args, **kwargs)
        print(f'after')
    return wrapper

@decorate
def say_hi(*args, **kwargs):
    print(f"{kwargs['name']} {args[0]}")


@decorate
def say_bye(msg):
    print(msg)

say_hi("say hi~", name = 'tommy')
say_bye("say bye~")