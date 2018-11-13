class Eraser:

    def __init__(self):
        self.current_durability = 0

    def set_durability(self, amount):
        self.current_durability = amount

    def erase(self, paper, text_to_erase):
        text_cost = 0
        old_text = ""
        new_text = ""

        for c in text_to_erase[::-1]:
            if c.isspace():
                old_text += c
                new_text += " "
            else:
                text_cost += 1
                if self.current_durability >= text_cost:
                    old_text += c
                    new_text += " "

        self.current_durability -= text_cost

        paper.text = paper.text[::-1].replace(old_text, new_text, 1)[::-1]
