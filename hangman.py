import random

# Step 1: Define a list of 5 words
word_list = ['apple', 'train', 'cloud', 'house', 'plant']

# Step 2: Randomly choose a word from the list
secret_word = random.choice(word_list)

# Step 3: Initialize variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Step 4: Create a display version of the word with underscores
display_word = ['_' for _ in secret_word]

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Step 5: Game loop
while incorrect_guesses < max_attempts and '_' in display_word:
    print("\nWord:", ' '.join(display_word))
    print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
    guess = input("Enter a letter: ").lower()

    # Validate input
    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Incorrect guess.")
        incorrect_guesses += 1

# Step 6: End of game
if '_' not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 Game over! The word was:", secret_word)
