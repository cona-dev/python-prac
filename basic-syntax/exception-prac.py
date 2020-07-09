# # 예외상황 처리
# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))

# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")

# #이미 있는 에러를 그대로 출력해주고 싶을 때 사용방법
# except ZeroDivisionError as err: 
#     print(err)


# list를 사용해서 나누기 전용 계산기 만들기

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번쩨 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))

    print( "{} / {} = {}".format(nums[0], nums[1], nums[2]) )

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")