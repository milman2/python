from datetime import date

class User:
  def __init__(self, id: int, name: str, birthdate:date, admin: bool = False) -> None:
    self.id = id
    self.name = name
    self.birthdate = birthdate
    self.admin = admin

  def __repr__(self) -> str:
    # return f"User(id={self.id}, name='{self.name}', birthdate={self.birthdate}, admin={self.admin})"
    return self.__class__.__qualname__ + "(" + ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items()) + ")"

  # 필드값이 동일한 경우에는 동등한 인스턴스 취급 => __eq__ 메서드 오버라이딩 필요
  def __eq__(self, other) -> bool:
    if isinstance(other, User): # other.__class__ == self.__class__
      # self.id == other.id and self.name == other.name and self.birthdate == other.birthdate and self.admin == other.admin
      return (self.id, self.name, self.birthdate, self.admin) == (other.id, other.name, other.birthdate, other.admin)
    return NotImplemented

user = User(id=1, name="Steave Jobs", birthdate=date(1955, 2, 24))
print(user)

# 동등성 비교
user1 = User(id=1, name="Steave Jobs", birthdate=date(1955, 2, 24))
user2 = User(id=1, name="Steave Jobs", birthdate=date(1955, 2, 24))
print(user1 == user2)  # False, 객체의 주소값이 다르기 때문

# dataclass 데코레이터를 사용하면 __init__, __repr__, __eq__ 메서드를 자동으로 생성해준다.
from dataclasses import dataclass

@dataclass
class User2:
  id: int
  name: str
  birthdate: date
  admin: bool = False

user3 = User2(id=1, name="Steave Jobs", birthdate=date(1955, 2, 24))
user4 = User2(id=1, name="Steave Jobs", birthdate=date(1955, 2, 24))
print(user3 == user4)  # True, 필드값이 동일하기 때문
user3.admin = True  # 가변 객체이므로 admin 필드값을 변경할 수 있다.
print(user3 == user4)


# 불변성 보장해야 하는 경우
@dataclass(frozen=True)
class User3:
  id: int
  name: str
  birthdate: date
  admin: bool = False
user5 = User3(id=1, name="Steave Jobs", birthdate=date(1955, 2, 24))
# user5.admin = False

# 대소 비교
@dataclass(order=True)
class User4:
  id: int
  name: str
  birthdate: date
  admin: bool = False
user6 = User4(id=1, name="Steave Jobs", birthdate=date(1955, 2, 24))
user7 = User4(id=2, name="Bill Gates", birthdate=date(1955, 10, 28))
print(user6 < user7)  # True, id 필드값이 작은 경우
print(user6 > user7)

# 정렬
print(sorted([user7, user6]))  # [User4(id=1, name='Steave Jobs', birthdate=datetime.date(1955, 2, 24), admin=False), User4(id=2, name='Bill Gates', birthdate=datetime.date(1955, 10, 28), admin=False)]

# set, dict에 사용하기
#set([user1, user2])

@dataclass(unsafe_hash=True)
class User5:
  id: int
  name: str
  birthdate: date
  admin: bool = False

user8 = User5(id=1, name="Steave Jobs", birthdate=date(1955, 2, 24))
user9 = User5(id=2, name="Bill Gates", birthdate=date(1955, 10, 28))
user10 = User5(id=1, name="Steave Jobs", birthdate=date(1955, 2, 24))
user11 = User5(id=2, name="Bill Gates", birthdate=date(1955, 10, 28))
print(set([user8, user9, user10, user11]))  # {User5(id=1, name='Steave Jobs', birthdate=datetime.date(1955, 2, 24), admin=False), User5(id=2, name='Bill Gates', birthdate=datetime.date(1955, 10, 28), admin=False)}

# 주의 사항: list와 같이 가변데이터 필드에 기본값을 할당하는 경우
# 필드의 기본값은 서로 다른 인스턴스간에 공유된다.
# => default_factory 함수를 사용하여 각 인스턴스마다 새로운 객체를 생성하도록 해야 한다.
from dataclasses import field

@dataclass(unsafe_hash=True)
class User6:
  id: int
  name: str
  birthdate: date
  admin: bool = False
  # friends: list[int] = []  # 가변데이터 필드에 기본값을 할당하는 경우, 모든 인스턴스가 동일한 리스트 객체를 참조하게 된다.
  friends: list[int] = field(default_factory=list)  # default_factory 함수를 사용하여 각 인스턴스마다 새로운 객체를 생성하도록 해야 한다.

user12 = User6(id=2, name="Bill Gates", birthdate=date(1955, 10, 28))
print(user12.friends) # []
user12.friends.append(1)
print(user12.friends) # [1]