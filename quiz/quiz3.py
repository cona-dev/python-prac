"""
Quiz3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
http://naver.com

규칙1: http:// 부분은 제외 -> naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

생성된 비밀번호 예시 : nav51!
"""

inputSiteAddress = "http://naver.com"
print(inputSiteAddress)
 
index = inputSiteAddress.find("/")
index = inputSiteAddress.find("/", index + 1)
print(index)

index2 = inputSiteAddress.find(".")

temp = inputSiteAddress[index + 1:index2]
print(temp)

pwd = temp[:3] + str(len(temp)) + str(temp.count("e")) + "!"

print(pwd)