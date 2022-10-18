def update_light(current):
    dct = {'red': 'green', 'green': 'yellow', 'yellow': 'red'}
    for x,y in dct.items():
        if x == current:
            print(y)
        
            

update_light('green')