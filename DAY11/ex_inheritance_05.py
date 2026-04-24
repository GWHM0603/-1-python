# ===========================================================
# 사용자 정의 클래스와 내장 클래스 사용
# 내장 클래스: int, float, str, list, ...
# 사용자 정의 클래스: 프로그램 구성 데이터용 클래스
#                    (EX 1: 학생관리 프로그램 -> 주데이터 학생: 학생 클래스)
#                    (EX 2: 게    임 프로그램 -> 주데이터 캐릭터: 캐릭터 클래스)
# ============================================================

class Student:
    shcool_name = "KDT"

    def __int__(self, name, stdno, major):
        self.name = name
        self.stdno = stdno
        self.major = major


# 1개의 데이터를 저장하는 경우
# 점수 1개 저장
jumsu = 98

# 학생 1명 저장
std01 = Student("홍길동", 1, "컴공")


# 10개 데이터 저장하는 경우
jumsu_list = [98, 99, 76, 87, 56, 75, 34, 56, 88, 85]

# 학생 10명 저장
std_list = [Student("홍길동", 1, "컴공"), Student("임꺽정", 2, "기계"), Student("허준", 3, "로봇")]

for std in std_list:
    print(std.name)