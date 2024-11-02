# TO DO: !MORE_IMPORTANT MAKE A USER ACCOUNT AND KEEP THE SCORES IN A FILE -> LEARN FILE HANDLING IN PYTHON
# TO DO: UPDATE THE OLDER PHRASES, BECAUSE I GOT BORED BY THE OLD ONES
# TO DO: !IMPORTANT PUT THE PHRASES IN A FILE, THEN READ THE FILE AND SAVE EVERYTHING TO ARRAY (GET RID OF 150 USELESS LINES)

import random

# words array
phrases = [
    "I have got new kidneys! I do not like the color",
    "I am a high functioning sociopath",
    "Miss Hudson leave Baker street? England would fall!",
    "Humans. Are not. Otters.",
    "I did not know you could read",
    "It is called the Bootstrap paradox. Google it.",
    "Have you gone bananas?",
    "There is an escaped fish",
    "I. Am. An idiot!",
    "Shut up! Shut up! Shutity up up up!",
    "Anderson, don't talk out loud. You lower the IQ of the whole street.",
    "Miss Hudson took my skull",
    "Dear God, what is it like in your funny little brains? It must be so boring!",
    "Try not to start a war before I get home",
    "Do not rob a bank without me",
    "Oh, breathing. Breathing's boring.",
    "Stop! We can't giggle, it's a crime scene.",
    "We've got ourselves a serial killer. I love those. There's always something to look forward to.",
    "Heroes don't exist, and if they did, I wouldn't be one of them",
    "Ah, the wall had it coming",
    "John arrives home to find Sherlock shooting at a smiley on the wall",
    "Is that a gun in your pocket or are you just pleased to see me?",
    "There is a head in the fridge!",
    "The graves around you eat people",
    "The graves around you eat people",
    "A nice murder. That will cheer you up.",
    "I am Scottish, I can complain about things now!",
    "You sound the same, it's spreading. You all sound all English!",
    "This is your power source and feeble though it is, I can use it to blow this whole room if I see one thing that "
    "I don't like. And that includes karaoke and mime, so take no chances.",
    "I need clothes, that's what I need. And a big, long scarf. No, no, move on from that, it looked stupid.",
    "Ah, no sausages. And there's no pictures, either. Do you have a children's menu? Any specials?",
    "I hate being wrong in public, everybody forget that happened",
    "So you've got a whole room for not being awake in?",
    "Sorry, I was talking to the horse",
    "Is this how time normally passes? Really slowly, in the right order?",
    "What do you all have for brains, pudding?",
    "I always hear 'punch me in the face' when you're speaking, but it's usually sub-text",
    "Do you just carry on talking when I'm away?",
    "Please don't feel obliged to tell me that was remarkable or amazing. John's expressed that thought in every "
    "possible variant available to the English language.",
    "And exactly how many times did he fall out of the window?",
    "We solve crimes, I blog about it, and he forgets his pants. So I wouldn't hold out to too much hope.",
    "We are in Buckingham Palace, at the very heart of the British nation. Sherlock Holmes, put your trousers on!",
    "That's not the end of the world, that's Miss Hudson",
    "My only definite plan is that, in future, I'm definitely just using this screwdriver for screwing in screws",
    "Crime in Progress. Please Disturb.",
    "So if you have what you say you have, I will make you rich. If you don't, I'll make you into shoes.",
    "No, Sherlock always replies, to everything. He's Mr. Punchline. He will outlive God trying to have the last word.",
    "I dislike being outnumbered. It makes for too much stupid in the room.",
    "You're not my boss, you're one of my hobbies",
    "You'd starve to death trying to find the light switch",
    "Don't be lasagna",
    "If there's one thing I can't stand, it's a unpunctual alien attack",
    "Well, they call me the Doctor. I don't know why. I call me the Doctor too. I still don't know why.",
    "Sorry, wrong day to die",
    "I don't need a sword. Because I am the Doctor. And this is my spoon.",
    "You're as pale as milk. It's the way with Scots, they're strangers to vegetables.",
    "If I wanted poetry, I'd read John's emails to his girlfriends",
    "Did we just break into a military base to investigate a rabbit?",
    "Now shut up and smoke",
    "Well, that's a few years of my life I'll be needing back",
    "People don't need to be scared by a big gray-haired stick insect but here you are",
    "Why do you have three mirrors? Why don't you just turn your head?",
    "Phone Lestrade, tell him there's an escaped rabbit",
    "I'll let you know next week's lottery numbers",
    "I was hoping for minimalism, but I think I came out with magician",
    "Don't be so pessimistic, it'll affect team morale",
    "Basically, it's the eyebrows",
    "My personal plan is that a thing will probably happen quite soon",
    "We found these amazing worms!",
    "Don't rob any banks without me",
    "I want to kiss him to death",
    "Why have you got two jackets? Is one of them faulty?",
    "Apparently it's against the law to chin the Chief Superintendent",
    "We met twice, five minutes in total. I pulled a gun. He tried to blow me up. I felt we had a special something.",
    "Nobody can fake being such an annoying dick all the time",
    "Tell me what you knew, Doctor, or I'll smack you so hard you'll regenerate",
    "The moon is hatching!",
    "One small thing for a thing. One enormous thing for a thingy-thing.",
    "Don't let it get to you, I always feel like screaming when you walk into a room. In fact, so do most people.",
    "Falling's just like flying except there's a more permanent destination",
    "Hello. I'm so pleased to finally see you. I'm the Doctor and I will be your victim this evening. Are you my mummy?"
    "",
    "A mystery shopper. Oh, great.",
    "I could do with an extra pillow and I'm very disappointed with your breakfast bar and all the dying.",
    "Now, shut up and give me some planets",
    "Who knows? Some of you may even survive the trip.",
    "We're not calling it a de-flattener!",
    " I don't mean edible pie, I mean circular pi, which I also realise would be the edible pie, anyway",
    "It takes quite a lack of imagination to beat psychic paper",
    "Oh, please. Killing me, that's so two years ago.",
    "Yes, well, there are some things that I've never seen, but that's usually because I've chosen not to see them. "
    "Even my incredibly long life is too short for Les Miserables.",
    "Why are you asking me all the questions? Give someone else a go.",
    "Well, anybody who wears a hat as stupid as this isn't in the habit of hanging around other people, is he?",
    "Madam, can I suggest you look at this menu? It's, uh, completely identical.",
    "Hello. How may I assist you with your death?",
    "Cybermen don't just blow themselves up for no good reason, dear. They're not human.",
    "I'm going to kill you in a moment",
    "Imagine someone's going to get murdered at a wedding. Who exactly would you pick?",
    "There's a horror movie called Alien? That's really offensive. No wonder everyone keeps invading you.",
    "There's a skeleton man and a girl in a nightie!",
    "We are just three passing perfectly ordinary roof people, doing some emergency roof things",
    "Yeah, your mum and dad, one day a year, for no particular reason, just out of the blue, suddenly decide to give "
    "you a great big pile of presents",
    "Well, that's a bit rude, coming from a magician",
    "If either of you use my name again, I will remove your organs in alphabetical order. Any questions?",
    "My back's playing up. It simply refuses to carry the weight of an entirely pointless stratum of society who "
    "contribute nothing of worth to the world and crush the hopes and dreams of working people.",
    "I think I'm going to need a bigger flowchart",
    "I'm an archaeologist from the future. I dug you up.",
    "We're being threatened by a bag! By a head in a bag!",
    "You are a time-space machine. You're a vehicle! I've never asked you to cheer me up with hologrammatic antlers!",
    "Don't hush me. I'm not a hushing person.",
    "I'm never sure. I don't like being sure about things. One minute you're sure, the next everybody turns into "
    "lizards and a piano falls on you.",
    "What's that face? Are you thinking? Stop it. You're a man, it looks weird.",
    "Cheer up, get a saw, I'll kill the lights, you kill the patient. I employed you. You agreed to this.",
    "I was about to suggest that force-feeding might be required",
    "It would be slightly awkward if the world was destroyed at this point",
    "You know when grown-ups tell you everything's going to be fine, and you think they're probably lying to make you "
    "feel better?",
    "Hello. I'm the Doctor. Basically. Run.",
    "Box falls out of the sky, man falls out of a box, man eats fish custard! And look at you... just sitting there.",
    "Are you stealing clothes now? Those clothes belong to people you know.",
    "Blimey. Get a girlfriend, Jeff.",
    "I'm the Doctor, I'm worse than everybody's aunt!",
    "Did he just bring them back? Did he just save the world from aliens, and then bring all the aliens back again?",
    "Do I just have a face that nobody listens to?",
    "Dear Santa, thank you for the dolls and pencils and the fish. It's Easter now, so I hope I didn't wake you "
    "but... honest, it is an emergency. There's a crack in my wall.",
    "I am the bloody queen, mate. Basically, I rule.",
    "Oh, don't mind me, I never could resist a keep out sign",
    "The eyes are not the windows of the soul, they are the doors. Beware what may enter them",
    "It's a long story and I don't know most of it",
    "There's a difference between dormant and patient",
    "Funny how you can say something in your head and it sounds fine...",
    "Am I thinking what I think I'm thinking?",
    "I don't think that's such a good idea, do you? I'm a Timelord, you're a big fish... think of the children.",
    "You owe Casanova a chicken?",
    "Ice can burn. Sofas can read. It's a big universe.",
    "Never use force, you just embarrass yourself! Unless you're cross, in which case, always use force!",
    "If we're going to die, let's die looking like a Peruvian folk band",
    "I'd blush if I had a blood supply, or a real face",
    "Ah, a poncho. The biggest crime against fashion since lederhosen."
]
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
        item = self.name + "\t" + self.key + "\t" + str(self.score) + "\t" + str(self.games)
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
        listword = list(string)        #(DEL)
        listword[index] = letter       #string[index]=letter
        newword = "".join(listword)    #DEL
        string = newword               #DEL
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


# Import user data (if it exists)
# user array
users = []
# read file
#data = open("hangmandata.txt", "r")                       !!!!!!!!!!!!!!!!!!!!!!!
for line in data:
    linelist = line.split("\t")
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
