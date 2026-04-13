## =======================================
## 컨테이너 자료형 - [1] List
## List 전용 메서드 사용
## =======================================

# >>> 1 ~ 30 범위에서 7의 배수로만 구성된 데이터

num_list = range(7,31,7) # 타입이 range임 -> 형 변환 필요
num_list = list(num_list)
print(f"[1] 리스트: {num_list}    개수: {len(num_list)}개")
print()

# >>> List 전용 함수 즉, 메서드 사용
# >>> 원소/요소 추가 -> 마지막: 변수명.appned()

num_list.append(100)
print(f"[2] 리스트: {num_list}    개수: {len(num_list)}개")
print()


# >>> 객체명.insert(a, b) a번째 위치에 B 삽입
num_list.insert(0, 90)
print(f"[3] 리스트: {num_list}    개수: {len(num_list)}개")
print()

num_list.insert(-1, 1000)
print(f"[4] 리스트: {num_list}    개수: {len(num_list)}개")
print()

print("=====================================================")
str_list = ['a', 'e', 'c', 'd','f', 'b']
str_list.sort()
print(f"[1]{str_list}")
print()

str_list.sort(reverse=True)
print(f"[2]{str_list}")
print()

# >>> 단순 뒤집기만 함. 정렬 기능 없음
str_in = ['h', 'e', 'l', 'l' ,'o']
str_in.reverse()
print(str_in)

# >>> List: count vs len
count_list = [1, 1, 1, 2, 2]
print(f"[1] {count_list}    {len(count_list)}개")
print(f"[2] {count_list}    {count_list.count(1)}개")
print()

# >>> 원소/요소 삭제 : remove vs pop
int_list = [1, 2, 3, 4, 5]
int_list.remove(3)
print("==== remove(x): x 요소 삭제 ====")
print(f"[1] {int_list}")
print()

print("==== pop(): 마지막 인덱스에 해당하는 요소 삭제 후 반환 ====")
int_list = [1, 2, 3, 4, 5] 
print(f"[2] {int_list.pop()}") # 마지막 인덱스 추출 반환
print(f"[3] {int_list}")
print()
print(f"[4] {int_list.pop()}") # 마지막 인덱스 추출 반환
print(f"[5] {int_list}")
print()


print("==== pop(인덱스 위치): 특정 인덱스 위치에 있는 요소 삭제 후 반환 ====")
int_list = [1, 2, 3, 4, 5]
print(f"[6] {int_list.pop(2)}") # 특정 인덱스 추출 후 반환
print(f"[7] {int_list}")
print()

# >>> 리스트 원소를 모두 삭제할려면 clear(), 리스트 자체를 삭제할려면 del 사용