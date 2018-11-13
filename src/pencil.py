import string

from src.eraser import Eraser


class Pencil:

    LOWER_LETTER_COST = 1
    PUNCTUATION_COST = 1
    UPPER_LETTER_COST = 2
    WHITE_SPACE_COST = 0

    def __init__(self):
        self.current_length = 0
        self.current_tip_durability = 0
        self.eraser = Eraser()
        self.max_tip_durability = 0

        self.eraser.set_durability(0)

    def set_length(self, length):
        self.current_length = length

    def set_max_tip_durability(self, amount):
        self.max_tip_durability = amount

    def sharpen(self):
        if self.current_length > 0:
            self.current_length -= 1
            self.current_tip_durability = self.max_tip_durability

    def write(self, paper, text_to_write):
        text = ""

        for c in text_to_write:
            if c.isupper():
                letter_cost = Pencil.UPPER_LETTER_COST
            elif c.islower():
                letter_cost = Pencil.LOWER_LETTER_COST
            elif c in string.punctuation:
                letter_cost = Pencil.PUNCTUATION_COST
            else:
                letter_cost = Pencil.WHITE_SPACE_COST

            if self.current_tip_durability >= letter_cost:
                text += c
                self.current_tip_durability -= letter_cost
            else:
                text += " "

        paper.write(text)
