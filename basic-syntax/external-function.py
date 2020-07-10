"""
google에서 list of python modules 검색

glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
os : 운영체제에서 제공하는 기본 기능 

"""

import glob
print(glob.glob("*.py")) #확장자가 py인 모든 파일

import os
print(os.getcwd()) #현재 디렉토리


folder = "simple_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
else:
    os.makedirs(folder) #folder 생성
    print(folder, "폴더를 생성하였습니다.") #폴더가 있는데 또 생성하라고 했을 때, 구문 실행되지 않음


print(os.listdir())

# time : 시간 관련 함수
import time 
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) #현재 시간 찍어내기

import datetime
print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) #100일 저장

print("우리가 만난지 100일은 ",today+td)