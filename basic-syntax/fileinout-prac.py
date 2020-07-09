# score_file = open("score.txt", "w", encoding="utf8") # file create
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # 이미 있는 파일에 내용 추가하기 append
# score_file.write("과학 : 80", file=score_file)
# score_file.write("코딩 : 100", file=score_file)
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r 줄별로 읽기, 한 줄 익고 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline()) # 자동으로 줄바꿈해줌 줄 안바꾸고 싶으면 print(score_file.readline(), end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장

for line in lines:
    print(line, end="")

score_file.close()
