# 問題文
# 半径Rの円の周長を出力してください。
#
# 制約
# 1≤R≤100入力は全て整数である。

# 提出結果：正解

from math import pi

r = int(input())
len = (r * 2) * pi

print(len)
