total = 150
game = False

def get_total():
    global total
    return total

def take_candies(take: int):
    global  total
    total -= take

def check_game():
    global  game
    return game

def new_game():
    global  game
    global total
    if game:
        game = False
    else:
        total = 150
        game = True









# class Games:
#     total: int
#     player_one_id: int
#     player_tow_id: int
#
#     def __init__(self, total: int, player_one_id: int):
#         self.total = total
#         self.player_one_id = player_one_id