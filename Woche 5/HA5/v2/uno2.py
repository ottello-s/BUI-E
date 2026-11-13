
from enum import Enum
import random


# ==========================================
# COLOR
# ==========================================

class Color(Enum):
    RED = "Rot"
    YELLOW = "Gelb"
    GREEN = "Grün"
    BLUE = "Blau"

    def __repr__(self):
        return self.value


# ==========================================
# CARD
# ==========================================

class Card:

    def __init__(self, color: Color, value: int):
        self.color = color
        self.value = value

    def __repr__(self):
        return f"{self.color.value} {self.value}"


# ==========================================
# PLAYER
# ==========================================

class Player:

    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def draw(self, stack):
        """Draw one card from the CardStack."""
        card = stack.draw()

        if card is not None:
            self.hand.append(card)

        return card

    def play_first_match(self, top_card):
        """
        Play the first matching card in the hand.
        A card matches if its color OR value is equal.
        """

        for card in self.hand:

            if (card.color == top_card.color or
                    card.value == top_card.value):

                self.hand.remove(card)
                return card

        return None

    def has_won(self):
        return len(self.hand) == 0

    def __repr__(self):
        return f"{self.name}: {self.hand}"


# ==========================================
# CARD STACK
# ==========================================

class CardStack:

    def __init__(self):
        self.draw_pile = []
        self.discard_pile = []

        self.create_cards()
        random.shuffle(self.draw_pile)

    def create_cards(self):
        """Create 40 unique cards."""

        for color in Color:
            for value in range(10):
                self.draw_pile.append(Card(color, value))

    def draw(self):
        """Draw a card, replenishing the pile if necessary."""

        if not self.draw_pile:
            self.replenish()

        if not self.draw_pile:
            return None

        return self.draw_pile.pop()

    def discard(self, card):
        """Place a card on the open discard pile."""
        self.discard_pile.append(card)

    def replenish(self):
        """
        Rebuild the draw pile from the discard pile.
        The top card remains on the discard pile.
        """

        if len(self.discard_pile) <= 1:
            return

        top_card = self.discard_pile.pop()

        self.draw_pile = self.discard_pile
        self.discard_pile = [top_card]

        random.shuffle(self.draw_pile)

        print("\nDer verdeckte Stapel wurde neu gebildet.")

    def __repr__(self):
        return (
            f"CardStack("
            f"draw_pile={len(self.draw_pile)}, "
            f"discard_pile={len(self.discard_pile)})"
        )


# ==========================================
# GAME
# ==========================================

class Game:

    def __init__(self, num_players=4):

        if num_players < 2:
            raise ValueError("Mindestens 2 Spieler erforderlich!")

        self.players = [
            Player(f"Spieler {i + 1}")
            for i in range(num_players)
        ]

        self.stack = CardStack()
        self.current = 0
        self.finished = False

        self.deal()
        self.start_discard()

    def deal(self):
        """Give every player 5 cards."""

        for _ in range(5):
            for player in self.players:
                player.draw(self.stack)

    def start_discard(self):
        """Move the first card to the discard pile."""

        card = self.stack.draw()
        self.stack.discard(card)

    def step(self):
        """Execute one player's turn."""

        player = self.players[self.current]
        top_card = self.stack.discard_pile[-1]

        print(f"\n{player.name} ist am Zug.")
        print(f"Oberste Karte: {top_card}")

        # Try to play the first matching card
        card = player.play_first_match(top_card)

        if card is not None:

            self.stack.discard(card)

            print(f"{player.name} spielt {card}")

        else:

            # No matching card: draw exactly one
            card = player.draw(self.stack)

            if card is None:
                print("Keine Karten mehr verfügbar. Unentschieden!")
                self.finished = True
                return

            print(f"{player.name} zieht {card}")

        print(f"Karten auf der Hand: {len(player.hand)}")

        # Check for winner
        if player.has_won():

            print(f"\n{player.name} hat gewonnen!")
            self.finished = True
            return

        # Move to next player
        self.current = (self.current + 1) % len(self.players)

    def play(self):

        print("\n========== UNO ==========")
        print("Spielstart!\n")

        for player in self.players:
            print(player)

        print(f"\n{self.stack}")
        print(f"Ablage: {self.stack.discard_pile[-1]}")

        round_number = 1

        while not self.finished:

            print(f"\n---------- Runde {round_number} ----------")

            self.step()

            round_number += 1

        print("\n========== SPIELENDE ==========")

        for player in self.players:
            print(player)

        print(self.stack)

    def __repr__(self):
        return (
            f"Game(players={self.players}, "
            f"current={self.current}, "
            f"finished={self.finished})"
        )


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    game = Game(num_players=4)
    game.play()
