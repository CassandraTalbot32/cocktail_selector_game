# drink selector game
# make all four cocktails whichever one disappears from the list
# needs to be drank

import random
  
cocktail = ['cosmo', 'pina colada', 'caipirinha', 'daiquiri']
randomDrink = random.choice(cocktail)
cocktail.remove(randomDrink)
