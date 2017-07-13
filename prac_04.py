# encoding: utf-8

import random


game_count = 0
all_count =[]
while True:
    game_count += 1
    guess_count = 0
    answer = random.randint(0,99)
    while True:
        guess = int(input("請猜一個數字 (0~99): "))
        guess_count += 1
        if guess == answer:
            print("恭喜你猜對了!")
            print("你總共猜了" + str(guess_count) + "次")
            all_count.append(guess_count)
            break;
        elif guess > answer:
            print("你猜的數字太大了!")
        elif abs(guess - answer) <= 3:
            print("差一點點!")
        else:
            print("你猜的數字太小了!")
    onemore = input("要再玩一次嗎?(Y, N)? ")
    if onemore != 'Y' and onemore != 'y':
        print("歡迎下次再來~")
        print("你的成績如下: ")
        print(all_count)
        print("平均猜中次數" + str(sum(all_count) / float(len(all_count))))
        break;
