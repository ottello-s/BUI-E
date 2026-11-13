
import random


class Card:
    """Repräsentiert eine UNO-Karte."""

    COLORS = ["Rot", "Blau", "Grün", "Gelb"]

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        if self.color is None:
            return f"{self.value}"
        return f"{self.color} {self.value}"

    def is_wild(self):
        return self.value in ("Joker", "+4")

    def is_playable(self, top_card, current_color):
        if self.is_wild():
            return True

        return (
            self.color == current_color
            or self.value == top_card.value
        )


class Deck:
    """Erstellt und verwaltet den Kartenstapel."""

    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        self.cards = []

        for color in Card.COLORS:
            # Eine Karte mit der Zahl 0
            self.cards.append(Card(color, 0))

            # Zwei Karten jeder Zahl von 1 bis 9
            for number in range(1, 10):
                self.cards.append(Card(color, number))
                self.cards.append(Card(color, number))

            # Aktionskarten
            for _ in range(2):
                self.cards.append(Card(color, "Aussetzen"))
                self.cards.append(Card(color, "Richtungswechsel"))
                self.cards.append(Card(color, "+2"))

        # Joker und +4-Joker
        for _ in range(4):
            self.cards.append(Card(None, "Joker"))
            self.cards.append(Card(None, "+4"))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            return None
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


class Player:
    """Verwaltet einen Spieler und seine Handkarten."""

    def __init__(self, name, is_human=False):
        self.name = name
        self.hand = []
        self.is_human = is_human

    def draw_card(self, deck):
        card = deck.draw()

        if card is not None:
            self.hand.append(card)

        return card

    def play_card(self, index):
        return self.hand.pop(index)

    def has_won(self):
        return len(self.hand) == 0

    def show_hand(self):
        for index, card in enumerate(self.hand):
            print(f"  [{index + 1}] {card}")


class UNOGame:
    
    """Steuert den gesamten UNO-Spielablauf."""

    def __init__(self, number_of_players):
        self.players = [
            Player("Du", is_human=True)
        ]

        for i in range(1, number_of_players):
            self.players.append(Player(f"Computer {i}"))

        self.deck = Deck()
        self.deck.shuffle()

        self.discard_pile = []
        self.current_color = None
        self.current_player = 0
        self.direction = 1
        self.game_over = False

    @property
    def top_card(self):
        return self.discard_pile[-1]

    def setup_game(self):
        """Teilt sieben Karten an jeden Spieler aus."""

        print("\n========== UNO ==========\n")

        for _ in range(7):
            for player in self.players:
                player.draw_card(self.deck)

        # Eine Zahlenkarte als Startkarte auswählen
        while True:
            card = self.deck.draw()

            if card is None:
                raise RuntimeError("Der Kartenstapel ist leer.")

            if isinstance(card.value, int):
                self.discard_pile.append(card)
                self.current_color = card.color
                break

            self.deck.cards.insert(0, card)

        print(f"Startkarte: {self.top_card}")
        print(f"Anzahl Spieler: {len(self.players)}")

    def get_next_player(self, steps=1):
        self.current_player = (
            self.current_player + self.direction * steps
        ) % len(self.players)

    def recycle_discard_pile(self):
        """Mischt den Ablagestapel zurück in den Kartenstapel."""

        if len(self.discard_pile) <= 1:
            return

        top = self.discard_pile.pop()

        self.deck.cards.extend(self.discard_pile)
        random.shuffle(self.deck.cards)

        self.discard_pile = [top]

    def draw_card(self, player):
        """Zieht eine Karte, gegebenenfalls durch Recycling."""

        if len(self.deck) == 0:
            self.recycle_discard_pile()

        card = player.draw_card(self.deck)

        if card:
            print(f"{player.name} zieht eine Karte.")
        else:
            print("Keine Karten mehr verfügbar.")

        return card

    def choose_color(self, player):
        """Wählt eine neue Farbe nach einem Joker."""

        if player.is_human:
            print("\nWähle eine Farbe:")

            for i, color in enumerate(Card.COLORS):
                print(f"  [{i + 1}] {color}")

            while True:
                choice = input("> ").strip()

                if choice in ("1", "2", "3", "4"):
                    return Card.COLORS[int(choice) - 1]

                print("Ungültige Auswahl.")

        # Computer wählt die häufigste Farbe auf seiner Hand
        colors = [
            card.color for card in player.hand
            if card.color is not None
        ]

        if not colors:
            return random.choice(Card.COLORS)

        return max(set(colors), key=colors.count)

    def show_game_state(self):
        print("\n" + "=" * 35)
        print(f"Ablagekarte: {self.top_card}")
        print(f"Aktuelle Farbe: {self.current_color}")
        print(f"Karten im Stapel: {len(self.deck)}")

        for player in self.players:
            print(
                f"{player.name}: {len(player.hand)} Karten"
            )

        print("=" * 35)

    def get_playable_cards(self, player):
        return [
            i for i, card in enumerate(player.hand)
            if card.is_playable(
                self.top_card, self.current_color
            )
        ]

    def play_card(self, player, index):
        """Spielt eine Karte und führt ihre Aktion aus."""

        card = player.play_card(index)

        self.discard_pile.append(card)
        print(f"\n{player.name} spielt: {card}")

        if card.is_wild():
            self.current_color = self.choose_color(player)
            print(f"Neue Farbe: {self.current_color}")
        else:
            self.current_color = card.color

        if len(player.hand) == 1:
            if player.is_human:
                answer = input(
                    "Du hast nur noch eine Karte! UNO ansagen? (j/n): "
                ).strip().lower()

                if answer != "j":
                    print("UNO vergessen! Du ziehst 2 Strafkarten.")
                    for _ in range(2):
                        self.draw_card(player)
                else:
                    print("UNO!")
            else:
                print(f"{player.name} sagt UNO!")

        if player.has_won():
            print(f"\n{player.name} hat gewonnen!")
            self.game_over = True
            return

        # Aktionskarten
        if card.value == "Aussetzen":
            print("Der nächste Spieler wird übersprungen.")
            self.get_next_player(2)
            return

        if card.value == "Richtungswechsel":
            self.direction *= -1
            print("Die Spielrichtung wurde geändert.")

            if len(self.players) == 2:
                self.get_next_player(2)
            else:
                self.get_next_player()

            return

        if card.value == "+2":
            print("Der nächste Spieler zieht 2 Karten.")
            self.get_next_player()

            next_player = self.players[self.current_player]

            for _ in range(2):
                self.draw_card(next_player)

            self.get_next_player()
            return

        if card.value == "+4":
            print("Der nächste Spieler zieht 4 Karten.")
            self.get_next_player()

            next_player = self.players[self.current_player]

            for _ in range(4):
                self.draw_card(next_player)

            self.get_next_player()
            return

        self.get_next_player()

    def human_turn(self, player):
        """Verarbeitet den Spielzug des menschlichen Spielers."""

        playable = self.get_playable_cards(player)

        print("\nDeine Handkarten:")
        player.show_hand()

        if playable:
            print("\nSpielbare Karten:")

            for i in playable:
                print(f"  [{i + 1}] {player.hand[i]}")

        else:
            print("\nDu hast keine spielbare Karte.")

        print("\n[Z] Karte ziehen")
        print("[Q] Spiel beenden")

        while True:
            choice = input("\nDeine Auswahl: ").strip().lower()

            if choice == "q":
                self.game_over = True
                return

            if choice == "z":
                card = self.draw_card(player)

                if card and card.is_playable(
                    self.top_card, self.current_color
                ):
                    print(f"Du kannst {card} spielen.")

                    answer = input(
                        "Möchtest du die Karte spielen? (j/n): "
                    ).strip().lower()

                    if answer == "j":
                        self.play_card(
                            player, len(player.hand) - 1
                        )
                        return

                self.get_next_player()
                return

            if choice.isdigit():
                index = int(choice) - 1

                if 0 <= index < len(player.hand):
                    card = player.hand[index]

                    if card.is_playable(
                        self.top_card, self.current_color
                    ):
                        self.play_card(player, index)
                        return

                print("Diese Karte kannst du nicht spielen.")

            else:
                print("Ungültige Eingabe.")

    def computer_turn(self, player):
        """Einfache Strategie für Computergegner."""

        print(f"\n{player.name} ist am Zug.")

        playable = self.get_playable_cards(player)

        if not playable:
            self.draw_card(player)
            self.get_next_player()
            return

        # Aktionskarten und Joker bevorzugen
        index = max(
            playable,
            key=lambda i: (
                player.hand[i].value in (
                    "Aussetzen",
                    "Richtungswechsel",
                    "+2",
                    "+4",
                    "Joker"
                )
            )
        )

        self.play_card(player, index)

    def play(self):
        """Hauptschleife des Spiels."""

        self.setup_game()

        while not self.game_over:
            self.show_game_state()

            player = self.players[self.current_player]

            print(f"\n>>> {player.name} ist am Zug.")

            if player.is_human:
                self.human_turn(player)
            else:
                self.computer_turn(player)

        print("\n========== SPIELENDE ==========")
        print("Danke fürs Spielen!")


def main():
    print("Willkommen bei UNO!")

    while True:
        try:
            number = int(
                input("Wie viele Spieler (2-4)? ")
            )

            if 2 <= number <= 4:
                break

            print("Bitte eine Zahl zwischen 2 und 4 eingeben.")

        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

    game = UNOGame(number)
    game.play()


if __name__ == "__main__":
    main()
