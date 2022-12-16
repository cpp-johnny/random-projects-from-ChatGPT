#include <iostream>
#include <string>

int main() {
  // Set up the game
  const int MAX_WRONG_GUESSES = 6;  // Maximum number of wrong guesses allowed
  std::string word;  // The word to be guessed
  std::string used;  // The letters that have been used
  int wrong;  // The number of wrong guesses so far

  // Get the word to be guessed
  std::cout << "Enter the word to be guessed: ";
  std::cin >> word;

  // Initialize the game state
  used = "";
  wrong = 0;

  // Main game loop
  while (wrong < MAX_WRONG_GUESSES) {
    // Display the current state of the game
    std::cout << "You have used the following letters:\n" << used << std::endl;
    std::cout << "You have made " << wrong << " wrong guesses." << std::endl;
    std::cout << "The word is:\n";
    for (int i = 0; i < word.length(); i++) {
      if (used.find(word[i]) != std::string::npos) {
        std::cout << word[i];
      } else {
        std::cout << "_";
      }
    }
    std::cout << std::endl;

    // Get the next guess
    std::cout << "Enter your next guess: ";
    char guess;
    std::cin >> guess;

    // Check if the guess is valid
    if (used.find(guess) != std::string::npos) {
      std::cout << "You have already used that letter. Try again." << std::endl;
      continue;
    }
    used += guess;

    // Check if the guess is correct
    if (word.find(guess) != std::string::npos) {
      std::cout << "That's correct!" << std::endl;

      // Check if the player has won
      bool won = true;
      for (int i = 0; i < word.length(); i++) {
        if (used.find(word[i]) == std::string::npos) {
          won = false;
          break;
        }
      }
      if (won) {
        std::cout << "Congratulations, you won!" << std::endl;
        return 0;
      }
    } else {
      std::cout << "Sorry, that's incorrect." << std::endl;
      wrong++;
    }
  }

  // The player has lost
  std::cout << "You have lost. The word was " << word << "." << std::endl;
  return 0;
}
