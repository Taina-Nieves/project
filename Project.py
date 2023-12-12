import turtle as t
import random

class CategoryGenerator:
    def __init__(self):
        self.category = None

    def getCatWord(self):
        print("Choose a category to guess a word from!")
        self.category = input("Enter either USA cities, Continents, or Countries: ").lower()

        try:
            if self.category == "usa cities": 
                cities = ["newyork", "losangeles", "chicago", "miami" ,
                        "houston", "dallas", "albany", "orlando", "boston", "colorado",
                        "stamford", "newark", "tampa", "honolulu", "cambridge", "buffalo"]
                word = random.choice(cities)
                return word
        
            elif self.category == "continents":
                continents =  ["northamerica", "southamerica", "europe", "asia",
                            "africa", "australia", "antartica"]
                word = random.choice(continents)
                return word

            elif self.category == "countries":
                americas_countries = ["usa", "canada", "mexico", "brazil", "guatemala",
                                    "argentina", "ecuador", "bolivia", "colombia", "peru",
                                    "panama", "venezuela", "honduras", "belize", "barbados"]
                word = random.choice(americas_countries)
                return word
            else:
                print("Invalid choice, try again")
                return None
                
        except TypeError:
            print("Invalid category, try again")




               
class Hangman():
    def __init__(self):
        self.word_generator = CategoryGenerator()  
        self.word = self.word_generator.getCatWord()
        self.guessed_letters = set()
        self.wrong_guesses = 0

    def display_word(self):
        display_word = ""
        for i in self.word:
            if i in self.guessed_letters:
                display_word += i
            else:
                display_word += "_"
        return display_word
    
    def guess(self, letter):
        if letter in self.guessed_letters:
            print("You already guessed that letter. Try again.")
        elif letter in self.word:
            self.guessed_letters.add(letter)
            print("Correct!")
        else:
            self.wrong_guesses += 1
            self.draw_hangman()
            print("Incorrect!")

    def draw_hangman(self):
        if self.wrong_guesses == 1:
            # head
            t.penup()
            t.goto(0, 170)
            t.pendown()
            t.circle(40) 
        elif self.wrong_guesses == 2:
            # body
            t.pendown()
            t.left(90)
            t.backward(80) 
            t.forward(40) 
        elif self.wrong_guesses == 3:
            # left arm
            
            t.left(45)
            t.forward(40)   
        elif self.wrong_guesses == 4:
            # right arm
            
            t.backward(40)  
            t.right(90)
            t.forward(40) 

        elif self.wrong_guesses == 5:
            # right leg
            
            t.backward(40)  
            t.left(225)
            t.forward(40)
            t.right(45)
            t.forward(60) 
            
        elif self.wrong_guesses == 6:
            # left leg
            t.backward(60) 
            t.left(90) 
            t.forward(60)  
            t.hideturtle()
            t.done()
    
    def is_game_over(self):
        if self.wrong_guesses >= 6:
            print("You ran out of guesses. The word was:", self.word)
            return True
        elif set(self.guessed_letters) == set(self.word):
            print("You guessed the word! It is:", self.word)
            return True
        else:
            return False
        
    def play(self):
        while self.is_game_over() == False:
            letter = input("Enter letter: ")
            self.guess(letter)
            print("Current word:", self.display_word())


class Challange(Hangman):
    def __init__(self):
        super().__init__()

    def guess_word(self,guess):
        if guess.lower() == self.word.lower():
            print("Congratulations! You guessed the word:", self.word)
            t.clear()
            return True
        elif len(guess) != len(self.word):
            print("You entered the wrong amount of letters! Try again!")
            return False
        else:
            print("Incorrect! Keep guessing.")
            self.wrong_guesses += 1
            self.draw_hangman()
            return False

    def play(self):
        while self.is_game_over() == False:
            letter = input("Enter letter: ")
            self.guess(letter)
            print("Current word:", self.display_word())

            guess_word_option = input("Do you want to guess the whole word? (yes/no): ").lower()
            if guess_word_option == "yes":
                whole_word = input("Enter the whole word to guess: ")
                if self.guess_word(whole_word):
                    break


if __name__ == "__main__":
    while True:
        print("Welcome to Hangman!")
        print("1. Play Hangman: only letters")
        print("2. Play Hangman: letters and whole word")
        print("3. Quit")

        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                game = Hangman()
                game.play()
            elif choice == 2:
                challenge_game =  Challange()
                challenge_game.play()
            elif choice == 3:
                print("Ending game")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

