# ===========================================================
# 다중 상속
# 형식: 자식클래스(부모클래스1, 부모클래스2, ..., 부모클래스n)
# 규칙
## 자신의 클래스에서 메소드/속성 찾기
## 자신의 클래스에 존재 x -> 부모클래스1
## 부모클래스1에 존재 x -> 부모클래스2
## 부모클래스2 존재 x -> 에러
# ============================================================

class Animal:
    def hello(self):
        print("안녕! 난 animal이야.")

    def hi(self):
        print("안녕! 반가워!")


class Dog(Animal):
    # 메소드 오버라이딩
    def hello(self):
        print("안녕! 난 Dog야.")

class Cat(Animal):
    # 메소드 오버라이딩
    def hello(self):
        print("안녕! 난 Cat이야.")


class new_animal(Dog, Cat):
    pass

# 인스턴스 생성 및 사용
dog = Dog()
cat = Cat()
animal = Animal()
data = list()
new_ani = new_animal()


# 부모 자식 관계 검사
print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")
print(f"issubclass(Cat, Animal): {issubclass(Cat, Animal)}")
print(f"issubclass(Dog, Cat): {issubclass(Dog, Cat)}")
print()

# 특정 클래스로 생성된 인스턴스 즉, 객체 여부 검사 isinstance(변수명, 클래스명)
print(f"isinstance(cat, Cat): {isinstance(cat, Cat)}")
print(f"isinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"isinstance(dat, list): {isinstance(data, list)}")


# 매소드 사용
cat.hello()
animal.hello()
cat.hi()

new_ani.hello()

# __dict__: 포함된 속성/메소드 리스트를 추출
print(new_animal.__dict__)
print(new_ani.__dict__)
print()

print(Cat.__dict__)
print(cat.__dict__)

## 메소드 호출 순서
print("Cat.mor: ", Cat.mro())




