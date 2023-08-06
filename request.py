from time import sleep as wait
from addict import Dict
import requests
import random

# to increase the chance of new games raise the default value (250k) to a greater integer, to increase the chance of
# anything good due to bots and the inflation of the roblox community itself.

"""
 12 (2004 games)
 154 (2005 games)
 11k (2006 games)
 130k (2007 games)
 1.7m (2008 games)
 5.8m (2009 games)
 13m (2010 games)
 22m (2011 games)
 36m (2012 games)
 53m (2013 games)
 75m (2014 games)
 103m (2015 games)
 205m (2016 games)
 478m (2017 games)
 915m (2018 games)
 1.3b (2019 games)
 2.2b (2020 games)
 3.1b (2021 games)
 3.6b (2022 games)
"""

dates = {
    2004: 12,
    2005: 154,
    2006: 1100,
    2007: 130000,
    2008: 1700000,
    2009: 5800000,
    2010: 13000000,
    2011: 22000000,
    2012: 36000000,
    2013: 53000000,
    2014: 75000000,
    2015: 103000000,
    2016: 205000000,
    2017: 478000000,
    2018: 915000000,
    2019: 1300000000,
    2020: 2200000000,
    2021: 3100000000,
    2022: 3600000000,
    2023: 4800000000
}

value = dates[2015]

while True is True and not False or None: # kill me
    randomint = random.randint(0, value)
    try:
        url = f'https://games.roblox.com/v2/users/{randomint}/games?accessFilter=Public&sortOrder=Asc&limit=10'
    except IndexError:
        # some mfs put special unicodes in their games and that stops the script
        pass

    name_api = f'https://users.roblox.com/v1/users/{randomint}'
    response = requests.get(url)
    games = Dict(response.json())
    delay = 1

    # main vars
    try:
        data = games.data[0]['rootPlace']['id'], games.data[0]['name'], games.data[0]['placeVisits'], \
                      games.data[0]['description'], games.data[0]['created'], games.data[0]['updated']
    except IndexError:
        # line 35
        pass

    print(f'{data[1]}\n')

    path = 'games.txt'

    # blacklist and file handler
    if '\'' not in data[1]:
        try:
            print(f'saved to {path}\n')
            with open(path, 'a') as file:
                file.write(f'{data[1]}\nhttps://www.roblox.com/games/{data[0]}\nDescription: {data[3]}\nVisits: {data[2]}\n\n')
                file.close()
        except UnicodeEncodeError:
            print('game ignored due to error')
            pass
    wait(delay/5)