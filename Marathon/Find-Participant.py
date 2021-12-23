# マラソンで完走出来なかった選手探し.
#
# 【条件】
# 完走できなかった選手は1人のみ.
# 同姓同名あり.
def solution(participant, completion):
    # マラソンで完走出来なかった選手
    answer = ''
    # sort(): 元のリストをソート
    # sorted(): ソートした新たなリストを生成
    sorted_participant = sorted(participant)
    sorted_completion = sorted(completion)

    for index in range(len(sorted_completion)):
        if sorted_participant[index] != sorted_completion[index]:
            answer = sorted_participant[index]
            return answer

    return answer

def main():
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

if __name__ == '__main__':
    main()