import random

def number_guessing_game():
    print("数当てゲームへようこそ！")
    print("1から100までの数を当ててください。")

    target = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("あなたの予想を入力してください: "))
            attempts += 1

            if guess < target:
                print("もっと大きい数です。")
            elif guess > target:
                print("もっと小さい数です。")
            else:
                print(f"正解です！ {attempts}回で当てました！")
                break
        except ValueError:
            print("無効な入力です。整数を入力してください。")

if __name__ == "__main__":
    number_guessing_game()