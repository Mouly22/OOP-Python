class buttons:
    def __init__(self, word, spaces, border):
        self.word = ''
        self.spaces = 0
        self.border = ''
        calculate = 1 + spaces + len(word) + spaces + 1
        print(f"{word} Button Specifications:")
        print(f"Button name: {word}")
        print(f"Number of the border characters for the top and the bottom: {calculate}")
        print(f"Number of spaces between the left side border and the first character of the button name: {spaces}")
        print(f"Number of spaces between the right side border and the last character of the button name: {spaces}")
        print(f"Characters representing the borders:{border}")
        print(calculate * border)
        a = ((calculate - len(word))-2)//2
        g = ((calculate - (calculate// len(word)))//2) - len(word)   
        print(f"{border}{a * ' '}{word}{a * ' '}{border}")
        print(f"{border* calculate}")
word = "CANCEL"
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')