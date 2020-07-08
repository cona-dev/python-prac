def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end=" | ")
    print()

profile("chaeyeon", 24, "Python", "Java", "JavaScript", "Html", "css")
profile("jinho", 27)