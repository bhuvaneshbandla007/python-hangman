import random

# Predefined list of words
words = ["python", "hangman", "random", "string", "loops"]

# Randomly choose a word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman!")
print("Instructions:")
print("-> Guess the hidden word one letter at a time.")
print("-> You have 6 wrong guesses before the game ends.")
print("-> Type a single letter and press Enter.")
print("-> If you reveal all letters, you win!")

print("Guess the word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in used_letters:
        print("You already tried that letter.")
        continue

    used_letters.append(guess)

    if guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    print("Word:", " ".join(guessed))
    print("Used letters:", ", ".join(used_letters))

# End of game
if "_" not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over! The word was:", word)
