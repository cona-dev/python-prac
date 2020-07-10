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
