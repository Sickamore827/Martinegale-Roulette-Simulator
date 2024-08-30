import random
import numpy as np

starting_bet = int(input('Enter bet amount: '))

def spin_roulette():
    roulette_values = {
    0: 'green',
    1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red', 8: 'black', 9: 'red',
    10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black', 16: 'red', 17: 'black', 18: 'red',
    19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red',
    28: 'black', 29: 'black', 30: 'red', 31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red',
    37: 'green'
}
    num = random.randint(0, 37)
    roulette_color = roulette_values.get(num)
    return roulette_color

def num_color(li_of_colors):
    black = 0
    green = 0
    red = 0
    for color in li_of_colors:
        if color == 'black':
            black += 1
        elif color == 'red':
            red += 1
        else:
            green += 1
    return black, green, red



def caluclate_winning_bet(balance, bet):
    balance = balance - bet
    payout = bet*2
    new_amount =  balance + payout
    # print(f"bet: {bet}, ")
    return new_amount

# def caluclate_losing_bet(player, bet):
#     player = player - bet
#     return player


def calculate_next_bet(balance, prev_bet, win):
    if win:
        return starting_bet
    else:
        new_bet = prev_bet * 2
        if balance - new_bet < 0:
            return -1
        return new_bet

def hands(hand_amount):
    winning_color = []
    balance = 2048
    current_bet = starting_bet
    longest_streak = 0
    current_streak = 0
    for i in range(hand_amount):
        number = spin_roulette()
        winning_color.append(number)
        if number != 'black':
            print(f'roll: {i}')
            current_streak += 1
            print(f'current losing streak: {current_streak}')
            print(f'color: {number}')
            prev_bet = current_bet
            # print(f'current bet: {prev_bet}')
            current_bet = calculate_next_bet(balance, current_bet, False)
            if current_bet == -1:
                print('you lost all of your money')
                return 0, winning_color, current_streak
            balance -= prev_bet
            print(f'current balance: {balance}')
            print('======================================')
        else:
            if current_streak > longest_streak:
                longest_streak = current_streak
            current_streak = 0
            prev_bet = current_bet
            current_bet = calculate_next_bet(balance, current_bet, True)
            balance = caluclate_winning_bet(balance, prev_bet)
            print(f'roll: {i}')
            print(f'current balance: {balance}')
            print('======================================')
        
        current_gains = balance - 2048
    return current_gains, winning_color, longest_streak

def roulette(day_amount, hand_amount):
    total_balances = []
    black = []
    green = []
    red = []
    losing_streak = []
    for i in range(day_amount):
        print(f'day: {i}')
        daily_balance, li_of_colors, longest_streak = hands(hand_amount)
        black1, green1, red1 =  num_color(li_of_colors)
        if daily_balance == 0:
            return print('Ya ran outta money pal')
        black.append(black1)
        red.append(red1)
        green.append(green1)
        losing_streak.append(longest_streak)
        print(f'daily increase: {daily_balance}')
        total_balances.append(daily_balance)
    total_green = sum(green)
    total_red = sum(red)
    total_black = sum(black)
    longest_losing_streak = np.max(losing_streak)
    final_balance = np.sum(total_balances)
    print(f'black:{total_black}, red:{total_red}, green:{total_green} \ntotal gains:{final_balance} \nlongest losing streak: {longest_losing_streak}') 


        
            

        



        
roulette(10, 200)
# spin_roulette()



    
