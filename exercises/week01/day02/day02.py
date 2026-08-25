score_count=5

def grade_for(score:float)->str:
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"


def read_score(index:int)->float:
    while True:
        raw=input(f"请输入第{index}个分数：")

        try:
            score=float(raw)
        except ValueError:
            print(f"请输入数字")
            continue

        if not 0 <= score <= 100:
            print(f"分数必须在 0 到 100 之间。")
            continue

        return score

def main():
    total=0
    highest=0
    grade_counts={
        "A":0,
        "B":0,
        "C":0,
        "D":0,
        "F":0
    }
    for index in range(1,score_count+1):
        score=read_score(index)
        total+=score
        grade=grade_for(score)
        grade_counts[grade]+=1
        highest=max(highest,score)

    average=total/score_count
    print(f"最高分：{highest:.2f}")
    print(f"平均分：{average:.2f}")
    print(f"等级分布人数：")
    for grade in ("A","B","C","D","F"):
        print(f"{grade}:{grade_counts[grade]}人")


if __name__=="__main__":
    main()
