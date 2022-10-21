// 1. 배열에 담긴 중복된 이름을 {'이름': 수} 형태의 object로 반환하세요.

const names = ['harry', 'aiden', 'julie', 'julie', 'edward']

// answer
// 중복된 값이 생기면 값이 2가 된다. 없다면 1이된다.


const counted = names.reduce(function(acc, name){
    if(name in acc){
        acc[name] += 1
    } else {
        acc[name] = 1
    }
    return acc;
},{})

console.log(counted)