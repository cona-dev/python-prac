# language = input("무슨 언어를 좋아하세요?")
# print("{}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장함수
# print(dir())

# import pickle
# print(dir())
# 결과값으로 pickle과 random이 추가된 것을 terminal에서 확인할 수 있다.

print(dir(random)) # random 모듈 안에서 사용할 수 있는 것들에 대한 내용을 확인할 수 있음


lst = [1, 2, 3]
print(dir(lst)) #list타입인 lst 변수가 사용할 수 있는 function 목록을 확인할 수 있다
# google에서 list of python builtins 검색하면 똑같은 리스트를 확인할 수 있다

print()
print()

name = "Smith"
print(dir(name)) #string 타입 변수가 사용할 수 있는 function 목록을 확인할 수 있다