from random import choice, randint
from readchar import readchar
from time import sleep
from os import system


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

initial_cash = 20

cash_bot = initial_cash
cash_player = initial_cash
pot = 0

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

def show_cards(turn, player_cards, table_cards, bot_cards):
    global cash_player, cash_bot, pot
    print("Tu dinero: {}\nBot dinero: {}\nDinero en la mesa: {}".format(cash_player, cash_bot, pot))
    print("TURNO {}:".format(turn))

    print("TUS CARTAS\n" + "-" * 30)
    print("[{}{}]\n[{}{}]".format(player_cards[0][0], player_cards[0][1], player_cards[1][0], player_cards[1][1]))
    print("-" * 30)

    for i in range(turn + 2):
        print("[{}{}]".format(table_cards[i][0], table_cards[i][1]))
    print("[--]\n" * (5 - 2 - turn), end="")
    print("-" * 30)

    print("[{}{}]\n[{}{}]".format(bot_cards[0][0], bot_cards[0][1], bot_cards[1][0], bot_cards[1][1]))
    #print("[--]\n[--]")
    print("CARTAS DEL BOT")
    print("-" * 30)

def bet():
    global cash_player, cash_bot, pot
    if cash_player >= 0:
        print("-" * 30)
        print("\n")

        respond = ""
        while respond.lower() not in ["a", "n", "l"]:
             print("Quieres apostar: A\n"
                  "No quieres apostar: N\n"
                   "All in: L\n")
             sleep(0.1)
             respond = input()
        bet = 0

        if respond.lower() == "a":
            while bet > cash_player or bet < 1:
                print("Cuanto quieres apostar?")
                try:
                    bet = int(input())
                    if bet > cash_player and bet < 1:
                        print("Valor fuera de tus posibilidades")
                except ValueError:
                    print("Valor no correcto, reintentelo")
            pot += bet
            cash_player -= bet
        elif respond.lower() == "l":
            bet = cash_player
            pot += cash_player
            cash_player = 0

        elif respond.lower() == "n":
            print("Has perdido {}$".format(pot))
            exit()

        return bet

def call_the_bet(bet_more):
    global cash_player, pot
    input = ""
    while input.lower() not in ["s", "n"]:
        print("Tienes {}$. Quieres seguir jugando? S/N".format(cash_player))
        input = input()
    if input.lower() == "s":
        cash_player -= bet_more
        pot += bet_more

def bot_decision(bot_cards, turn, cash_bet):
    global cash_bot, pot
    probability = randint(1, 100)

    firs_index = values.index(bot_cards[0][1])
    second_index = values.index(bot_cards[1][1])

    percent = percentages[firs_index][second_index]
    #Se le suma a la probabilidad dependiendo el turno
    if turn == 3:
        percent = percent + percent * 0.1
    elif turn == 2:
        percent = percent + percent * 0.2
    elif turn == 1:
        percent = percent + percent * 0.3

    #Se le resta dinero a la apuesta dependiendo des dinero apostado, cuanto mas tenga que apostar, mas se restara

    percentage_subtraction = cash_bet * 0.2 / cash_bot
    percent = percent - percent * percentage_subtraction


    if probability <= int(percent):
        print("El bot decide seguir jugando")
        cash_bet_bot = cash_bet
        pot += cash_bet_bot
        cash_bot -= cash_bet_bot
        if int(percent) < 15:
            add = randint(1, cash_bot)
            cash_bot -= add
            pot += add
            print("El bot ha subido la apuesta a {}$".format(cash_bet_bot + add))
            return add
    else:
        print("El bot no quiere seguir jugando\nHas ganado {}$".format(pot))
        exit()

def check_escalera_real(cards_met):
    escalera_real = ["A", "K", "Q", "J", "10"]
    cards_found = []
    for card in cards_met:
        if card[1] in escalera_real:
            cards_found.append(card)
            escalera_real.remove(card[1])
    if escalera_real == []:
        suit = cards_met[0][0]
        for cards in cards_found:
            if cards[0] != suit:
                return False
    else:
        return False
    return True

def check_escalera_color(cards_met):
    ordered_list = []
    cards_meet_copy = cards_met.copy()
    for i in range(7):
        lower_card = cards_meet_copy[0]
        for card in cards_meet_copy:
            index = values.index(card[1])
            if index < values.index(lower_card[1]):
                lower_card = card
        cards_meet_copy.remove(lower_card)
        ordered_list.append(lower_card)
    return None

def check_winner(cards_to_check, cards_player):
    cards_met = cards_to_check.copy()
    cards_met.extend(cards_player)

    #Comprovar escalera real
    escalera_real = check_escalera_real(cards_met)
    #Comprovar Escalera Color
    check_escalera_color(cards_met)

def play(player_cards, bot_cards, table_cards):
    for turn in range(1, 4):
        system('cls')
        texas_holdem()
        show_cards(turn, player_cards, table_cards, bot_cards)
        cash_bet = bet()
        bet_more = bot_decision(bot_cards, turn, cash_bet)
        if bet_more != None:
            call_the_bet(bet_more)
        check_winner(table_cards, player_cards)

def main():
    system('cls')
    deck = create_deck()
    player_cards, bot_cards, table_cards = deal_cards(deck)
    play(player_cards, bot_cards, table_cards)

if __name__ == '__main__':
    main()