from random import choice
from readchar import readchar
from time import sleep


corazones = "♥"
diamantes = "♦"
treboles = "♣"
picas = "♠"

suits = [corazones, diamantes, treboles, picas]
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

percentages = [
    [51, 35, 36, 37, 37, 37, 40, 42, 44, 47, 49, 53, 57],
    [39, 37, 38, 38, 39, 39, 40, 42, 43, 48, 50, 54, 55],
    [40, 42, 58, 41, 41, 41, 42, 43, 46, 48, 51, 54, 56],
    [41, 43, 44, 61, 41, 43, 43, 45, 46, 50, 52, 55, 57],
    [40, 42, 44, 46, 64, 45, 46, 48, 49, 50, 53, 56, 59],
    [40, 43, 45, 46, 48, 67, 47, 48, 50, 52, 54, 57, 60],
    [42, 43, 45, 48, 49, 50, 69, 50, 52, 53, 55, 58, 61],
    [42, 45, 46, 48, 50, 51, 53, 72, 55, 55, 57, 59, 62],
    [46, 46, 48, 50, 51, 53, 54, 56, 75, 57, 59, 61, 62],
    [47, 48, 49, 51, 53, 54, 56, 57, 59, 79, 60, 62, 65],
    [52, 53, 54, 55, 55, 56, 58, 59, 61, 61, 80, 62, 65],
    [55, 56, 57, 58, 58, 59, 60, 61, 63, 64, 64, 83, 66],
    [59, 60, 61, 62, 62, 63, 63, 64, 66, 66, 67, 68, 85]
]



cash_bot = 20
cash_player = 20
def create_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append([suit, value])
    return deck

def texas_holdem():
    print("-" * 30 + "\n", end="")
    print("-" * 30 + "\n", end="")
    print("-" * 9 + "TEXAS HOLDEM" + "-" * 9 + "\n", end="")
    print("-" * 30 + "\n", end="")
    print("-" * 30 + "\n\n", end="")

def deal_cards(deck):
    player_cards = []
    bot_cards = []
    table_cards = []
    for i in range(2):
        player_cards.append(choice(deck))
        deck.remove(player_cards[i])
        bot_cards.append(choice(deck))
        deck.remove(bot_cards[i])
    for i in range(5):
        table_cards.append(choice(deck))
        deck.remove(table_cards[i])

    return player_cards, bot_cards, table_cards

def show_cards(turn, player_cards, table_cards):
    print("TURNO {}:".format(turn))

    print("TUS CARTAS\n" + "-" * 30)
    print("[{}{}]\n[{}{}]".format(player_cards[0][0], player_cards[0][1], player_cards[1][0], player_cards[1][1]))
    print("-" * 30)

    for i in range(turn + 2):
        print("[{}{}]".format(table_cards[i][0], table_cards[i][1]))
    print("[--]\n" * (5 - 2 - turn), end="")
    print("-" * 30)

    print("[--]\n[--]")
    print("CARTAS DEL BOT")
    print("-" * 30)

def ask_player():
    respond = ""
    while respond.lower() not in ["s", "n"]:
        print("Quiere seguir? (s/n): ")
        sleep(0.1)
        respond = readchar()
    if respond.lower() == "n":
        print("Has perdido")
        exit()
    return respond

def play(player_cards, bot_cards, table_cards):
    for turn in range(1, 4):
        show_cards(turn, player_cards, table_cards)
        respond = ask_player()



def main():
    texas_holdem()
    deck = create_deck()
    player_cards, bot_cards, table_cards = deal_cards(deck)
    play(player_cards, bot_cards, table_cards)

if __name__ == '__main__':
    main()