import random

# list of words for guessing
words = ["python", "developer", "program", "hangman", "beautiful", "computer"]

# randomly choose a word
word = random.choice(words)

# create blank spaces: _ _ _ _
guessed = ["_"] * len(word)

# number of wrong attempts allowed
attempts = 6

print("HANGMAN GAME STARTED!")
print("Guess the word:")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ")

    # check if letter is in the word
    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("❌ Wrong guess!")

# check win or lose
if "_" not in guessed:
    print("\n🎉 YOU WIN! The word was:", word)
else:
    print("\n💀 YOU LOST! The word was:", word)
