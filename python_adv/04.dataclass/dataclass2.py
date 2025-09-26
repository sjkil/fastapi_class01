# 정확한 정보를 출력하려면 __repr__ 매직메소드 만들어 줘야함

class User:
    def __init__(self, id: int, name: str, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return self.__class__.__qualname__ + f"(id={self.id}, name={self.name}, age={self.age})"
    
    def __eq__(self, other) -> bool:
        if other.__class__ is self.__class__:
            return (self.id == other.id and
                    self.name == other.name and
                    self.age == other.age)
        
        return NotImplemented

    # # 아래는 상속받은 클래스 까지 허용    
    # def __eq__(self, value):
    #     if isinstance(value, User):
    #         return (self.id == value.id and
    #                 self.name == value.name and
    #                 self. age == value.age)
        
    #     return NotImplemented

user1 = User(id=1, name='Steve Jobs', age=54)
user2 = User(id=1, name='Steve Jobs', age=54)

print(f"{user1}")
print(user1 == user2)

print('-' * 200)
# __name__ 과 __qualname__의 차이
class User:
    pass

user1 = User()

print(user1.__class__.__name__)  
# 출력: User

class Outer:
    class Inner:
        pass

obj = Outer.Inner()

print(obj.__class__.__name__)     # Inner
print(obj.__class__.__qualname__) # Outer.Inner

