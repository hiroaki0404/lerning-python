#!/usr/bin/env python
#
# Hit and Blow
#   Web version
#   
import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def is_number_correct(target: str) -> bool:
    if target[1] == target[0] or \
        target[2] == target[1] or target[2] == target[0] or \
        target[3] == target[2] or target[3] == target[1] or target[3] == target[0]:
        return False
    return True

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

def judge(com_num: str, player_num: str) -> tuple[str, int, int]:
    if com_num == player_num:
        return com_num, 4, 0
    hit_num = count_hit(com_num, player_num)
    blow_num = count_blow(com_num, player_num, hit_num)

    return player_num, hit_num, blow_num

@app.route("/", methods = ["GET"])
def main():
    session["target"] = target_num()
    session["history"] = []
    return render_template("index.html")

@app.route("/", methods=["POST"])
def play():
    t: str = "0000" + (request.form.get("number") or "" )
    p: str = t[len(t)-4:]
    j = judge(session["target"], p)
    h =session["history"]
    h.append(j)
    session["history"] = h
    if j[1] == 4:
        return render_template("win.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
