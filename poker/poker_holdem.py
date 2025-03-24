from random import choice


corazones = "♥"
diamantes = "♦"
treboles = "♣"
picas = "♠"

suits = [corazones, diamantes, treboles, picas]
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

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
    for i in range(2):
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

def play(player_cards, bot_cards, table_cards):
    for turn in range(1, 4):
        show_cards(turn, player_cards, table_cards)

def main():
    texas_holdem()
    deck = create_deck()
    player_cards, bot_cards, table_cards = deal_cards(deck)
    play(player_cards, bot_cards, table_cards)

if __name__ == '__main__':
    main()