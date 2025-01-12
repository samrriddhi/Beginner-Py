import random

word_bank = ["Cow", "Buffalo", "Lion", "Elephant", "Giraffe", "Horse", "Pig", "Goat"]
word = random.choice(word_bank).lower()  
attempts = 10
guessed_word = ['_'] * len(word)  

print("Welcome to the Guess The Word game!")
print(f"Your word has {len(word)} letters in it.")

while attempts > 0:
    print("\nCurrent word: " + ' '.join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_word:
        print("You already guessed that letter!")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("You have correctly guessed the letter!")
    else:
        attempts -= 1
        print(f"Wrong guess. Attempts left: {attempts}")

    if '_' not in guessed_word:
        print(f"Congratulations! You won. You guessed the word: {word}")
        break
else:
    print(f"You ran out of attempts. The word was: {word}.")
