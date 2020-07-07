jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) 

# ------------------------------------------------------
# 문자열 함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) #두번째 n의 인덱스를 찾음
print(index)

print(python.find("n")) #해당되는 값이 없을 때에는 -1을 반환하여 없다는 것을 보여줌

# -----------------------------------------------------

print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))

# -----------------------------------------------------

age = 24
color = "보라"
print(f"나는 {age}살이며, {color}색을 좋아해요.")