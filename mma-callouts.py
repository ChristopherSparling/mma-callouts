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

while True: 
    file = audio_dict[random.choice(list(audio_dict.keys()))][0]
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)
