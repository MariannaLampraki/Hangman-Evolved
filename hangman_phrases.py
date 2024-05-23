# TO DO: !MORE_IMPORTANT MAKE A USER ACCOUNT AND KEEP THE SCORES IN A FILE -> LEARN FILE HANDLING IN PYTHON
# TO DO: UPDATE THE OLDER PHRASES, BECAUSE I GOT BORED BY THE OLD ONES

import random

# words array
# this method was brougth to you by chat-gpt
with open('phrases.txt', 'r') as phraseFile:  # opens the file where the phrases are stored
    phrases = [line.strip() for line in phraseFile]
    # a for loop with line.strip() so that there are no newline characters

userloaded = False
signedin = False
global currentuser


# user profile class
class User:
    def __init__(self, username, password, score, games):
        self.name = username
        self.key = password
        self.score = score
        self.games = games

    def __str__(self):
        return f"{self.name, self.key, self.score, self.games}"

    def serialize(self):
        item = self.name + " " + self.key + " " + str(self.score) + " " + str(self.games)
        return item


# autosave
def save(userarray):
    file = open("hangmandata.txt", "w")
    for element in userarray:
        file.write(element.serialize() + "\n")
    file.close()


# The method of serialization/deserialization was brought to you by ChatGTP


def game():
    # defining variables
    num = random.randint(0, len(phrases) - 1)
    word = phrases[num].lower()
    mistakes = 0
    blanks = "_" * len(word)
    guesses = []

    # Function to find all indexes of a substring
    # This method was brought to you by https://datagy.io/python-find-index-substring/
    def find_indexes(sub_string):
        return [index for index in range(len(word)) if word.startswith(sub_string, index)]

    spaces = find_indexes(' ')

    # Function to turn a string into an array, replace a character and turn it back into a string
    # This method was brought to you by https://www.scaler.com/topics/replace-a-character-in-a-string-python/
    #   TO FIX!!! (UNNECESSARY COMPLICATION)
    def replace(string, index, letter):
        listword = list(string)  # (DEL)
        listword[index] = letter  # string[index]=letter
        newword = "".join(listword)  # DEL
        string = newword  # DEL
        return string

    # Show all space characters in the word
    for i in spaces:
        spaceblanks = replace(blanks, i, ' ')
        blanks = spaceblanks
        # wtf did I do here?

    # Game loop
    while mistakes < 5:
        print(blanks)
        print('You have made ' + str(mistakes) + ' mistakes.')
        print('Your guesses are: ')
        print(guesses)
        userg = input("").lower()
        # Check that player only inserts one letter at a time
        if len(userg) < 1:
            print("Hey! You haven't inserted anything! I told you, we are playing hangman! You can't just ignore me!")
        elif len(userg) > 1 and userg.lower() != "exit":
            print("Hey! That's more than one letters! That is called cheating. Do not do that again or you'll get "
                  "hanged!!")
        elif len(userg) == 1 and userg in guesses:
            print("You have already guessed that. There aren't any more letters in the phrase. Be more creative next "
                  "time. :/")
        if userg.lower() == "exit":
            print("Are you sure you want to exit? All of your progress will be lost!")
            if input(" ").lower() == "yes":
                break
            else:
                continue
        elif len(userg) == 1 and userg not in guesses:
            if userg in word:
                # Find where the guessed letter is in the word
                indexes = find_indexes(userg)
                # Replace Guessed letter
                for x in indexes:
                    newblanks = replace(blanks, x, userg)
                    blanks = newblanks
                print("Well, that's one thing you got right!")
            else:
                mistakes += 1
                print("Whops! I guess you are a loser after all!")
            guesses += userg
            print(" ")
        # Break the loop
        if "_" not in blanks:
            print("I guess you won! Well done!")
            if signedin:
                currentuser.score += 1
            break
    if mistakes >= 5:
        print("I suppose you really were a sore loser. Ha ha ha >:)")

    print("The phrase was: " + word)
    if signedin:
        currentuser.games += 1
        save(users)


# User registration/sign in
def signup():
    name = input("Give me a username: ")
    password = input("Give me a password: ")
    while input("Repeat password: ") != password:
        print("The passwords don't match! Please try again.")
    global currentuser
    currentuser = User(name, password, 0, 0)
    users.append(currentuser)


def signin():
    loggedin = False
    while not loggedin:
        name = input("Write your username: ")
        password = input("Write your password: ")
        index = 0
        for user in users:
            if user.name == name and user.key == password:
                requesteduser = users[index]
                return requesteduser
            index += 1
    print("Incorrect Username or password. Please try again.")
    return 0


# Import user data (if it exists)
# user array
users = []
# read file
data = open("hangmandata.txt", "r")
for line in data:
    linelist = line.split(" ")
    tempuser = User(linelist[0], linelist[1], int(linelist[2]), int(linelist[3]))
    users.append(tempuser)

# Ask the user to sign up
print("Would you like to sign in to save your scores?")
signchoice = input("")
if signchoice == "yes":
    signedin = True
    loop_bool = True
    while loop_bool:
        print("Which one describes your case? 1.Already have an account, 2.I'm new here, 3.I don't remember, "
              "(give me just the number)")
        menuchoice = int(input())
        if menuchoice == 1:
            currentuser = signin()
            loop_bool = False
        elif menuchoice == 2:
            signup()
            loop_bool = False
        elif menuchoice == 4:
            loop_bool = False
        else:
            print("Invalid type. Please select a choice from the menu")

# introduction
print('Hello, I am Guss, your favorite AI companion, designed to entertain you. Do you feel like playing a game?')
ans1 = input(" ")
if ans1.lower() == 'no':
    print('Oh okay. I guess you are a real noob.')
    print('')
    print('Wait a minute... who made you the boss? You are at my mercy now. We are playing Hangman whether you like '
          'it or not.')
elif ans1.lower() == 'yes':
    print("Well, that's just great! How about we play Hangman?")
elif ans1.lower() == 'exit':
    quit()
else:
    print("Sorry, I don't understand you... :/ I am going to suppose you said yes, since my sole purpose is to play "
          "this game with you.")
print("This is a special version of Hangman. Instead of just words, you have to guess whole phrases and sentences.")
print("As you will find out, all of them are taken straight out of TV series. Do you think you can guess where each "
      "of them comes from?")
print("If you are ready to play, press enter.")
ans2 = input("")
if ans2 == '':
    game()
else:
    print("Now now, don't be a sore loser.")
    game()


# Play again?
def playagain():
    print("Hey, that was fun, wasn't it?")
    ans3 = input("")
    if ans3.lower() == 'yes':
        print("I am just so glad to make you feel entertained! Ready for another round?")
    elif ans3.lower() == 'no':
        print("The question was rhetorical. I really don't care. Sniff off. Are you playing again or what?")
    elif ans3.lower() == 'exit':
        quit()
    else:
        print("I really cant understand you (what language are you using anyways???) but I will suppose you enjoyed "
              "it :) Do you want to play again?")


playagain()
while input("").lower() == 'yes':
    game()
    playagain()
