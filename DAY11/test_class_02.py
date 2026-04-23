# 사용자 정의 클래스
# >>> 사람 클래스 정의
# 데이터: 이름, 나이, 성별, 키, 몸무게, 지역
# 기능/역할
# > 사람 정보 출력 기능 -> 이름, 나이, 성별, 키, 몸무게

# 클래스 이름: Person
# 클래스 속성: name, age, gender, height, weight
# 클래스 함수: print_info(), BMI_check()


class Person:

    def __init__(self,  name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
    
    def print_info(self):
        print('-'*12)
        print(f"이  름: {self.name}")
        print(f"나  이: {self.age}세")
        print(f"성  별: {self.gender}")
        print(f"키    : {self.height}cm")
        print(f"몸무게: {self.weight}kg")
        print('-'*12)
    
    def BMI_check(self):
        
        self.height = self.height * 0.01
        print("BMI:", round(self.weight / (self.height ** 2), 2))
        print('-'*12)
        

per = Person("홍길동", 20, "남", 170, 65)
per.print_info()
per.BMI_check()  