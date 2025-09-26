
#이건 하지말자...

# ------------------------------
# TypeVar / Generic
# ------------------------------

from typing import TypeVar

T = TypeVar('T')  # 제네릭 타입 변수

def first_item(items: list[T]) -> T:
    """리스트 첫 번째 요소 반환, 타입 유지"""
    return items[0]

print(first_item([1, 2, 3]))        # int 반환
print(first_item(["a", "b", "c"]))  # str 반환
print(first_item([True, False]))    # bool 반환

# T는 "아직 정해지지 않은 타입"을 뜻함
# 리스트 안에 있는 타입을 유지하면서 꺼낼 수 있음
# 들어간 타입 그대로 나오니까 안전하게 사용가능

# 여러 개의 TypeVar

S = TypeVar("S")
U = TypeVar("U")

def pair(x: S, y: U) -> tuple[S, U]:
    return (x, y)

print(pair(1, "hi"))   # (int, str)
print(pair("a", 3.14)) # (str, float)

# S, U 각각 독립적인 타입이어서 입력 타입 관계를 유지할 수 있음.

# 클래스에서 TypeVar 사용

from typing import Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()
    
s1 = Stack[int]()
s1.push(1)
s1.push(2)
print(s1.pop())  # int

s2 = Stack[str]()
s2.push("a")
s2.push("b")
print(s2.pop())  # str

# Stack[int]는 int만 저장하는 스택
# Stack[str]는 str만 저장하는 스택
# 타입이 섞이지 않아서 안전!

# TypeVar는 "변수에 붙은 라벨" 같은 것.
# T = TypeVar("T") 라고 하면 "이 함수 안에서는 T라는 타입으로 통일하겠다"는 뜻.

# "컵"에 비유하면:
# TypeVar 있는 경우: "이건 물컵이다 → 물만 따라라"

# Any 쓰는 경우: "그냥 컵 → 뭘 따라도 되는데, 잘못 따라도 몰라"