import random
import pygame.mixer
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
# Could make a gui but that sounds like work
# Console prompts: number of rounds, number 

"""
Functions for setting up round, maybe create list of moves to perform so that I can see the upcoming combo? Maybe that defeats the purpose.
    -> give a mode for known and unknown moves?

configuration file to pull data from, or at least a data structure in this file. Could move audio-dict there as well
"""

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
    
