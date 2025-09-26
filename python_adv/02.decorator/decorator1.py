# # decorator는 함수를 매개변수로 받아 새로운 함수를 반환하는 함수
# # decorator를 활용하면 함수의 코드를 수정하지 않고도, 부가적인 기능을 추가하거나 작동 방식을 변경가능

def say_hi():
    print("Say Hi~")

def say_bye():
    print('Say bye~')

print('before : ' + say_hi.__name__)
say_hi()
print('after : ' +  say_hi.__name__)

print('before : ' + say_bye.__name__)
say_bye()
print('after : ' + say_bye.__name__)


def decorate(func):
    def wrapper():
        print(f'before')
        func()
        print(f'after')
    return wrapper


def say_hi():
    print("Hi~")


def say_bye():
    print('Say bye~')

say_hi_deco = decorate(say_hi)
say_hi_deco()

say_bye_deco = decorate(say_bye)
say_bye_deco()