#write
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

#read
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

