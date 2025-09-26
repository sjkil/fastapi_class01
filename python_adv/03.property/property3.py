# property 데코레이터를 사용하면 더 간결하고 읽기 편하게 작성이 가능

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        
        self._age = age


user1 = User('John', 'Doe', 20)

print(user1.age)
# user1.age = -1 #동일하게 속성의 validation 검증 가능
user1.age += 1
print(user1.age)

