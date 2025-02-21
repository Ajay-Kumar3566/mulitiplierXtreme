import random
import json
import time
import pygame    # This is new one ⭐⭐⭐⭐⭐

# ANSI ( American National Standards Institute) codes  ✨✨✨✨
'''
def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Usage
print(colored_text("This is red!", "31"))  # Red
print(colored_text("This is green!", "32"))  # Green
print(colored_text("This is bold!", "1"))  # Bold

'''
'''
Here I am using "random" module.....

random.random() -> generates a number between 0.0 to 1.0(but 1.0 exclusive)
random.randint(a,b)-> generates a number between a to b (both are included) 
random.uniform(a,b) -> generates a floating number between a to b
random.randrange(start, end,step) -> (0,10,2)-> (2,4,6,8) 
'''

'''
FATURES:
-->Hint System
--> difficulties  levels
--> Score Sysytem
-->Attempts System
--> Customizable Range
-->Mutiplayer Mode
-->Leaderboard System
-->Fun messages
--> Sound effect
-->Time system

'''
pygame.init() # this is the initialization of the pygame

'''
Here is two conditions...
1. if the player enter the wrong input then "wrong.mp3" will give sound
2. if the player enter the correct input then "correct.mp3" will give sound


'''
correct_sound=pygame.mixer.Sound("correct.mp3")
wrong_sound=pygame.mixer.Sound("wrong.mp3")




with open("quotes.json","r" , encoding="utf-8" , errors="ignore") as file:
    messages=json.load(file)["messages"]

def fun_message(category):
    return random.choice(messages[category])

# def saveData(name, score):
#     try:
#         with open(f"{name}.json", "r+") as file:
#             json.load(file)['scores'].append(score);
#         print("Storing in old file")
#     except FileNotFoundError:
#         with open(f"{name}.json","w") as file:
#             print("stroring in fresh file")
#             json.dump({"scores": [{score}]}, file, indent=2)

def play_game():
    
    print("\n \033[1;101m Welcome in the Multiplier Number Guessing Game !\033[0m")
    num_players=int(input("Enter the number of players: "))

    '''
    creation of lists
    1. player_names
    2. scores
    '''
    player_names=[]
    scores=[]
    for i in range(num_players):
        name=input(f"Enter player {i+1}'s name: ").title()
        player_names.append(name)
       
    print(" Player List: ",player_names)

    maxium_attempts=difficulties_level()
    
    starting_num=int(input("enter begining number: "))
    ending_num=int(input("enter last number: "))
   
    penality=2 
    print(f"You select a number in the range between {starting_num}  to {ending_num} .\n")

    for name in player_names:
        start_time=time.time()   # your time starts...
        attempt=0
        score=100
        random_number=random.randint(starting_num,ending_num) 
        # this random module is used to generate random number 

        print(f"\n{name}, your turn starts now.....\n")


        while attempt<maxium_attempts:
            try:
                guess=int(input("please guess a number: "))
                print("Generated random number is: ",random_number,"\n")
                attempt+=1
                
                if guess<random_number:
                    wrong_sound.play()
                    print(fun_message("too_low"))
                    score=scoring_system(score,penality)
                elif guess>random_number:
                    wrong_sound.play()
                    print(fun_message("too_high"))
                    score=scoring_system(score,penality)
                else:
                    end_time=time.time()  # your time ends at ..
                    time_taken=end_time-start_time
                    correct_sound.play()
                    print(fun_message("correct"))
                    print(f"Congratulations  {name}! You have guessed the correct numbers in {attempt} attempts. ")
                    print(f"Your final score is: {score}")
                    print(f"It took you {time_taken :.2f} seconds to guess the correct number")
                    print(fun_message("goodbye"))
                    print(f"{name} , your turn is over!")
                    scores.append(score)

                    # saveData(name, score);
                    # attempt = maxium_attempts
                    break
            except ValueError:

                print("Invalid Number! Please enter a valid number..")
        if attempt==maxium_attempts:
            updated_socres=score
            



            ''' it will notify to the players that they won the game with the remaining attempts
            or if they are unable to guess the right number in their choosen attempts then the game will over...😒😒

            '''

            remaining_attempts=maxium_attempts-attempt
            if remaining_attempts>0:
                print(f"You have {remaining_attempts} remaining attempts!\n")
            else:
                print(f"Game Over! The correct number was {random_number}!\n")
                

    # Display final scores of all players
    print("\nFinal Score")
    for i in range(num_players):
        print(f"{player_names[i]}: {scores[i]}")

    '''
    Problem Statement:
    when the number of attempts but the player is not able to guess the right number 
    then it shows the arrayindexofbound error ?????
    '''

    
    print("⭐⭐⭐ Leaderboard ⭐⭐⭐\n")

    players=sorted(zip(scores,player_names),reverse=True)  #⭐⭐⭐⭐⭐
    for ind,(score,name) in enumerate(players, start=1):
        print(f"{ind}. {name} {score}")


'''
this function is used to add a feature like difficulties level ..
Acoording to choosen number , the player will play hard, medium and easy level of game. 💪💪💪
'''
def difficulties_level():
    level= int(input("Enter difficulties level: \n 1. Hard   \n 2.Medium \n 3. Easy  \n"))
    Rules=''' Rules of this game:\n
         ➡️ If you choose the hard (1) level then you have only 5 attempts.
         ➡️ If you choose the medium (2) level then you have only 10 attempts.
         ➡️ If you choose the easy level (3) you will get 20 attempts.
    '''
    print(Rules)
    if level==1:
        print("You have 5 chances to guess the correct number !\n")
        return 5
    elif level==2:
        print("You have 10 chances to guess the correct number !\n")
        return 10
    else:
        print("You have only 20 chances to guess the correct number !\n")
        return 20





'''This function is used to track the score of the player!
initial value of the score is 100 .
when the player guess the incorrect answer then his score will deduct by 2 .
'''

def scoring_system(current_score, penality):
    return max(current_score-penality,0)

play_game()
   





        



        
        
















