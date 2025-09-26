# 읽기 전용 프로퍼티 만들때 유용하게 사용됨

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


user1 = User('John', 'Doe', 20)

print(user1.age)
print(user1.full_name)
