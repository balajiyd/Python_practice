secret_word = "red"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
print("Hint: Roses are ______")
while secret_word != guess and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the word: ").lower()
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, You Lose!")
else:
    print("YOu Win!!")
