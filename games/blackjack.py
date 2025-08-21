import random

def calculate_total(hand):
    total = 0
    has_ace = False
    for card in hand:
        if card == 'A':
            total += 11
            has_ace = True
        elif card in ['K', 'Q', 'J']:
            total += 10
        else:
            total += int(card)

    if total > 21 and has_ace:
        total -= 10

    return total

def play_game():
    total_points = 100
    bet = 0

    while total_points > 0:
        print("現在のポイント：", total_points)
        bet = int(input("掛け金を設定してください。:"))

        if bet > total_points:
            print("ポイントが足りません。")
            continue

        player_hand = [random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']) for _ in range(2)]
        dealer_hand = [random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']) for _ in range(2)]
        print("プレイヤーの手札:", player_hand)
        print("ディーラーの手札:", dealer_hand[0])
        game_over = False
        
        while not game_over:
            action = input("ヒット(1) or スタンド(2)を選んでください：")

            if action == '1':
                player_hand.append(random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']))
                player_total = calculate_total(player_hand)
                print("プレイヤーの手札:", player_hand)
                if player_total > 21:
                    print("プレイヤーがバストしました")
                    total_points -= bet
                    game_over = True
            elif action == '2':
                player_total = calculate_total(player_hand)
                dealer_total = calculate_total(dealer_hand)
                print("プレイヤーの手札:", player_hand)
                print("ディーラーの手札:", dealer_hand)

                while calculate_total(dealer_hand) < 17:
                    dealer_hand.append(random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']))
                    dealer_total = calculate_total(dealer_hand)

                if dealer_total > 21:
                    print("ディーラーがバストしました")
                    total_points += bet
                elif dealer_total > player_total:
                    print("ディーラーの勝ちです")
                    total_points -= bet
                elif dealer_total < player_total:
                    print("プレイヤーの勝ちです")
                    total_points += bet
                else:
                    print("引き分けです")
                game_over = True
            else:
                print("無効な入力です。もう一度選んでください。")

        print("ゲーム終了")

if __name__ == "__main__":
    play_game()