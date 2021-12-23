import collections

def solution1(participant, completion):
    # collections.Counter()にリストやタプルを渡すと、Counterオブジェクトが生成される。
    # Counterは辞書型dictのサブクラスで、キーに要素、値に出現回数という形のデータを持つ。
    # Counterオブジェクト同士の加算・減算もできる。
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

def main():
    print(solution1(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

if __name__ == '__main__':
    main()