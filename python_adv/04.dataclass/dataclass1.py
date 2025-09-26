# 파이썬으로 코딩을 하면서 데이터를 담아두기 위해 여러가지 방법을 사용
# list, tuple, dictionary, 내장 자료구조는 사용하기 간편
# 파이선 3.7에서 dataclasses 모률 표준 라이브러리에 추가
# 내장 자료구조처럼 편리하면서 클래스처럼 견고한 데이터 클래스

class User:
    def __init__(self, id: int, name: str, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age

user1 = User(id=1, name='Johe Doe', age=18)
user2 = User(id=1, name='Johe Doe', age=18)

print(user1.id)
print(user1.name)
print(user1.age)

print(user1)    # <__main__.User object at 0x105563c70>

print(user1 == user2)   # 비교안됨