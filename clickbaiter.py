import random
import sys

def generate_title():
    template_titles = open('wordlists/template_titles').read().splitlines()
    game = open('wordlists/games').read().splitlines()
    person = open('wordlists/person').read().splitlines()
    subject = open('wordlists/subject').read().splitlines()
    item = open('wordlists/item').read().splitlines()
    gameitem = open('wordlists/gameitem').read().splitlines()
    action = open('wordlists/action').read().splitlines()
    ending = open('wordlists/ending').read().splitlines()
    place = open('wordlists/place').read().splitlines()

    title = random.choice(template_titles)
    lowercase = title.split('/')[0] == 'l'
    title = title[2:]

    if random.randint(1, 2) == 1:
        title += ' ' + random.choice(ending)

    while '$gameitem' in title:
        title = title.replace('$gameitem', random.choice(gameitem), 1)
    while '$game' in title:
        title = title.replace('$game', random.choice(game), 1)
    while '$person' in title:
        title = title.replace('$person', random.choice(person), 1)
    while '$subject' in title:
        title = title.replace('$subject', random.choice(subject), 1)
    while '$item' in title:
        title = title.replace('$item', random.choice(item), 1)
    while '$action' in title:
        title = title.replace('$action', random.choice(action), 1)
    while '$place' in title:
        title = title.replace('$place', random.choice(place), 1)

    if lowercase:
        title = title.lower()
    else:
        title = title.upper()
    return title

if len(sys.argv) < 2:
    count = 1
else:
    count = int(sys.argv[1])

for i in range(count): print("Your video's title should be :", generate_title())

