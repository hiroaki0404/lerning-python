#!/usr/bin/env python
#
# Hit and Blow
#   慣れていない人が書くとこんな感じ？
#   
import random

def is_number_correct(target):
    k1 = target % 10
    k2 = (target // 10) % 10
    k3 = (target // 100) % 10
    k4 = target // 1000
    if k2 == k1 or \
        k3 == k2 or k3 == k1 or \
        k4 == k3 or k4 == k2 or k4 == k1:
        return False
    return True

def target_num():
    while True:
        t = random.randint(123,9876)
        if is_number_correct(t):
            return t

def count_hit(com_num, player_num):
    count = 0
    if com_num % 10 == player_num % 10:
        count += 1
    if (com_num // 10) % 10 == (player_num // 10) % 10:
        count += 1
    if (com_num // 100) % 10 == (player_num // 100) % 10:
        count += 1
    if com_num // 1000 == player_num // 1000:
        count += 1
    return count

def count_blow(com_num, player_num, hit_num):
    count = 0

    com_keta_1 = com_num % 10
    com_keta_2 = (com_num // 10) % 10
    com_keta_3 = (com_num // 100) % 10
    com_keta_4 = com_num // 1000

    player_keta_1 = player_num % 10
    player_keta_2 = (player_num // 10) % 10
    player_keta_3 = (player_num // 100) % 10
    player_keta_4 = player_num // 1000

    if com_keta_1 == player_keta_1 or \
        com_keta_1 == player_keta_2 or \
        com_keta_1 == player_keta_3 or \
        com_keta_1 == player_keta_4:
        count += 1
    if com_keta_2 == player_keta_1 or \
        com_keta_2 == player_keta_2 or \
        com_keta_2 == player_keta_3 or \
        com_keta_2 == player_keta_4:
        count += 1
    if com_keta_3 == player_keta_1 or \
        com_keta_3 == player_keta_2 or \
        com_keta_3 == player_keta_3 or \
        com_keta_3 == player_keta_4:
        count += 1
    if com_keta_4 == player_keta_1 or \
        com_keta_4 == player_keta_2 or \
        com_keta_4 == player_keta_3 or \
        com_keta_4 == player_keta_4:
        count += 1
    return count - hit_num

def judge(com_num, player_num):
    if com_num == player_num:
        print("Congraturation!")
        return True
    hit_num = count_hit(com_num, player_num)
    blow_num = count_blow(com_num, player_num, hit_num)

    print(f'{hit_num} hit {blow_num} blow')
    return False

def main():
    t = target_num()
    while not judge(t, int(input())):
        pass
    return

if __name__ == "__main__":
    main()
