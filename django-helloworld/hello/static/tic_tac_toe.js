boxes = {};

winpatterns = [ [0,1,2], [3,4,5], [6,7,8], //Horizontal
                [0,3,6], [1,4,7], [2,5,8], //Vertical
                [0,4,8], [2,4,6]]; //Diagonal
let announcement = null;
document.addEventListener('DOMContentLoaded', ()=> {

    // Will be changed once a better way of selecting these if found
    boxes[0] = document.querySelector("body > div > div > div:nth-child(1) > div:nth-child(1)");
    boxes[1] = document.querySelector("body > div > div > div:nth-child(1) > div:nth-child(2)");
    boxes[2] = document.querySelector("body > div > div > div:nth-child(1) > div:nth-child(3)");
    boxes[3] = document.querySelector("body > div > div > div:nth-child(2) > div:nth-child(1)");
    boxes[4] = document.querySelector("body > div > div > div:nth-child(2) > div:nth-child(2)");
    boxes[5] = document.querySelector("body > div > div > div:nth-child(2) > div:nth-child(3)");
    boxes[6] = document.querySelector("body > div > div > div:nth-child(3) > div:nth-child(1)");
    boxes[7] = document.querySelector("body > div > div > div:nth-child(3) > div:nth-child(2)");
    boxes[8] = document.querySelector("body > div > div > div:nth-child(3) > div:nth-child(3)");

    for(let i = 0; i < 9; i++){
        boxes[i].addEventListener("click", boxClicked)
    }
    announcement = document.getElementById("announcement")

    document.getElementById("reset_button").addEventListener("click", reset);
});

function boxClicked() {
    const box = this;
    if(box.innerText !== "") {
        box.innerText = "";
    } else {
        box.innerText = "X";
        box.removeEventListener("click", boxClicked);
        if(!checkWinLossState() && !checkTie()) {
            makeComputerMove(Math.floor(Math.random() * 9));
            checkWinLossState()
        }
    }
}

function checkWinLossState() {
    for(let i = 0; i < 8; i++) {
        if(boxes[winpatterns.at(i).at(0)].innerText === "X"
            &&  boxes[winpatterns.at(i).at(0)].innerText === boxes[winpatterns.at(i).at(1)].innerText
            && boxes[winpatterns.at(i).at(1)].innerText === boxes[winpatterns.at(i).at(2)].innerText){
            onWin()
            return true;
        }
        if(boxes[winpatterns.at(i).at(0)].innerText === "O"
            &&  boxes[winpatterns.at(i).at(0)].innerText === boxes[winpatterns.at(i).at(1)].innerText
            && boxes[winpatterns.at(i).at(1)].innerText === boxes[winpatterns.at(i).at(2)].innerText){
            onLoss()
            return true;
        }
    }
    return false;
}

function checkTie() {
    for( let i = 0; i < 9; i++) {
        if(boxes[i].innerText === "") {
            return false;
        }
    }
    onTie()
    return true;
}

function onWin() {
    for(let i = 0; i < 9; i++) {
        boxes[i].removeEventListener("click", boxClicked);
    }
    announcement.innerText = "You Win";
}

function onLoss() {
    for(let i = 0; i < 9; i++) {
        boxes[i].removeEventListener("click", boxClicked);
    }
    announcement.innerText = "You Lose";
}
function onTie() {
    announcement.innerText = "Tie";
}
function makeComputerMove(boxNum) {
    if (boxNum === 9) {
        makeComputerMove(0);
    } else {
        if (boxes[boxNum].innerText !== "") {
            if (boxNum === 8) {
                makeComputerMove(0);
            } else {
                makeComputerMove(boxNum + 1);
            }
        } else {
            boxes[boxNum].innerText = "O";
            boxes[boxNum].removeEventListener("click", boxClicked);
        }
    }
}

function reset() {
    for(let i = 0; i < 9; i++){
        boxes[i].innerText = "";
        boxes[i].addEventListener("click", boxClicked)
    }
    announcement.innerText = "";
}