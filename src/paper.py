class Paper:

    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def print_text(self):
        print(self.text)
