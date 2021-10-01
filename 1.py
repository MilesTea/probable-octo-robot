import requests
from pprint import pprint


def _get_id(name):
    url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
    response = requests.get(url=url, timeout=5)
    respjs = response.json()
    count = 0
    if respjs['response'] == 'error':
        print(f'{name} Not Found')
        return
    for hero in respjs['results']:
        if hero['name'].lower() == name.lower():
            target = hero['id']
            count += 1
    if count == 0:
        print(f'{name} Not Found')
    elif count >= 2:
        print(f'Warning. Multiple heroes share name {name}')
        return target
    else:
        return target


def get_intell(name):
    char_id = _get_id(name)
    if not char_id:
        print(f'error: no id set for {name}')
        return
    url = f'https://superheroapi.com/api/2619421814940190/{char_id}/powerstats'
    response = requests.get(url=url, timeout=5)
    respjs = response.json()
    intell = respjs['intelligence']
    return intell


def who_is_smarter(hero_list):
    max_intelligence = 0
    length = 0
    intelligence_dict = dict()
    for hero in hero_list:
        intelligence = int(get_intell(hero))
        intelligence_dict[hero] = intelligence
        if intelligence > max_intelligence:
            max_intelligence = intelligence
            smartest_heroes = [hero]
            length = len(hero)
        elif intelligence == max_intelligence:
            smartest_heroes.append(hero)
            if len(hero) > length:
                length = len(hero)
    print('Smartest:')
    print('Name:'.ljust(length+2), 'intelligence:')
    for hero in smartest_heroes:
        print(hero.ljust(length+2), intelligence_dict[hero])


if __name__ == '__main__':
    who_is_smarter(['Hulk', 'Captain America', 'Thanos'])
