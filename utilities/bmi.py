def calculate_bmi():
    print("BMI計算機へようこそ！")
    
    height = float(input("身長をメートル単位で入力してください。:"))
    weight = float(input("体重をキログラム単位で入力してください："))

    bmi = weight / (height ** 2)
    print("あなたのBMIは{:.2f}です。".format(bmi))
    
    # BMI判定
    if bmi < 18.5:
        print("低体重です")
    elif bmi < 25:
        print("普通体重です")
    elif bmi < 30:
        print("肥満（1度）です")
    else:
        print("肥満（2度以上）です")

if __name__ == "__main__":
    calculate_bmi()