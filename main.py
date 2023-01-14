#!/usr/bin/env python
#
# Hit and Blow
#   使われている数字の種類を数える
#   
import random

def is_number_correct(target: str) -> bool:
    s = set()
    for c in target:
        s.add(c)

    return len(s) == len(target)

def target_num() -> str:
    while True:
        t: str = str(random.randint(123,9876)).zfill(4)
        if is_number_correct(t):
            return str(t)

def count_hit(com_num: str, player_num: str) -> int:
    count: int = 0

    for i in range(4):
        if com_num[i] == player_num[i]:
            count += 1
    return count

def count_blow(com_num: str, player_num: str, hit_num: int) -> int:
    count: int = 0

    for i in range(4):
        if player_num[i] in com_num:
            count += 1
    return count - hit_num

def judge(com_num: str, player_num: str) -> bool:
    if com_num == player_num:
        print("Congraturation!")
        return True
    hit_num = count_hit(com_num, player_num)
    blow_num = count_blow(com_num, player_num, hit_num)

    print(f'{hit_num} hit {blow_num} blow')
    return False

def input_number() -> str:
    p: str = "0000" + input()
    l = len(p)
    return p[l-4:]

def main() -> None:
    t: str = target_num()
    while not judge(t, input_number()):
        pass
    return

if __name__ == "__main__":
    main()
