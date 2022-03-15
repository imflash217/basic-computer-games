###############################################################
#  This is a simulation of the Acey Ducey card game.
#  In the game, the dealer (the computer) deals two
#  cards face up.  You have an option to bet or not to
#  bet depending on whether or not you feel the next
#  card dealt will have a value between the first two.
#
#  Your initial money is set to $100. The game keeps
#  going on until you lose all your money or interrupt
#  the program.
#
###############################################################

import random

cards = {
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "Jack",
    11: "Queen",
    12: "King",
    14: "Ace",
}


def play_game() -> None:
    """Play the Acey-Ducey game"""

    cash = 100

    while cash > 0:
        print(f"You now have ${cash}.")
        print(f"Here aare you next two cards.")
        round_cards = list(cards.keys())
        random.shuffle(round_cards)
        card_a = round_cards.pop()
        card_b = round_cards.pop()
        card_c = round_cards.pop()
        if card_a > card_b:
            card_a, card_b = card_b, card_a
        print(f"{cards[card_a]}")
        print(f"{cards[card_b]}\n")

        while True:
            try:
                bet = int(input("What's your bet? "))
                if bet < 0:
                    raise ValueError("Bet must be more than 0")
                if bet == 0:
                    print("CHICKEN!!\n")
                if bet > cash:
                    print("Sorry my friend! but you bet too much.")
                    print(f"You only have ${cash} available!!")
                    continue
                cash -= bet
                break
            except ValueError:
                print("Please enter a positive number")

        print(f"{cards[card_c]}")
        if bet > 0:
            if card_a < card_c < card_b:
                print("You WIN!!!!")
                cash += bet * 2
            else:
                print("SORRY!! You loose!!")

    print("Sorry, bro! You blew your purse!")
