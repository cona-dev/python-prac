"""
Quiz2 ) 월 4회 스터디를 하는데 3회는 온라인 1번은 오프라인

조건1 : 랜덤으로 날짜 뽑기
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

출력 예시 : 오프라인 스터디 모임 날짜는 매월 X일로 선정되었습니다.
"""

from random import *

day = int(randrange(4,29))

print("오프라인 스터디 모임 날짜는 매월 " + str(day) +"로 선정되었습니다.")