print("Python", "Java", "C++", sep=" vs ") # Python vs Java vs C++

print("Python", "Java", sep = ",", end = "? ") # Python,Java? 무엇이 더 재밌을까요?
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr) # 표준 에러메세지를 띄우는 것

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)

print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), score) # 좌측 정렬
# 수학       0
# 영어       50
# 코딩       100


for subject, score in scores.items():
    print(subject.rjust(8), score) # 우측 정렬
#       수학 0
#       영어 50
#       코딩 100


for subject, score in scores.items():
    print(subject.center(8), score) # 센터 정렬
#    수학    0
#    영어    50
#    코딩    100

for num in range(1, 21):
    print("Wating no : " + str(num).zfill(3)) #3크기만큼의 자리를 확보하고 숫자가 채워지지 않는 곳은 0을 삽입

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")
# 사용자가 입력한 값은 항상 문자열로 변수에 저장되는 것을 인지해야함


# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print( "{0: >10}".format(500) )

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))

# 3자리 마다 콤마 찍어주기
print("{0:,}".format(100000000000))

# 3자리 마다 콤마 찍어주기, +- 부호 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기

print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시 (수수점 셋째 자리에서 반올림)
print("{0:.2f}".format(5/3))
