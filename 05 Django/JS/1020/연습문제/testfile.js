const name = 'yeni'

switch(name) {
    case '홍길동' :{
        console.log('관리자님 환영합니다.')
        break
    }
    case 'manager' :{
        console.log('매니저님 환영합니다.')
        break
    }
    default:{
        console.log(`${name}님 환영합니다.`)
    }
}