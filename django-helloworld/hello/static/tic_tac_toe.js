document.addEventListener('DOMContentLoaded', ()=> {

    const box1 = document.querySelector("body > div > div > div:nth-child(1) > div:nth-child(1)");
    const box2 = document.querySelector("body > div > div > div:nth-child(1) > div:nth-child(2)");
    const box3 = document.querySelector("body > div > div > div:nth-child(1) > div:nth-child(3)");
    const box4 = document.querySelector("body > div > div > div:nth-child(2) > div:nth-child(1)");
    const box5 = document.querySelector("body > div > div > div:nth-child(2) > div:nth-child(2)");
    const box6 = document.querySelector("body > div > div > div:nth-child(2) > div:nth-child(3)");
    const box7 = document.querySelector("body > div > div > div:nth-child(3) > div:nth-child(1)");
    const box8 = document.querySelector("body > div > div > div:nth-child(3) > div:nth-child(2)");
    const box9 = document.querySelector("body > div > div > div:nth-child(3) > div:nth-child(3)");

    box1.addEventListener("click", boxClicked);
    box2.addEventListener("click", boxClicked);
    box3.addEventListener("click", boxClicked);
    box4.addEventListener("click", boxClicked);
    box5.addEventListener("click", boxClicked);
    box6.addEventListener("click", boxClicked);
    box7.addEventListener("click", boxClicked);
    box8.addEventListener("click", boxClicked);
    box9.addEventListener("click", boxClicked);
});

function boxClicked(event) {
    const box = this;
    if(box.innerText !== "") {
        box.innerText = "";
    } else {
        box.innerText = "X";
    }
}
document.querySelector("body > div > div > div:nth-child(1) > div:nth-child(2)")