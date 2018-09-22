import random
"""
basic_dict = {
    'name' (key): ['path-to-file', (basic-length?), combo-length (numeric for seconds), 'combo text']
}
http://www.fromtexttospeech.com/ use Daisy or George
"""
basic_dict = {
    'one':      ['./basic-files/one.mp3',    1, 'Jab'],
    'two':      ['./basic-files/two.mp3',    1, 'Jab Cross'],
    'three':    ['./basic-files/three.mp3',  2, 'Jab Cross Hook'],
    'four':     ['./basic-files/four.mp3',   2.5, 'Jab Cross Hook Cross'],
    'five':     ['./basic-files/five.mp3',   3, 'Jab Cross Hook Cross Up'],
    'six':      ['./basic-files/six.mp3',    1, 'Cross'],
    'seven':    ['./basic-files/seven.mp3',  1, 'Cross Up'],
    'eight':    ['./basic-files/eight.mp3',  1.5, 'Cross Up Cross'],
    'nine':     ['./basic-files/nine.mp3',   1.5, 'Hook Cross Hook'],
    'ten':      ['./basic-files/ten.mp3',    1.5, 'Cross Hook'],
}
# list of tips to be displayed below combo maybe
tips_list = []

# 180 seconds per round -> 3 minutes = standard round length
round_length = 180

# used to determine delays 
time_weight = 875
time_const = time_weight/1000
rest_length = 10

kick_threshold = 0.5
kick_length = 1
go_sk_split = 0.5

basic_rs_split = 0