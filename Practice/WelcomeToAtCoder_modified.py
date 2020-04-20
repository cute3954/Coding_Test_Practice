# https://practice.contest.atcoder.jp/tasks/practice_1#Python3
# 整数を格納する配列
numArray = []
# 整数の入力
a = int(input("please enter a number: "))
# スペース区切りの整数の入力
b, c = (int(x) for x in input("please enter two numbers: ").split())
# 配列に格納
numArray.extend([a, b, c])

# numArrayの値を足す
sum = 0
for var in numArray:
    sum += var

# 文字列の入力
s = input("please enter a string: ")

# 出力
if 1 <= sum <= 1000:
    print("result: {} {}".format(sum, s))
else:
    print("Error! Invalid Integer Value...")