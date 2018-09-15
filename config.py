import random
"""
audio_dict = {
    'name' (key): ['path-to-file', (audio-length?), combo-length (numeric for seconds), 'combo text']
}
http://www.fromtexttospeech.com/ use Daisy or George
"""
basic_dict = {
    'one':      ['./audio-files/one.mp3',    1, 'Jab'],
    'two':      ['./audio-files/two.mp3',    1, 'Jab Cross'],
    'three':    ['./audio-files/three.mp3',  2, 'Jab Cross Hook'],
    'four':     ['./audio-files/four.mp3',   2.5, 'Jab Cross Hook Cross'],
    'five':     ['./audio-files/five.mp3',   3, 'Jab Cross Hook Cross Up'],
    'six':      ['./audio-files/six.mp3',    1, 'Cross'],
    'seven':    ['./audio-files/seven.mp3',  1, 'Cross Up'],
    'eight':    ['./audio-files/eight.mp3',  1.5, 'Cross Up Cross'],
    'nine':     ['./audio-files/nine.mp3',   1.5, 'Hook Cross Hook'],
    'ten':      ['./audio-files/ten.mp3',    1, 'Cross Hook'],
}
# list of tips to be displayed below combo maybe
tips_list = []

# 180 seconds per round -> 3 minutes = standard round length
round_length = 10

# used to determine delays 
time_weight = 750
time_const = time_weight/1000
rest_length = 10
go_threshold = 0.2
go_length = 1

basic_rs_split = 0.5
