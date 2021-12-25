# 電話帳での前方一致判定.
#
# 【条件】
# 各電話番号の長さは1以上20以下.
# 重複なし.
def solution(phone_book):
    # 効率性3，4で失敗
    # for phone_number in phone_book:
    #     result = next(filter(lambda x: x != phone_number and x.startswith(phone_number), phone_book), None)
    #     if result is not None:
    #         return False

    # 効率性3，4で失敗
    # for x in range(len(phone_book)):
    #     for y in range(len(phone_book)):
    #         if phone_book[y] != phone_book[x] and phone_book[y].startswith(phone_book[x]):
    #             return False

    phone_book.sort()
    for idx in range(1, len(phone_book)):
        count = len(phone_book[idx - 1])
        if phone_book[idx][0:count] == phone_book[idx - 1][0:count]:
            return False

    return True


def main():
    print(solution(["119", "97674223", "1195524421"]))


if __name__ == '__main__':
    main()
