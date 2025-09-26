# oop에서 property는 객체의 속성을 제어할 때 유용하게 사용되는 기능
# 데이터 캡슐화에 도움

class Person:
    def __init__(self, first_name, last_name, age):
        self.frist_name = first_name
        self.last_name = last_name
        self.age = age

person = Person("John", "Doe", 20)

# 필드명에 직접 접근해서 읽기나 쓰기가 가능해서 편리
# 그러나 외부로 부터 데이터 보호를 할 수 없는 무방비 상태에 놓이게 됨
print(person.age)
person.age = person.age + 1
print(person.age)