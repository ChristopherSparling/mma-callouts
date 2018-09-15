import random
import pygame.mixer
import importlib
import config as cf
import riggs_system as rs

# Could make a gui but that sounds like work
# Console prompts: number of rounds, number 

"""
Functions for setting up round, maybe create list of moves to perform so that I can see the upcoming combo? Maybe that defeats the purpose.
    -> give a mode for known and unknown moves?
configuration file to pull data from, or at least a data structure in this file. Could move basic-dict there as well
"""

"""
    Call out combo to perform
    @combo_list - [[move, go_bool], ...
    @countdown - True/False
"""
def callout(combo_list, countdown = False):
    for combo_key in combo_list:

        if countdown == False:
            file = cf.basic_dict[combo_key[0]][0] 
        else:
            file = combo_key
        
        play_clip(file)

        # if kick should be appended
        if cf.basic_dict[combo_key[0]][1]:
            pygame.time.delay(cf.go_length * cf.time_weight)
            play_clip("./basic-files/go.mp3")
            
        if countdown == False:
            pygame.time.delay(int(cf.basic_dict[combo_key[0]][1] * cf.time_weight))
        else:
            pygame.time.delay(1 * cf.time_weight)
 
# Play relevant .mp3
def play_clip(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)

# Decide based on threshold whether to include a kick
def go_inject():
    return random.randint(0,1) < cf.go_threshold

 
# Generate list of combos for every round
def round_setup(num_rounds):
    combo_set = []

    # list of lists of keys, NOT numbers
    for round in range(num_rounds):
        curr_length = 0 # time in seconds for current combo
        combo_set.append([])
        move_count = 0
        # convert to seconds
        while cf.time_const * curr_length < cf.round_length:

            basic_selected = random.randint(0,1) >= cf.basic_rs_split

            if basic_selected:
                new_combo = random_combo(cf.basic_dict)
                combo_set[round].append([new_combo, go_inject()]) # possibly add kick to basic combo

            else:
                new_combo = random_combo(rs.rs_dict)
                combo_set[round].append([new_combo, False]) # never add kick to rs combo

            curr_length += cf.basic_dict[new_combo][1] * cf.time_const

            # if a kick has been added, increase time accordingly
            if combo_set[round][move_count][1]:
                curr_length += cf.go_length * cf.time_const

            move_count += 1 

    return combo_set

# Perform starting countdown
def initial_count():
    countdown_paths = [ "./basic-files/three.mp3",
                        "./basic-files/two.mp3",
                        "./basic-files/one.mp3",
                        "./basic-files/start.mp3"
                        ]
    callout(countdown_paths, True)

# Return random combo
def random_combo(combo_dict):
    return random.choice(list(combo_dict.keys()))

# Main execution
def main():
    num_rounds = int(input("Enter Number of Rounds: "))

    pygame.mixer.init()
    initial_count()
    program = round_setup(num_rounds) # lists of combos
    for round in range(num_rounds):
        callout(program[round])
        pygame.time.delay(cf.rest_length * cf.time_weight)

    print("Now go to bed")

main()