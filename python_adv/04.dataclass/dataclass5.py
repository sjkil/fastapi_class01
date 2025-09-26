from dataclasses import dataclass, field
import copy

# =========================================
# 1️⃣ 잘못된 방법: mutable default
# =========================================
@dataclass
class UserBad:
    name: str
    friends: list[str] = []  # ❌ 모든 인스턴스가 같은 리스트를 공유

# 인스턴스 생성
u1 = UserBad("Alice")
u2 = UserBad("Bob")

# 친구 추가
u1.friends.append("Charlie")

print("=== UserBad ===")
print(f"u1.friends: {u1.friends}")  # ['Charlie']
print(f"u2.friends: {u2.friends}")  # ['Charlie'] <-- 공유되어 있음!

# =========================================
# 2️⃣ 올바른 방법: field(default_factory=list)
# =========================================
@dataclass
class UserGood:
    name: str
    friends: list[str] = field(default_factory=list)  # ✅ 새로운 리스트 생성

u3 = UserGood("Alice")
u4 = UserGood("Bob")

u3.friends.append("Charlie")

print("\n=== UserGood ===")
print(f"u3.friends: {u3.friends}")  # ['Charlie']
print(f"u4.friends: {u4.friends}")  # [] <-- 각자 독립적

# =========================================
# 3️⃣ copy vs deepcopy로 이해
# =========================================
original = UserGood("Zoe")
original.friends.append(["A", "B"])

# 얕은 복사(shallow copy): 리스트 객체를 그대로 공유
shallow = copy.copy(original)
shallow.friends[0].append("C")  # 원본에도 영향

# 깊은 복사(deep copy): 완전히 독립된 객체
deep = copy.deepcopy(original)
deep.friends[1].append("D")  # 원본에 영향 없음

print("\n=== Copy vs Deepcopy ===")
print(f"original.friends: {original.friends}")  # [['A', 'C'], 'B']
print(f"shallow.friends: {shallow.friends}")    # [['A', 'C'], 'B'] <-- 공유
print(f"deep.friends: {deep.friends}")          # [['A', 'C'], 'B', 'D'] <-- 독립
