# Sequence: 읽기 전용 시퀀스 타입을 표현할 때 사용, 즉 순서가 있고 인덱싱/슬라이싱이 가능하며, 반복가능한 자료구조
# list, tuple, str, bytes, bytearray, range -> OK
# set, dict, generator, iterator -> NO

from typing import Sequence

def first(seq: Sequence[int]) -> int:
    return seq[0]
data = [10, 20, 30]
print(first(data))

data = (10, 20, 30)
print(first(data))

data = "abcd"
print(first(data))

data = range(10)
print(first(data))


# 사용자 정의 타입 힌팅
from dataclasses import dataclass

@dataclass
class User:
    name: str

user1: User = User('tommy')
user2: User = User('angela')

def one(player: User, npc: User) -> None:
    print(player, npc)

one(player=user1, npc=user2)