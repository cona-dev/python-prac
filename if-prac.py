weather = input("오늘 날씨는 어때요? (비, 미세먼지, 눈, 맑음 중 입력하세요.) : ")
if weather == "비" or weather == "눈":
    print(">> 우산을 챙기세요\n")
elif weather == "미세먼지":
    print(">> 마스크를 사용하세요\n")
else:
    print(">> 준비물 필요 없어요\n")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print(">> 너무 더워요. 나가지 마세요.\n")
elif 10 <= temp and temp < 30:
    print(">> 괜찮은 날씨에요.\n")
elif 0 <= temp and temp < 10:
    print(">> 외투를 챙기세요.\n")
else:
    print(">> 너무 추워요. 나가지 마세요.\n")
