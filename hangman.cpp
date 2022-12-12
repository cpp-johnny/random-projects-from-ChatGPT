#include <iostream>
#include <string>

// The word to be guessed
const std::string WORD = "hangman";

int main()
{
    // Initialize the game
    std::string word = WORD;
    std::string used = "";

    int lives = 6; // Number of lives

    // Keep playing as long as the player has lives left
    while (lives > 0)
    {
        // Show the word with letters that have been used
        for (char c : word)
        {
            if (used.find(c) != std::string::npos)
            {
                // The letter has been used, show it
                std::cout << c << " ";
            }
            else
            {
                // The letter has not been used, show a blank
                std::cout << "_ ";
            }
        }
        std::cout << std::endl;

        // Check if the player has won
        if (word == used)
        {
            std::cout << "You win!" << std::endl;
            break;
        }

        // Prompt the player for a letter
        std::cout << "Enter a letter: ";
        char letter;
        std::cin >> letter;

        // Check if the letter is in the word
        if (word.find(letter) == std::string::npos)
        {
            // The letter is not in the word, subtract a life
            lives--;
            std::cout << "Wrong! You have " << lives << " lives left." << std::endl;
        }
        else
        {
            // The letter is in the word, add it to the used letters
            used += letter;
        }
    }

    if (lives == 0)
    {
        std::cout << "You lose! The word was " << WORD << "." << std::endl;
    }

    return 0;
}
