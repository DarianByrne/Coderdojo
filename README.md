# CoderDojo Projects

This repository contains a collection of projects I worked on during my time at CoderDojo in 2022. These projects were created to learn and practice programming concepts in Python while having fun building games and applications. Unfortunately, I don't have access to copies of my work from other years. We didn't have time to finish Top Trumps.
I decided to try having fun with "vibe coding" the rest of the Top Trumps game. I had to steer it a lot but overall the game works well with some small bugs I might not have found. The new characters in marvel.yaml are from the AI, I chose not to edit it's output. The chat log is included at [chat.md](/chat.md).

## Projects

### 1. **Hangman**

A Python implementation of the classic word-guessing game "Hangman." Players try to guess a secret word within a limited number of attempts.

- **Features**:

  - Random word selection from a word list.
  - Tracks guessed letters and remaining attempts.
  - Simple command-line interface.

- **How to Run**:

  1. Navigate to the `Hangman` directory.
  2. Run the game:
     ```bash
     python main.py
     ```

- **Files**:
  - [main.py](/Python/Projects/Hangman/main.py): Core game logic.
  - [words.txt](/Python/Projects/Hangman/words.txt): Word list for the game, sourced from [MichaelWehar/Public-Domain-Word-Lists](https://github.com/MichaelWehar/Public-Domain-Word-Lists/blob/master/5000-more-common.txt)
  - [test.py](/Python/Projects/Hangman/test.py): Unit tests for the game.

---

### 2. **TopTrumps**

An unfinished Python implementation of the classic card game "Top Trumps." Players can choose between different decks (e.g., Marvel Heroes or Villains) and compete by selecting stats to win cards.

- **Features**:

  - Custom decks with stats for heroes and villains.
  - AI and human players.
  - YAML configuration for deck customization.

- **How to Run**:

  1. Navigate to the `TopTrumps` directory.
  2. Install dependencies:
     ```bash
     python -m pip install -U pip setuptools wheel
     python -m pip install .
     ```
  3. Run the game:
     ```bash
     python -m toptrumps.app
     ```

- **Files**:
  - [top_trumps.py](/Python/Projects/TopTrumps/toptrumps/top_trumps.py): Core game logic and classes.
  - [marvel.yaml](/Python/Projects/TopTrumps/toptrumps/config/marvel.yaml): Configuration for Marvel decks.
  - [marvel_game.py](/Python/Projects/TopTrumps/toptrumps/base_decks/marvel_game.py): Marvel-specific deck implementation.

---

### 3. **Test**

A simple Python script to practice loops and functions.

- **How to Run**:
  1. Navigate to the `Test` directory.
  2. Run the script:
     ```bash
     python index.py
     ```

---

## About CoderDojo

[CoderDojo](https://coderdojo.com/) is a global movement of free, volunteer-led, community-based programming clubs for young people. At CoderDojo, young people learn how to code, develop websites, apps, games, and more in a fun and social environment.

This repository reflects the skills and projects I developed during my time at CoderDojo in 2022.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.

## AI Disclosure

Code in this repository is written by Darian Byrne. This README was generated with the help of GitHub Copilot running GPT-4o. Some implementation in this branch was made by GitHub Copilot running GPT-4o.
