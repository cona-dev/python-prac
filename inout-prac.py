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