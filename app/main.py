"""
スラムダンク名言API
Fast API利用
    https://qiita.com/yota_dev/items/ab8dea7f71c8a130d5bf
起動コード
    uvicorn main:app --reload
叩く方法
    curl localhost:8000<任意>
"""


from fastapi import FastAPI
import random

app = FastAPI()

# スラムダンク名言ランキング
# https://sarashina0707.com/meigen/2/
msg = [
    "あきらめたらそこで試合終了ですよ",
    "安西先生……バスケがしたいです",
    "リバウンドを制する者は試合を制す",
    "左手はそえるだけ",
    "天才ですから",
    "天才とは99%の才能と1%の努力",
    "要チェックや！",
    "まだあわてるような時間じゃない",
    "お前の為にチームがあるんじゃねぇ チームの為にお前がいるんだ",
    "とりあえず君は日本一の高校生になりなさい",
]

# スラムダンクスタメン
mem = [
    "桜木花道",
    "流川楓",
    "赤木剛憲",
    "宮城リョータ",
    "三井寿",
]

# ルート: 説明
@app.get("/")
async def root():
    description = "スラムダンクのAPIです。/messageでランダムに名言を出力します。/talk/文字列でランダムなメンバが任意の文字列を言います"
    return {"message": description}

# /message: スラダン名言ランキング
@app.get("/message")
def message():
    rand = random.randint(0,9)
    return {"message": msg[rand]}

# /member: 任意の文字列をランダムなメンバに言わせられる
@app.get("/member/{item}")
def member(item: str):
    rand = random.randint(0,4)
    msg_member = mem[rand] + "「" + item + "」"
    return {"message": msg_member}

# /test: ランダムなメンバがランダムに名言を言う
@app.get("/test")
def test():
    rand_msg = random.randint(0,9)
    rand_member = random.randint(0,4)
    msg_test = mem[rand_member] + "「" + msg[rand_msg] + "」"
    return {"message": msg_test}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}
