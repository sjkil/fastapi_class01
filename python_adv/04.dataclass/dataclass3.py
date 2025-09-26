# 위에와 같이 기존의 클래스 만드는 방법으로 데이터 클래스를 작성하려면 아주 많은 코드를 작성해야됨
# dataclass 모듈을 사용하면 위의 복잡한 코드를 아주 간단하게 해결할 수 있음
# dataclass의 옵션을 가지고 다양한 부가 기능을 사용할 수 있음

from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    age: int
    
user1 = User(id=1, name='tommy', age=25)
user2 = User(id=1, name='tommy', age=25)


print(user1)
print(user2)

print(user1 == user2)

user1.age = 10
print(user1.age)