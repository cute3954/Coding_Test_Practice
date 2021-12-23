function solution(participant, completion) {
    var answer = "";

    var participantCount = participant.reduce(countName, {}); // 初期値は{}
    var completionCount = completion.reduce(countName, {}); // 初期値は{}

    // Object.keys(): オブジェクトのキーが格納された新規配列を作成
    // そして新規作成された配列に対してforEach()でループするので、エラーにならない
    Object.keys(participantCount).forEach(function(key) {
        if (typeof completionCount[key] === "undefined" || participantCount[key] !== completionCount[key]) {
            answer = key;
        }
    });
    return answer;
}

/**
 * 配列内の重複した要素を数える
 * 
 * @param {*} prev 
 * @param {*} current 
 * return prev
 */
function countName(prev, current) {
    prev[current] = (prev[current] || 0) + 1;
    return prev;
}

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]);