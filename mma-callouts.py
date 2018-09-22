import random
import pygame.mixer
import importlib
import config as cf
import riggs_system as rs

"""
    Call out combo to perform
    @combo_list - [[move, go_bool], ...
    @countdown - True/False
"""
def callout(combo_list, countdown = False):
    for combo_key in combo_list:
        is_basic_dict = combo_key[0] in cf.basic_dict.keys()
        if countdown == False:
            if is_basic_dict:
                file = cf.basic_dict[combo_key[0]][0]
                print_moves(combo_key, cf.basic_dict[combo_key[0]][2])
            else:
                file = rs.rs_dict[combo_key[0]][0]
                print_moves(combo_key, rs.rs_dict[combo_key[0]][2])

        else:
            file = combo_key

        play_clip(file)

        # if kick should be appended
        if combo_key[1]:
            pygame.time.delay(cf.kick_length * cf.time_weight)
            play_clip("./basic-files/" + combo_key[1] +".mp3")
            
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
def kick_inject():
    if random.randint(0,1) <= cf.kick_threshold:
        if random.randint(0,1) < cf.go_sk_split: 
            return "go"
        return "switch-kick"
    return False

 
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
                combo_set[round].append([new_combo, kick_inject()]) # possibly add kick to basic combo
                curr_length += cf.basic_dict[new_combo][1] * cf.time_const

            else:
                new_combo = random_combo(rs.rs_dict)
                combo_set[round].append([new_combo, False]) # never add kick to rs combo
                curr_length += rs.rs_dict[new_combo][1] * cf.time_const
            
            # if a kick has been added, increase time accordingly
            if combo_set[round][move_count][1]:
                curr_length += cf.kick_length * cf.time_const

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

# Return breakdown of previous round's combos
def round_breakdown(combo_set):
    tracking_dict = {}
    
    for combo in combo_set:
        if combo[0] not in tracking_dict.keys():
            tracking_dict[combo[0]] = 1
        else:
            tracking_dict[combo[0]] += 1
    
    i = 1
    s = [(key, tracking_dict[key]) for key in sorted(tracking_dict, key=tracking_dict.get, reverse=True)]

    for key, value in s:
        print(key, ": ", value, end = '\t')
        if i == 6:
            print ('\r')
            i = 0
        i += 1
    print()

# Print out moves for current combo
def print_moves(combo_name,combo_moves):
   
    print(combo_name[0].capitalize(), ": \t", combo_moves, " ", combo_name[1].capitalize() if combo_name[1] else '', sep='' )


# Main execution
def main():
    num_rounds = int(input("Enter Number of Rounds: "))
    
    pygame.mixer.init()
    #initial_count()
    
    program = round_setup(num_rounds) # lists of combos
    
    round_breakdown(program[0])
    for round in program:
        callout(round)
        pygame.time.delay(cf.rest_length * cf.time_weight)
    
    """
    print("Now go to bed")
    """
main()