import random


def play_mystery_word():
        bad_choices = 0
        prev_choices = []
        with open("words.txt") as f:
                easy_list = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                for line in f.readlines():
                        if len(line.strip()) > 3 and len(line.strip()) < 7:             
                                easy_list.append(line)
        easy_word_to_guess = (random.choice(easy_list))
        # b = easy_word_to_guess.split(",")
        print("Your word contains", len(easy_word_to_guess), "letters!")
        print(easy_word_to_guess)
        guess = str(input("Please guess a letter from the mystery word: ")).lower()
        def display_letter(letter, prev_choices):
                for letter in easy_word_to_guess.split():
                        return letter
                else:
                        return "_"
        if len(guess) > 1:
                        print("Please select only one character")
        if guess not in easy_word_to_guess:
                bad_choices += 1
                print("You done messed up mate!")
        else:
                print("Nice job big shooter!")

        while bad_choices < 8 and not easy_word_to_guess:
                [display_letter(letter, prev_choices) for letter in easy_word_to_guess]
                prev_choices.append(guess)
      

# with open("words.txt") as f:
#         normal_list = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
#         for line in f.readlines():
#             if len(line.strip()) > 5 and len(line.strip()) < 9:             
#                 normal_list.append(line)
# normal_word_to_guess = (random.choice(normal_list))

# print(normal_word_to_guess)

# with open("words.txt") as f:
#         hard_list = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
#         for line in f.readlines():
#             if len(line.strip()) >= 8:             
#                 hard_list.append(line)
# hard_word_to_guess = (random.choice(hard_list))

# print(hard_word_to_guess)


print("WELCOME TO THE MYSTERY WORD GAME!")
mode = input("What mode would you like to play: 1)Easy. 2)Normal. 3)Hard? Type 1, 2, or 3 for choice:")
if mode == "1":
        print("You have chosen easy!") 
        play_mystery_word()
elif mode == "2":
        print("You have chosen normal!")
        print("Your word contains", len(normal_word_to_guess, "letters"))
elif mode == "3":
        print("You have chosen hard!")
        print("Your word contains",len(hard_word_to_guess),"letters!")
else:
        print("Please read the instructions!")    
