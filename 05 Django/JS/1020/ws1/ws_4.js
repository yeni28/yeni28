const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
	// 작성해 주세요
        if (p1_choice === 'rock' && p2_choice ==='paper'){
            console.log(2)
        }
        else if (p2_choice === 'rock' && p1_choice ==='paper'){
            console.log(1)
        }
        else if (p1_choice === 'rock' && p2_choice ==='scissors'){
            console.log(1)
        }
        else if (p2_choice === 'rock' && p1_choice ==='scissors'){
            console.log(2)
        }
        else if (p1_choice === 'paper' && p2_choice ==='scissors'){
            console.log(2)
        }
        else if (p2_choice === 'paper' && p1_choice ==='scissors'){
            console.log(1)
        }
        else if (p2_choice ===  p1_choice ){
            console.log(0)
        }

    }



for (const idx in p1) {
    p1_choice = p1[idx]
    p2_choice = p2[idx]
    playGame(p1_choice, p2_choice)
}
// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2
