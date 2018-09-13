import random
import pygame.mixer
import importlib
import config as cf

# Could make a gui but that sounds like work
# Console prompts: number of rounds, number 

"""
Functions for setting up round, maybe create list of moves to perform so that I can see the upcoming combo? Maybe that defeats the purpose.
    -> give a mode for known and unknown moves?
configuration file to pull data from, or at least a data structure in this file. Could move audio-dict there as well
"""
"""
    Call out combo to perform
"""
def callout(combo_list, countdown = False):
    for combo_key in combo_list:
        if countdown == False:
            file = cf.audio_dict[combo_key][0] # get (relative) file path
        else:
            file = combo_key
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
            
        if countdown == False:
            pygame.time.delay(cf.audio_dict[combo_key][1] * cf.time_weight)
        else:
            pygame.time.delay(1 * cf.time_weight)
 
""" 
    Generate list of combos for every round
"""
def round_setup(num_rounds):
    combo_set = []

    # list of lists of keys, NOT numbers
    for round in range(num_rounds):
        curr_length = 0 # time in seconds for current combo
        combo_set.append([])

        # convert to seconds
        while cf.time_const * curr_length < cf.round_length:
            # should make a function to randomly choose a value instead of this
            new_combo = cf.random_combo()
            combo_set[round].append(new_combo)
            curr_length += cf.audio_dict[new_combo][1] * cf.time_const
    #print(combo_set)
    return combo_set

"""
    Perform starting countdown
"""
def initial_count():
    countdown_paths = [ "./audio-files/three.mp3",
                        "./audio-files/two.mp3",
                        "./audio-files/one.mp3"
                        #,"./audio-files/start.mp3"
                        ]
    callout(countdown_paths, True)
    

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