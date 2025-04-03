// These are the main variables that keep track of the game state
let correctColor;  // Stores the color that the player needs to guess
let lives = 3;     // How many chances the player has left
let score = 0;     // How many points the player has earned

// This function creates a random color by mixing red, green, and blue
function getRandomColor() {
    const r = Math.floor(Math.random() * 256);  // Random number between 0 and 255 for red
    const g = Math.floor(Math.random() * 256);  // Random number between 0 and 255 for green
    const b = Math.floor(Math.random() * 256);  // Random number between 0 and 255 for blue
    return {r, g, b};  // Returns the color as an object with r, g, and b values
}

// This is the main function that starts a new round of the game
function newGame() {
    // First, we clear any old color boxes from the previous round
    const colorOptions = document.getElementById('colorOptions');
    colorOptions.innerHTML = '';

    // We create a new color that the player needs to guess
    correctColor = getRandomColor();
    document.getElementById('rgbValue').textContent = 
        `RGB(${correctColor.r}, ${correctColor.g}, ${correctColor.b})`;

    // We create three color boxes: one correct color and two wrong colors
    const colors = [correctColor];  // Start with the correct color
    for (let i = 0; i < 2; i++) {
        colors.push(getRandomColor());  // Add two more random colors
    }

    // We mix up the colors so the correct one isn't always in the same place
    colors.sort(() => Math.random() - 0.5);

    // Now we create the color boxes that the player can click
    colors.forEach(color => {
        const box = document.createElement('div');
        box.className = 'color-box';
        box.style.backgroundColor = `rgb(${color.r}, ${color.g}, ${color.b})`;
        box.onclick = () => checkAnswer(color);  // When clicked, check if this is the right color
        colorOptions.appendChild(box);
    });
}

// This function checks if the player picked the right color
function checkAnswer(selectedColor) {
    // We check if the selected color matches the correct color exactly
    if (selectedColor.r === correctColor.r && 
        selectedColor.g === correctColor.g && 
        selectedColor.b === correctColor.b) {
        // If they're right, they get 10 points
        score += 10;
        document.getElementById('score').textContent = score;
        alert('Correct! Well done!');
    } else {
        // If they're wrong, they lose a life
        lives--;
        document.getElementById('lives').textContent = lives;
        alert('Wrong! Try again!');
        
        // If they run out of lives, the game is over
        if (lives <= 0) {
            alert('Game Over! Your final score: ' + score);
            lives = 3;  // Reset lives back to 3
            score = 0;  // Reset score back to 0
            document.getElementById('lives').textContent = lives;
            document.getElementById('score').textContent = score;
        }
    }
    // Start a new round no matter if they were right or wrong
    newGame();
}

// Start the game as soon as the page loads
newGame(); 