# 問題文
# 高橋君の夏休みはN日間です。
# 夏休みの宿題がM個出されており、i番目の宿題をやるにはAi日間かかります。
# 複数の宿題を同じ日にやることはできず、また、宿題をやる日には遊ぶことができません。
# 夏休み中に全ての宿題を終わらせるとき、最大何日間遊ぶことができますか？
# ただし、夏休み中に全ての宿題を終わらせることができないときは、かわりに -1 を出力してください。
#
# 制約
# 1≤N≤106
# 1≤M≤104
# 1≤Ai≤104

# 提出結果：正解
# 他のコードも見たけど、何で正解なのか全く理解できないw

vacation, homework = map(int, input().split())
daysList = []
days = list(map(int, input().split()))
for i in range(homework):
    daysList.append(days[i])
play_days = vacation - sum(daysList)

if play_days >= 0:
    print(play_days)
else:
    print(-1)
