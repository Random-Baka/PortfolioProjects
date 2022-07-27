let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

const generateTarget = () => {
    return randomNum = Math.floor(Math.random() * 9);
}

const compareGuesses = (human, computer, target) => {
    if (human > 9 || human < 0) {
        alert("Out of range, you lose!");
        return false;
    } else {
    human = Math.abs(human - target);
    computer = Math.abs(computer - target);
    if (human === computer || human < computer) {
        return true;
    }
        return false;
    }
}

const updateScore = (winner) => {
    if (winner === 'human') {
        humanScore++;
    } else  {
        computerScore++;
    }
}

const advanceRound = () => {
    currentRoundNumber++;
}