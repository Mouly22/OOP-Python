class Wadiya():
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True

wadiya = Wadiya()
print('Part 1:')
print('Name of President:', wadiya.name)
print('Designation:', wadiya.designation)
print("Number of wife:", wadiya.num_of_wife)
print("Is he/she a dictator:", wadiya.dictator)
wadiya2 = Wadiya()
wadiya2.name = "Donald Trump"
wadiya2.designation = "President"
wadiya2.num_of_wife = 1
wadiya2.dictator = False
print('Part 2:')
print("Name of President:", wadiya2.name)
print("Designation:", wadiya.designation)
print("Number of wife:", wadiya.num_of_wife)
print("Is he/she a dictator:", wadiya.dictator)