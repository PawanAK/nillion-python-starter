# Secure Guessing Game using Nada DSL

This project implements a simple guessing game using the Nada Domain-Specific Language (DSL) for secure multi-party computation. The game allows a user to guess a number while maintaining privacy and security of inputs from all parties involved.

## Overview

The game involves three parties:
1. User: Provides a guess
2. Computer: Contributes to the random number generation
3. Game Master: Manages the game state

The goal is for the user to guess a number that matches one of the secret seeds provided by the parties. The game maintains a score and determines when the game is over, all while keeping the inputs private.

## How It Works

1. Each party (User, Computer, and Game Master) provides a secret seed number between 1 and 5.
2. The user provides their guess (also between 1 and 5).
3. The program combines the seeds to create a pseudo-random number.
4. The user's guess is compared against each individual seed.
5. If the guess matches any seed, the game ends. Otherwise, the score increases.


## Setup and Running

1. Ensure you have the Nada DSL environment set up.
2. Place the code in a file named `main.py` in your Nada project directory.
3. Run the Nada compiler on your code.

## Inputs

- **UserGuess**: The user's guess (1-5)
- **Seed1**: Secret seed from User (1-5)
- **Seed2**: Secret seed from Computer (1-5)
- **Seed3**: Secret seed from Game Master (1-5)
- **CurrentScore**: The current game score

## Outputs

- **ComputerNumber**: The combined seed (for transparency)
- **NewScore**: The updated score after this round
- **GameOver**: Flag indicating if the game has ended (0 if game over, non-zero if continuing)

## Security Features

- All inputs are treated as secret integers, ensuring privacy.
- The game logic is performed on encrypted data, revealing only the necessary outputs.
- No single party can determine the final "random" number on their own.

## Limitations

- The random number generation is simplified and may not provide uniform distribution.
- The game relies on honest participation from all parties.

## Future Improvements

- Implement a more sophisticated random number generation method.
- Add additional game features or complexity while maintaining security.
