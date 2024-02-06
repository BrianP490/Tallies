//-------------GLOBAL VARIABLES-------------//
const button = document.querySelector('.button');   //links the html button to a variable; used to initiate or replay the game
const text = document.querySelector('.text');   //links the html text div to a variable; used to display instructions
const Spaces = ["","","","","","","","",""]; //initializes spaces array of the game board 
let GameComplete = false;   // Variable that stores the current game completion state
let round = 0; //Variable that keeps track of the round number. After the 9th round, the game stops
let player = "";        //Will store the current player X or O
let elem="";    //Variables for the GameReset function
let e = "";     //Stores the selected box object
let boxes = Array.from(document.getElementsByClassName('box')); //used to add/remove event listeners from clicked board squares


//-------------HELPER FUNCTIONS-------------//

//Use: to generate either a 0 or a 1 randomly
function randomIntFromInterval(min, max) { // min and max included
    return Math.floor(Math.random() * (max - min + 1) + min);
}

//Use: helper function that determines the starting player X or O using the random number generator
function determineStartingPlayer(){
    //Randomly decides generates either a 0 or 1
    var num = randomIntFromInterval(0,1);//store the return into the variable num
    if( num.toString() === "1")
        player="X";
    else
        player="O";
}

//Function: resets game values and data
function GameReset(){
    GameComplete = false;       // the game conditional loop token

    button.classList.remove("fadeIn", "fadeOut");   //clear button animations

    text.classList.remove('slideUp', 'slide');  //clear instruction animations

    // player = "";

    round = 0;      //resets the round counter

    //clears the contents of the TTT game squares
    for(let i = 0; i < 9; i++){
        try{boxes[i].removeEventListener('click', addGo);}      //remove the event listener from the current TTT slot
        catch{console.log("remove didn't work for i ="+i)}

        elem = document.getElementById(i);      

        if (elem.classList.contains('Oclass')) {
            elem.classList.remove('Oclass');
        }
        else{
            elem.classList.remove('Xclass');
        }

        elem.innerHTML = "";
        elem.classList.remove("enlargedText");          //remove the class from the TTT square
    }

    Spaces.fill(null);  //clears the Spaces array
}

//Function that changes to the other player
function changePlayer(){
    if(player === "X")
        player = "O";
    else
        player = "X";
}

//Function that increases the current round counter
function incRound(){
    round++;}

//Function: Adds the currents player's styled icon to the selected TTT box
function updateBox(e){
    e.target.innerText= player;     //assign the current TTT box to the current player ; add text to declare player's spot
    if(player === "X")
        e.target.classList.add('Xclass', 'enlargedText');
    else
        e.target.classList.add('Oclass', 'enlargedText');
}

//Function: Updates the Spaces array of the board
function updateSpaces(e){
    Spaces[e.target.id] = player;
}

//Function: starts the TTT game
function AddButton(){

    //add an event listener to the on-screen button. On the botton click, the game starts
    button.addEventListener('click', function()
    {
        console.log(" button called");      //debug output to console

        //if the button has the class fadein the game was restarted by button-press
        if (button.classList.contains('fadeIn')) {
            GameReset();    //call reset game function
          }

        button.classList.add('fadeOut');    // add animation to the button to fade out of the screen
        text.classList.add('slide');    // add animation to the text prompt to slide down vertically

        determineStartingPlayer();  //determine the starting player

        playGame();

        try {
            button.removeEventListener('click', function(){});
        } catch (error) {
            console.log("button event listener removal error");
        }
    });
}

//Function: initialize boxes with round 1 message
function playGame(){
    //-------Update game-----
    //output ON-SCREEN message and add event listener to each TTT square
    if(round === 0){
        text.innerHTML = "Get 3 in a sequence to Win!!! " + player + " goes first.";

        boxes.forEach(box => box.addEventListener('click', addGo));  
    }
    else
        ;
}

//Function: updates the game space and determines whether or not the game is won ; ADD up the Win conditions and GO to the next state
function addGo(e){
    //remove clicking event from selected button
    try{boxes[e.target.id].removeEventListener('click', addGo);}
    catch{console.log("addGo remove event Listener didn't work")}
 
    updateBox(e);           //fill in selected box with user icon
 
    updateSpaces(e);        //update Spaces array
 
    //stop the Game??? 
    if(round >= 4){
        GameComplete = WinCondition(); //Determines if any player won
    }
    if( GameComplete ){
        //player has 3 in succession, quit game
        //print game winner to the screen
        text.innerHTML = "Player " + player + " has won the game with 3 in succession!!!";
    }
    if( !GameComplete && round === 8){//no more space to play
        //quit game
        GameComplete = true;
        text.innerHTML =
        "The Game Results in a Tie,";   //show on-screen tie message
    }
    
    if(GameComplete){   //Final Step of the Finished Game
        //slide up text
        text.classList.add('slideUp');
        
        button.classList.add('fadeIn');     //  make the button reappear
        setTimeout(function() {
            console.log("BYE BYE");         //debug console msg
            // AddButton();
            }, 1000);
        return;     //quits the game, but gives players the reset button option

    }
    //continue with the game by updating parameters
    else{
        changePlayer();     //change current player
        incRound();     //increase the round counter  
        text.innerHTML = player + "'s turn. Click on an empty square:"; //update instructions
    }
}

//check if a player won by checking if the player has 3 in a row, column, or diagonal; otherwise continue playing by returning false
function WinCondition(){
    //row check
    if( player === Spaces[0] && Spaces[0] === Spaces[1] && Spaces[1] === Spaces[2])
        return true;
    else if(player === Spaces[3] && Spaces[3] === Spaces[4] && Spaces[4] === Spaces[5] )
        return true;
    else if( player === Spaces[6] && Spaces[6] === Spaces[7] && Spaces[7] === Spaces[8] )
        return true;
    //diagonals

    else if( player === Spaces[0] && Spaces[0] === Spaces[4] && Spaces[4] === Spaces[8])
        return true;
    else if( player === Spaces[2] && Spaces[2] === Spaces[4] && Spaces[4] === Spaces[6] )
        return true;
    //column check
    else if( player === Spaces[0] && Spaces[0] === Spaces[3] && Spaces[3] === Spaces[6])
        return true;
    else if( player === Spaces[1] && Spaces[1] === Spaces[4] && Spaces[4] === Spaces[7])
        return true;
    else if( player === Spaces[2] && Spaces[2] === Spaces[5] && Spaces[5] === Spaces[8])
        return true;

    //game continues otherwise
    else
        return false;
}

//Main Function that Starts Game
AddButton();
