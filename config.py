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

# list of tips to be displayed below combo maybe
tips_list = []

# 180 seconds per round -> 3 minutes = standard round length
round_length = 180 