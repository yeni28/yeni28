const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]



// for(marvel of participantNums){
//     for(num in marvel){
//         const DDugi = funtion(marvel){
//             if(marvel[num] === marvel[num]){
//                 cnt += 1
//         }
    
//     }}



// 3
// 100
// 62

//
function findSolo(arr){
    //카운트 결과를 담아줄 딕셔너리 생성
    const candidates = {};
    // 깍두기를 찾아내기 위해서 참가 번호를 부여받은 사람이 몇 명 있는지 확인
    // 참가번호가 key, value는 참가 번호를 부여받은 사람의 수
    // '1' : 2, '2' : 2 '3': 1
    for (num of arr){
        //아직 키가 있다면 1을 할당하고, 이미 있다면 1을 추가
        if (candidates[num]=== undefined){
            candidates[num] = 1;
        } else {
            candidates[num] += 1;
        }
    }
    for (candidate in candidates){
        if(candidates[candidate]===1){
            console.log(candidate);
            break;
        }
    }
}

participantNums.forEach(function(tc){
    findSolo(tc);
})