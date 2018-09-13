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



# while True:

#     file = cf.audio_dict[random.choice(list(cf.audio_dict.keys()))][0]
#     pygame.mixer.init()
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy(): 
#         pygame.time.Clock().tick(10)
#     # pygame.time.delay(cf.audio_dict[]) use this with the weights, not the ticks.

# Generate list of combos for every round
def round_setup(num_rounds):
    combo_set = []
    curr_length = 0 # time in seconds for current combo

    for round in range(num_rounds):
        combo_set.append([])
        print(combo_set)
        #while curr_length < cf.round_length:

round_setup(3)    


# Main execution
def main():
    print("")