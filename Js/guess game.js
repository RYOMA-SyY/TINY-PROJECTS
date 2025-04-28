// slicing strings
// const fullName = "Bro Code";
// let firstName = fullName.slice(0, 3); // Bro
// let lastName = fullName.slice(4); // Code
// console.log(firstName);
// console.log(lastName);



// using multiple methodes once
// let user = window.prompt("Enter your name: ");

// user = user.trim().charAt(0).toUpperCase() + user.trim().slice(1).toLowerCase();
// console.log(user);





//simple guessing game
const min = 1;
const max = 100;
const answer = Math.floor(Math.random() * (max - min + 1)) + min ;

let attempts = 0;
let guess;
let exe = true;

while(exe){
    guess = window.prompt(`guess a number ${min} - ${max} `);
    guess = Number(guess);
    if(isNaN(guess)){
        window.alert("Please enter a number");
    }
    else if(guess < min || guess > max){
        window.alert("Please enter a valide number");

    }
    else {
        attempts++;
        if(guess < answer){
            window.alert("Too low !!");
        }
        else if (guess > answer){
            window.alert("Too High !!");
        }
        else{
            window.alert(`CORRECT it was ${answer} tooks u ${attempts}`);
            exe = false;
        }
    }



    
}
