# 問題文
# くじ引きをN回行い、i回目には種類が文字列Siで表される景品を手に入れました。
# 何種類の景品を手に入れましたか？
#
# 制約
# 1≤N≤2×105
# Siは英小文字のみからなり、長さは1以上10以下

# 提出結果：正解

lotteries = []
num_of_lot = 0
num = int(input())

for i in range(num):
    lotteries.append(input())

num_of_lot = len(set(lotteries))

print(num_of_lot)

# ------------------------------------------------------------------------------------
# 参照：https://atcoder.jp/contests/abc164/submissions/12481856
# コードがもっときれいになった

num = int(input())
lotteries = list(input() for i in range(num))
num_of_lot = len(set(lotteries))
print(num_of_lot)
