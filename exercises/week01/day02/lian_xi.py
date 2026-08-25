# SCORE_COUNTS=5
#
# def get_scores(index:int)->float:
#     while(True):
#         raw = input(f"请输入第{index}个成绩：")
#         try:
#             score = float(raw)
#         except ValueError:
#             print("请输入数字")
#             continue
#
#         if not(0 <= score <= 100):
#             print("请输入0到100以内的数字")
#             continue
#
#         return score
#
# def grade_counts(score:float)->str:
#     if score>=90:
#         return "A"
#     elif score>=80:
#         return "B"
#     elif score>=70:
#         return "C"
#     elif score>=60:
#         return "D"
#     else:
#         return "E"
#
# def main():
#     total = 0
#     highest = 0
#     for index in range(1, SCORE_COUNTS+1):
#         score=get_scores(index)
#         total+=score
#         highest=max(highest,score)
#         grade_count={
#             "A":0,
#             "B":0,
#             "C":0,
#             "D":0,
#             "E":0,
#         }
#         grade=grade_counts(score)
#         grade_count[grade]+=1
#
#     average=total/SCORE_COUNTS
#     print(f"最高分：{highest:.2f}")
#     print(f"平均成绩：{average:.2f}")
#     print("各等级人数：")
#     for grade in grade_count.keys():
#         print(f"{grade}:{grade_count[grade]}")
#
#
# if __name__=="__main__":
#     main()

# 判断奇偶
# def parity_of(num: int) -> str:
#     if num % 2 == 0:
#         print("这个数字是偶数")
#     else:
#         print("这个数字是奇数")
#     return -1
#
# def main():
#     raw=input('请输入数字：')
#     try:
#         num=int(raw)
#     except ValueError:
#         print('请输入整数')
#
#     parity_of(num)
#
#
# if __name__ == '__main__':
#     main()

# 统计及格和不及格人数
# NUM_COUNTS=5
# def classify(num:int)->str:
#     if num>=60:
#         return "及格"
#     else:
#         return "不及格"
#
# def get_num(index:int)->float:
#     while True:
#         raw=input(f"请输入第{index}个数字：")
#
#         try:
#             num=float(raw)
#         except ValueError:
#             print('请输入数字')
#             continue
#
#         if not 0<=num<=100:
#             print("请输入0到100以内的数字")
#             continue
#         return num
#
# def main():
#     num_grade={
#         "及格":0,
#         "不及格":0
#     }
#     for index in range(1,NUM_COUNTS+1):
#         num=get_num(index)
#         grade=classify(num)
#         num_grade[grade]=num_grade[grade]+1
#
#     print(num_grade)
#
#
# if __name__=="__main__":
#     main()


