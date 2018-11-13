class Pencil:

    def __init__(self):
        self.current_length = 0
        self.current_tip_durability = 0
        self.max_tip_durability = 0

    def set_length(self, length):
        self.current_length = length

    def set_max_tip_durability(self, amount):
        self.max_tip_durability = amount

    def sharpen(self):
        if self.current_length > 0:
            self.current_length -= 1
            self.current_tip_durability = self.max_tip_durability
