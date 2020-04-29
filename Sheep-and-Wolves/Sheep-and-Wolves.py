# 問題文
# 羊がS匹、狼がW匹います。
# 狼の数が羊の数以上のとき、羊は狼に襲われてしまいます。
# 羊が狼に襲われるなら unsafe、襲われないなら safe を出力してください。

# 制約
# 別に気にしなくても良さそう。
# 1 ≤ S ≤ 100、1 ≤ W ≤ 100

# 提出結果：不正解

s, w = (int(x) for x in input("please enter number of sheep and wolves: ").split())
if 1 <= s <= 100 and 1 <= w <= 100:
    if s > w:
        print("safe")
    else:
        print("unsafe")
else:
    print("invaild values...")

# ------------------------------------------------------------------------------------
# なぜか不正解が出で、解説を参考した。
# 全く意味わからんw
s, w = map(int, input().split())
if w >= s:
    print("unsafe")
else:
    print("safe")
