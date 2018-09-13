import random
import pygame.mixer
<<<<<<< HEAD
"""
audio_dict = {
    'name' (key): ['path-to-file', (audio-length?), combo-length (numeric for seconds), 'combo text']
}

http://www.fromtexttospeech.com/ use Daisy or George
"""
audio_dict = {
    'one':      ['./audio-files/one.mp3',    2, 'Jab'],
    'two':      ['./audio-files/two.mp3',    3, 'Jab Cross'],
    'three':    ['./audio-files/three.mp3',  4, 'Jab Cross Hook'],
    'four':     ['./audio-files/four.mp3',   5, 'Jab Cross Hook Cross'],
    'five':     ['./audio-files/five.mp3',   6, 'Jab Cross Hook Cross Up'],
    'six':      ['./audio-files/six.mp3',    2, 'Cross'],
    'seven':    ['./audio-files/seven.mp3',  3, 'Cross Hook'],
    'eight':    ['./audio-files/eight.mp3',   4, ''],
    'nine':     ['./audio-files/nine.mp3',    3, ''],
    'ten':      ['./audio-files/ten.mp3',     4, ''],
}

tips_list = [

]
=======
import importlib
import config as cf

>>>>>>> a6303fe644f44d3c347ebadedadae40172258de7
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

<<<<<<< HEAD
# Get number of rounds desired
#num_rounds = input("Desired Round Count: ")
# Specify preset configuration or define a custom configuration in the config file

# Countdown function to do a 3 2 1 Start sort of thing

"""[Config Options]
Length of rounds
Moves to be included -> provide an editable key list to be used -> done as list of lists
Length of "time units" compared to real time

"""
combo_count = 20
current_count  = 0
tick_weight = 1000
pygame.mixer.init()

while current_count < combo_count: 
    combo = random.choice(list(audio_dict.keys()))
    file = audio_dict[combo][0]
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    # Output current combo moves
    print(audio_dict[combo][2])

    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(tick_weight*audio_dict[combo][1])
    current_count += audio_dict[combo][1]
    
=======
    pygame.mixer.init()
    initial_count()
    program = round_setup(num_rounds) # lists of combos
    for round in range(num_rounds):
        callout(program[round])
        pygame.time.delay(cf.rest_length * cf.time_weight)

    print("Now go to bed")

main()
>>>>>>> a6303fe644f44d3c347ebadedadae40172258de7
