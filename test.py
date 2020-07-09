# for i in range(1,3):
#     report_file = open("{0}_report.txt".format(i), "w", encoding="utf8")
#     print("- {0}주차 주간보고 -".format(i))
#     print("부서 : ", file=report_file)
#     print("이름 : ", file=report_file)
#     print("업무 요약 : ", file=report_file)

# report_file.close()

score_file = open("test.txt", "w", encoding="utf8") # file create
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()
