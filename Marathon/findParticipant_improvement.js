function solution(participant, completion) {
    var completionNameCount = completion.reduce((prev, current) => (prev[current] = prev[current] ? prev[current] + 1 : 1), {});

    return participant.find(participantName => {
        if (completionNameCount[participantName]) {
            completionNameCount[participantName] = completionNameCount[participantName] - 1;
        } else {
            // find() メソッドは、提供されたテスト関数を満たす配列内の最初の要素の値を返す。
            return true;
        }
    });
}

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]);