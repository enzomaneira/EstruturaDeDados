book = {}

book['maçã'] = 0.67
book['leite'] = 1.49

print(book[input('Insira alimento: ')])


voted = {}
def check_voter(name):
    if voted.get(name):
       print(f'{name} ja votou')
    else:
       voted[name] = True
       print('pode votar!')

check_voter('Enzo')
check_voter('Miguel')
check_voter('Miguel')
