# return이 있는 데코레이터 처리

def decorate(func):
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


# 아래의 코드는 decorator4.py 를 설명하기 위한 빌드업
# functools.wraps의 활용전에 먼저 실행해서 보여줘야 함
# 함수명 wrapper로 출력됨
print(say_hi.__name__)
print(say_bye.__name__)
