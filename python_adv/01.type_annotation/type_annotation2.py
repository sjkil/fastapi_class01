# typing 모듈 python 3.5 이후
# list, dict, tuple, set와 같은 내장 타입을 이용가능
# typing 모듈에서 제공하는 List, Dict, Tuple, Set를 사용하여 원소의 타입까지 명시 가능

# List
from typing import List, Dict, Tuple, Set

num: List[int] = [1, 2, 3]

def total_length(words: List[str]) -> int:
    return sum(len(w) for w in words)


# Dict
temperateres: Dict[str, float] = {"bedroom": 25.1, 'kitchen': 23, "bathroom": 19.8}

def invert(mapping: Dict[str, int]) -> Dict[int, str]:
    return {v: k for k, v in mapping.items()}


# Tuple
user: Tuple[int, str, bool] = (3, "Dale", True)
number: Tuple[int, ...] = (1, 2, 3, 4, 5)

def get_point() -> Tuple[int, int]:
    return (3, 4)


# Set
chars: Set[str] = {"A", "B", "C"}

def unique_numbers(nums: List[int]) -> Set[int]:
    return set(nums)


# python 3.9이후 typing 모듈 없이 사용가능

num: list[int] = [1, 2, 3]
temperateres: dict[str, float] = {"bedroom": 25.1, 'kitchen': 23, "bathroom": 19.8}
user: tuple[int, str, bool] = (3, "Dale", True)
chars: set[str] = {"A", "B", "C"}


# Final type: 재할당이 불가능한 변수, 즉 상수에 대한 타입 어노테이션
from typing import Final, Union, Optional, Literal

TIME_OUT: Final[int] = 10
TIME_OUT = 100


# Union type: 여러 개의 타입이 허용
data: Union[int, str]
data = 10
data = "hello"

def stringify(x: Union[int, float]) -> str:
    return str(x)


# Optional: 선택적으로 변수를 할당하거나 None이 허용되는 함수의 매개 변수에 대한 타입 명시할 때 유용
nickname: Optional[str] = None

def greet(name: Optional[str] = None) -> str:
    return f"Hello {name or 'Guest'}"

print(greet('tommy'))   # Hello tommy
print(greet())          # Hello Guest

# Literal
def set_status(status: Literal["ON", "OFF"]) -> None:
    """정해진 값만 허용"""
    print(f"Status: {status}")

set_status("ON")   # OK
set_status("OFF")  # OK
set_status("YES")  # ❌ 에러

# 딱 정해진 값만 허용하는 타입
# 'ON' 또는 'OFF'만 받을 수 있음
# 버튼 상태, 신호등 색깔, 모드 설정처럼 제한된 값만 가능할 때 유용