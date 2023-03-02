# pylint: disable=missing-docstring

import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"

def tolist_winter(file):
    winter = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            winter.append(row)
    return winter


def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    athletes = []
    for rec in tolist_winter(MEDALS_FILEPATH):
        athletes.append([rec['Athlete'], rec['Medal']])
    athletes.sort()

    bronz = ['',0,0]
    silv = ['',0,0]
    gold = ['',0,0]

    def count(name, medal):
        if medal == 'Bronze':
            li = bronz
        elif medal == 'Silver':
            li = silv
        else:
            li = gold
        if name == li[0]:
            li[1] += 1
        else:
            li[2] += 1
        if li[2] > li[1]:
            li[0] = recc[0]
            li[1] = li[2]
            li[2] = 0
        breakpoint()

    for recc in athletes:
        count(recc[0], recc[1])


    return bronz, silv, gold






def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    pass  # YOUR CODE HERE

def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    pass  # YOUR CODE HERE


print(most_decorated_athlete_ever())
