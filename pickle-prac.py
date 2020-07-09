# pickle을 사용하려면 바이너리라는걸 알려줘야 하기 때문에 wb, rb 같은 식으로 씀

import pickle # module이라고 지칭함
profile_file = open ("profile.pickle", "wb")
profile = {"name":"Smith", "":30, "hobby":["golf", "coding"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile_file)
profile_file.close()