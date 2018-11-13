class Paper:

    def __init__(self):
        self.text = ""

    def write(self, text_to_write):
        self.text += text_to_write

    def write_at(self, text_to_write, index):
        if index > len(self.text):
            self.write(text_to_write)
        elif index + len(text_to_write) > len(self.text):
            slice_index = len(self.text) - index
            self.overwrite(text_to_write[:slice_index], index)
            self.write(text_to_write[slice_index:])
        elif index > 0:
            self.overwrite(text_to_write, index)
        else:
            raise IndexError("Index is below zero.")

    def overwrite(self, text_to_write, index):
        for i in range(index, index + len(text_to_write)):
            if self.text[i].isspace():
                new_char = text_to_write[i - index]
            else:
                new_char = "@"

            self.text = self.text[:i] + new_char + self.text[i + 1:]

    def print_text(self):
        print(self.text)
