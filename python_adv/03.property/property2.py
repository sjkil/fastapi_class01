# oop에서 property는 객체의 속성을 제어할 때 유용하게 사용되는 기능
# 데이터 캡슐화에 도움
# 일반 class에서 getter, setter 사용법

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age     # 속성에 _를 붙이는 것은 외부에서 직접 접근하면 안된다는 네이밍 컨벤션임 (private, protected, public)

    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age

    age = property(get_age, set_age)


user1 = User('John', 'Doe', 20)
print(user1.get_age())

user1.set_age(10)
print(user1.get_age())


# 속성에 데이터 변경이 불가능해 지는것은 아님
user1._age = 100

# age라는 속성을 추가해서 새로 데이터를 넣는거와 같은 것
user1.age = 200
