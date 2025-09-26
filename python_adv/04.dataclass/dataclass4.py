# 중요 dataclass를 사용할때 가장 많이 하는 실수로 주의해야됨
# 필드의 속성으로 list를 사용할때

from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    age: int
    friends: list[int] = []   # 에러나는 이유 설명시 list copy, deepcopy로 예시

user1 = User(id=1, name='tommy', age=17)
user2 = User(id=1, name='tommy', age=17)
print(user1)
print(user1 == user2)

# 위와 같이 빈 리스트를 초기값으로 넣어 줄경우 아래와 같은 에러가 발생
# default_factor를 사용하라는 에러가 발생

# 빈 리스트로 초기화 해서 사용할 경우 아래와 같이 사용해야 됨

from dataclasses import dataclass, field
from datetime import date

@dataclass
class User:
    id: int
    name: str
    age: int
    friends: list[int] = field(default_factory=list)

user1 = User(id=1, name='tommy', age=17)
user2 = User(id=1, name='tommy', age=17)

user1.friends.append(10)
print(user1)