subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

# 유재석과 조세호 사이에 정형돈을 태움
subway.insert(1, "정형돈")
print(subway)

# 뒤에서부터 꺼내기

print(subway.pop())
print(subway)

# 정렬하기

num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 리스트 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 및 리스트 확장
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, False]

num_list.extend(mix_list)
print(num_list)