def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end=" | ")
    print()

profile("chaeyeon", 24, "Python", "Java", "JavaScript", "Html", "css")
profile("jinho", 27)

# ---------------------------------------------------------------------------

gun = 10

#local gun
def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

#global gun
def checkpoint2(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint2(2)
print("남은 총 : {0}".format(gun))
