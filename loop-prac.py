# for

for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{}님 커피가 준비되었습니다.".format(customer))

# while

customer = "토르"
index = 5
while index >= 1:
    print("{0}님 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if(index == 0):
        print("커피는 폐기처분되었습니다.")
    
customer = "아이언맨"
while True: # 반복문에 종료조건 없으면 치명적이므로 무조건 break 조건 있어야 함.
    print("{0}님 커피가 준비되었습니다.".format(customer, index))
    index += 1
    if(index > 10):
        break

# interactive

customer = "smith"
person = "Unknown"

while person != customer:
    print("{0}님 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

    if person == "smith":
        print("맛있게 드세요.")
    else:
        print("죄송합니다.")

# continue는 break와 달리 다시 조건문으로 돌아가서 체크함
