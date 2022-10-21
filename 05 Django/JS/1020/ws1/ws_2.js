function palindrome(str) {
    if (str === str.split('').reverse().join('')){
      console.log(true)
    }
    else{
      console.log(false)
    }
  }

palindrome('level')
palindrome('hi')

  // 출력
  // palindrome('level') => true
  // palindrome('hi') => false

  // every함수로 만들기
  function palindrome2(str){
    str.split('').every(function (char, idx){
      return char ===str[str.length - 1 -idx];
    });
  }