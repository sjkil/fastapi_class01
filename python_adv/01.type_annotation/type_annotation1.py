# 파이썬은 동적 프로그래밍 언어
# 1. 파이썬에서 변수의 타입은 고정되어 있지 않아 개발자가 원하면 바꿀수 있음
# 2. 동적프로그래밍 언어인 파이썬은 인터프리터가 코드를 실행하면서 타입을 추론
# 3. 타입을 명시적으로 표시할 필요가 없어 파이썬은 다른 언어에 비해 간단명료한 코드 작성 가능
no = 1
print(type(no))

no = '1'
print(type(no))

number1 = 1
number2 = "2"

print(number1, number2)
print("-" * 20)
print(number1 + number2)


# 파이썬 버전 3.5에 추가된 타입 어노테이션
# 1. 파이썬의 유연함은 스크립트나 소규모 어플리케이션을 빠르게 개발할 때 유용
# 2. 규모가 큰 프로젝트에서는 파이썬의 다이나믹함이 치명적인 버그로 이어질 수 있음
# 3. 따라서 중규모 이상의 파이썬 프로젝트에서는 타입 힌팅을 개발 프로세스에 도입

# type hinting 지원 전
num = 1 # type: int

def repeat(message, times):
    # type: (str, int) -> list[str]
    return [message] * times


# type hinting 지원 후
num: int = 1

def repeat(message: str, times: int) -> list[str]:
    return [message] * times

# 변수 타입 어노테이션
name: str = "John Doe"
age: int = 25
height: float = 182.8
flag: bool = True


emails: list[str] = ["john1@doe.com", "john2@doe.com"]

students: dict[str, str] = {
  "tommy": "jejudo",
  "angela": "seoul",
  "jason": "busan"
}

# 함수 타입 어노테이션

def stringify(num: int) -> str:
    return str(num)

def plus(num1: int, num2: float = 3.5) -> float:
    return num1 + num2

def greet(name: str) -> None:
    print("hi! " + name)

def repeat(message: str, times: int = 2) -> list[str]:
    return [message] * times