import turtle
import time
import random

wn = turtle.Screen()   # Turtle Screen
wn.bgcolor("#429206")
wn.setup(800, 600)
wn.title("Deck of cards simulator")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
class CharacterPen():
    def __init__(self, color="white", scale=1.0):
        self.color = color
        self.scale = scale

        self.characters = {}
        self.characters["1"] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["2"] = ((-5, 10), (5, 10), (5, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["3"] = ((-5, 10), (5, 10), (5, 0), (0, 0), (5, 0), (5, -10), (-5, -10))
        self.characters["4"] = ((-5, 10), (-5, 0), (5, 0), (2, 0), (2, 5), (2, -10))
        self.characters["5"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10))
        self.characters["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
        self.characters["7"] = ((-5, 10), (5, 10), (0, -10))
        self.characters["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
        self.characters["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
        self.characters["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))

        self.characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
        self.characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5, 0), (5, -10), (-5, -10))
        self.characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
        self.characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
        self.characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
        self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
        self.characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
        self.characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))
        self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
        self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
        self.characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
        self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
        self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
        self.characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
        self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
        self.characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
        self.characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10))
        self.characters["V"] = ((-5, 10), (0, -10), (5, 10))
        self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10))
        self.characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))
        self.characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))
        self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0, 0), (0, -10))
        self.characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))

        self.characters["-"] = ((-3, 0), (3, 0))

    def draw_string(self, pen, str, x, y):
        pen.width(2)
        pen.color(self.color)

        # Center text
        x -= 15 * self.scale * ((len(str) - 1) / 2)
        for character in str:
            self.draw_character(pen, character, x, y)
            x += 15 * self.scale

    def draw_character(self, pen, character, x, y):
        scale = self.scale

        if character in "abcdefghijklmnopqrstuvwxyz":
            scale *= 0.8

        character = character.upper()

        # Check if the character is in the dictionary
        if character in self.characters:
            pen.penup()
            xy = self.characters[character][0]
            pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.pendown()
            for i in range(1, len(self.characters[character])):
                xy = self.characters[character][i]
                pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.penup()

# Splash Screen
character_pen = CharacterPen("#4E1CA5", 3.0)
character_pen.draw_string(pen, "CARD GAME", 0, 200)

character_pen.scale = 1.0
character_pen.draw_string(pen, "BY MIKE", 0, 100)

character_pen.scale = 1.0
character_pen.draw_string(pen, "Sum up the values", 0, 60)

character_pen.scale = 1.0
character_pen.draw_string(pen, "compare them", 0, 30)

character_pen.scale = 1.0
character_pen.draw_string(pen, "and win", 0, 0)

character_pen.scale = 1.0
character_pen.draw_string(pen, "PRESS space TO SHUFFLE", 0, -40)

character_pen.scale = 1.0
character_pen.draw_string(pen, "CARDS", 0, -70)

character_pen.scale = 1.0
character_pen.draw_string(pen, "PRESS 1 TO END GAME", 0, -240)

time.sleep(3)
pen.clear()

class Card():
    def __init__(self, name, suit):
         self.name = name
         self.suit = suit
         self.symbols = {"D": "♦", "C": "♣", "H": "♥", "S": "♠", }

    def print_card(self):
        print(f"{self.name}{self.symbols[self.suit]}")

    def render(self, x, y, pen):
        pen.penup()
        pen.goto(x, y)
        pen.color("white")
        pen.goto(x-50, y+75)
        pen.pendown()
        pen.begin_fill()
        pen.goto(x+50, y+75)
        pen.goto(x+50, y-75)
        pen.goto(x-50, y-75)
        pen.goto(x-50, y+75)
        pen.end_fill()
        pen.penup()
        if self.name != "":
            pen.color("black")
            pen.goto(x-22, y-30)
            pen.write(self.symbols[self.suit], False, font=('Helvetica', 48, 'normal'))

            # Draw top left
            pen.goto(x-40, y+47)
            pen.write(self.name, False, font=('Helvetica', 18, 'normal'))
            pen.goto(x-42, y+28)
            pen.write(self.symbols[self.suit], False, font=('Helvetica', 18, 'normal'))

            # Draw right buttom
            pen.goto(x+31, y-52)
            pen.write(self.name, False, font=('Helvetica', 18, 'normal'))
            pen.goto(x+30, y-70)
            pen.write(self.symbols[self.suit], False, font=('Helvetica', 18, 'normal'))

class Deck():
    def __init__(self):
        self.cards = []

        names = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")
        suits = ("D", "C", "H", "S")

        for name in names:
            for suit in suits:
                card = Card(name, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        card = self.cards.pop()
        return card

    def reset(self):
        self.cards = []

        names = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")  # change the names into values
        suits = ("D", "C", "H", "S")

        for name in names:
            for suit in suits:
                card = Card(name, suit)
                self.cards.append(card)
        self.shuffle()

# craete a new card and render reshuffle method in there
#Create Deck
deck = Deck()

# Shuffle
deck.reset()

#Render cards
def update():
    start_x = -250
    for x in range(5):
        card = Card("", "")
        card.render(start_x + x * 125, 0, pen)

    # Render 5 cards in a row
    start_x = -250
    for x in range(5):
        card = deck.get_card()
        card.render(start_x + x * 125, 0, pen)

wn.listen(xdummy=None, ydummy=None)
wn.onkey(update, "space")

def quit():
    pen.clear()
    character_pen = CharacterPen("#4E1CA5", 3.0)
    character_pen.draw_string(pen, "THANK YOU", 0, 100)

wn.listen(xdummy=None, ydummy=None)
wn.onkey(quit, "1")


wn.mainloop()

