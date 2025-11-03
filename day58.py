print("Palindrone checker")



while True:
    word = input("Enter a word: ")
    new = word[: :-1]

    if new == word:
        print("Yay this word is a palindrone!")
    
    else:
        print("This word is not a plaindrone :(")


    goAgain = input("DO you want to check if another word is a plaindrone?").strip().lower()
    if goAgain == "y":
        continue
    else:
        break


print("Thank you for playing")