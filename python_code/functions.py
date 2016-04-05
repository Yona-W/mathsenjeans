import os
import json, jsonpickle
from copy import deepcopy
from gamestate import *

def log_replay(turn_history):
    encodeString = json.dumps(json.loads(jsonpickle.encode(turn_history)), indent=4) 
    file = open("replay.json", "w")
    file.write(encodeString)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def play(game_board_state, slot, player_1):

    game_state = deepcopy(game_board_state)

    stones = game_state.stones
    num_stones = stones[slot]

    if num_stones == 0:
        return None

    current_slot = (slot + 1) % 12
    capture_slot = (slot + num_stones + num_stones // 12) % 12

    #todo: make all this less shit

    stones[slot] = 0
    for i in range(0, num_stones):
        stones[current_slot] += 1
        
        if (slot - 1) % 12 == current_slot:
            current_slot = (current_slot + 2) % 12
        else:
            current_slot = (current_slot + 1) % 12

    if player_1:
        did_capture = (12 > capture_slot > 5) and (2 <= stones[capture_slot] <= 3)
    else:
        did_capture = (6 > capture_slot > -1) and (2 <= stones[capture_slot] <= 3)


    while did_capture:
        if player_1:
            game_state.player_1_score += stones[capture_slot]
            stones[capture_slot] = 0
            capture_slot -= 1
            did_capture = (12 > capture_slot > 5) and (2 <= stones[capture_slot] <= 3)
        else:
            game_state.player_2_score += stones[capture_slot]
            stones[capture_slot] = 0
            capture_slot -= 1
            did_capture = (6 > capture_slot > -1) and (2 <= stones[capture_slot] <= 3)


    game_state.stones = stones
    game_state.slot_moved = slot
    game_state.is_player_1_turn = not player_1
    return game_state

def get_slot(letter, player_1):
    if player_1:
        if letter == "1":
            return 0
        if letter == "2":
            return 1
        if letter == "3":
            return 2
        if letter == "4":
            return 3
        if letter == "5":
            return 4
        if letter == "6":
            return 5
    if not player_1:
        if letter == "1":
            return 11
        if letter == "2":
            return 10
        if letter == "3":
            return 9
        if letter == "4":
            return 8
        if letter == "5":
            return 7
        if letter == "6":
            return 6
    return -1

