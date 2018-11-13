class Paper:

    def __init__(self):
        self.text = ""

    def write(self, text_to_write):
        self.text += text_to_write

    def write_at(self, text_to_write, index):
        for i in range(index, index + len(text_to_write)):
            if self.text[i].isspace():
                new_char = text_to_write[i - index]
            else:
                new_char = "@"

            self.text = self.text[:i] + new_char + self.text[i + 1:]

    def print_text(self):
        print(self.text)
