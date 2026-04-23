# ===== ===== ===== ===== =====
# 모든 데이터 관련 자료형 ---  클래스로 구현
# 객체지향언어 --- 정보은닉, 다형성, 상속

# -> 정보은닉 특징
# [기본] 속성과 메소드를 숨기기. 공개용 속성과 메소드 따로 존재
#        은닉된 속성을 사용하는 방법이 제공됨. -> getter/setter


class Car:
    ## 자동차 인스턴스/객체를 생성 위한 메모리 힙 영역 스캔 후 메모리 할당 메서드
    def __init__(self, user, number, ckey):
        self.user = user
        self.number = number
        self.__ckey = ckey # 비공개 속성 저장. 클래스내에서만 사용가능

    def forward(self):
        print("forward() 호출")
        print(f"{self.number}번의 자동차가 전진한다.")
        print(f"ckey: {self.__ckey}")

    # getter/setter 메소드: 비공개 속성의 외부 접근 가능 메소든
    def get_ckey(self):
        return self.__ckey

    def set_ckey(self, nkey):
        self.__ckey = nkey


myCar = Car("홍길동", "12가 1234", "ABCD")
myCar.forward()

print(myCar.user)
print(myCar.number)
# print(myCar.__ckey) -> 비공개 속성이라 클래사 외부에서 사용 불가능
print(myCar.get_ckey())


myCar.user = "김지찬"
print(myCar.user)
print(myCar.__dict__, 1)

myCar.set_ckey("가나다라")
print(myCar.get_ckey())

print(myCar.__dict__, 2)
