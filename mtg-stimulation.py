import random

class Card:
    def __init__(self, name, power, toughness):
        self.name = name
        self.power = power
        self.toughness = toughness

class Player:
    def __init__(self, name):
        self.name = name
        self.life_total = 20
        self.hand = []

def simulate_game(player1, player2):
    # Simulate a basic game
    while player1.life_total > 0 and player2.life_total > 0:
        # Simulate a turn
        draw_card(player1)
        play_card(player1)

        draw_card(player2)
        play_card(player2)

        # Simulate combat
        combat(player1, player2)

    # Determine the winner
    if player1.life_total <= 0:
        return f"{player2.name} wins!"
    elif player2.life_total <= 0:
        return f"{player1.name} wins!"

def draw_card(player):
    # Simulate drawing a card
    card = Card(f"Card_{len(player.hand) + 1}", random.randint(1, 5), random.randint(1, 5))
    player.hand.append(card)
    print(f"{player.name} draws {card.name}")

def play_card(player):
    # Simulate playing a card
    if player.hand:
        card_to_play = random.choice(player.hand)
        player.hand.remove(card_to_play)
        print(f"{player.name} plays {card_to_play.name}")
    else:
        print(f"{player.name}'s hand is empty")

def combat(attacker, defender):
    # Simulate combat
    print(f"{attacker.name} attacks {defender.name}")
    damage = attacker.hand[0].power
    defender.life_total -= damage
    print(f"{defender.name} loses {damage} life. {defender.name}'s life total: {defender.life_total}")

# Example usage
player1 = Player("Player 1")
player2 = Player("Player 2")

result = simulate_game(player1, player2)
print(result)
