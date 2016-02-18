from colorama import init, Fore
init()

class Game_State():
    player_1_score = 0
    player_2_score = 0
    stones = [4,4,4,4,4,4,4,4,4,4,4,4]
    is_player_1_turn = False

    slot_moved = -1

    def __init__(this, p1score, p2score, stones, slot_moved):
        this.player_1_score = p1score
        this.player_2_score = p2score
        this.stones = stones
        this.slot_moved = slot_moved
        this.is_player_1_turn = True



    def print_gameboard(this):
        print()
        print("╔════╦════╦════╦════╦════╦════╗")
        
        p2_stones_string = "║ "
        
        for i in range(11,5,-1):
            numstring = str(this.stones[i]).zfill(2)
            colorstring = Fore.WHITE

            if numstring == "00": colorstring = Fore.BLACK
            if numstring == "01": colorstring = Fore.YELLOW
            if numstring == "02": colorstring = Fore.RED

            p2_stones_string += colorstring + numstring + Fore.RESET + " ║ "
        
        p2_stones_string += "Player 2 Score: " + str(this.player_2_score)
        print(p2_stones_string)
        
        print("╠════╬════╬════╬════╬════╬════╣")
        
        p1_stones_string = "║ "
        for i in range(0,6):
            numstring = str(this.stones[i]).zfill(2)
            colorstring = Fore.WHITE

            if numstring == "00": colorstring = Fore.BLACK
            if numstring == "01": colorstring = Fore.YELLOW
            if numstring == "02": colorstring = Fore.RED

            p1_stones_string += colorstring + numstring + Fore.RESET + " ║ "

        p1_stones_string += "Player 1 Score: " + str(this.player_1_score)
        print(p1_stones_string)
        
        print("╚════╩════╩════╩════╩════╩════╝")

    def is_state_legal(this):
        sum_p1 = 0
        for i in range(0, 6):
            sum_p1 += this.stones[i]
        if sum_p1 == 0:
            return False

        sum_p2 = 0
        for i in range(6, 12):
            sum_p2 += this.stones[i]
        if sum_p2 == 0:
            return False

        return True
