// start screen off with this
fetchWord()

// fetches a word and its two definitions 
function fetchWord() {
    // uses fetch API to get the data from /get_word endpoint
    fetch('/get_word')
        .then(response => response.json()) // parsing as json
        .then(data => {
            // gets the html element with id word
            const wordElement = document.getElementById('word');
            // sets the elements text content to the word we just got
            wordElement.textContent = data.word;

            // gets html element for choices and displays it
            const choicesDiv = document.getElementById('choices');
            choicesDiv.style.display = 'block';

            // creates and poppulates array with right and wrong anser
            const choices = [data.definition, data.incorrect_definition]; 
            // shuffles which is which
            choices.sort(() => Math.random() - 0.5);

            // gets html element for buttons
            const choiceA = document.getElementById('choiceA');
            const choiceB = document.getElementById('choiceB');

            // sets elements text content to the shuffles choices
            // [0] and [1] are the two choices which were shuffled about
            choiceA.textContent = choices[0];
            choiceB.textContent = choices[1];

            // click event handlers for both buttons
            choiceA.onclick = () => checkAnswer(choiceA, data.definition);
            choiceB.onclick = () => checkAnswer(choiceB, data.definition);
        })
        .catch(error => console.error('Error fetching word:', error));
}

// here we check if they are correct
function checkAnswer(button, correctDefinition) {
    // if they chose right
    if (button.textContent === correctDefinition) {
        alert('Correct answer');
        // if they chose wrong
    } else {
        // giving them the right answer now
        alert('Incorrect answer, the correct answer is: ' + correctDefinition);
    }
    // gets a new word so we can continue
    fetchWord(); 
}


