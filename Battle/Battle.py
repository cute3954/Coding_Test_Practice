# 問題文
# 高橋君と青木君がモンスターを闘わせます。
# 高橋君のモンスターは体力がAで攻撃力がBです。 青木君のモンスターは体力がCで攻撃力がDです。
# 高橋君→青木君→高橋君→青木君→... の順に攻撃を行います。 攻撃とは、相手のモンスターの体力の値を自分のモンスターの攻撃力のぶんだけ減らすことをいいます。
# このことをどちらかのモンスターの体力が 0以下になるまで続けたとき、 先に自分のモンスターの体力が 0以下になった方の負け、そうでない方の勝ちです。
# 高橋君が勝つなら Yes、負けるなら No を出力してください。
#
# 制約
# 1≤A,B,C,D≤100
# 入力はすべて整数である。

# 提出結果：不正解

t_hp, t_power, a_hp, a_power = map(int, input().split())

while True:
    a_hp -= t_power
    t_hp -= a_power
    if a_hp < 0 or t_hp < 0:
        break

if t_hp > a_hp:
    print("Yes")
else:
    print("No")

# ------------------------------------------------------------------------------------
# 参照：https://atcoder.jp/contests/abc164/submissions/12369376
# While文の中で判定すべきだった。
# また、0未満になってるのも不正解の原因かも

t_hp, t_power, a_hp, a_power = map(int, input().split())

while True:
    a_hp -= t_power
    t_hp -= a_power
    if a_hp <= 0:
        print("Yes")
        break
    elif t_hp <= 0:
        print("No")
        break
