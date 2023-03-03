# pylint: disable=missing-docstring

import sys
import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"


#csv-to-lists-functions:
def tolist_winter(file):
    winter = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            winter.append(row)
    return winter

def tolist_lands(file):
    lands = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lands.append(row)
    return lands


def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    athletes = []
    for rec in tolist_winter(MEDALS_FILEPATH):
        athletes.append([rec['Athlete'], rec['Medal']])
    athletes.sort()

    count = ['', 0, 0, '']
    def counting(name):
        #same leading athlete in a row:
        if name == count[0]:
            count[1] += 1
        #same athlete in a row, but not leading:
        elif name == count[3]:
            count[2] += 1
        #new athlete in the list:
        else:
            count[2],count[3] = 1, name
        #score_check:
        if count[2] > count[1]:
            count[0], count[1], count[2] = count[3], count[2], 0

    for medal in athletes:
        counting(medal[0])

    return count[0]


def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    countries = []
    for rec in tolist_winter(MEDALS_FILEPATH):
        countries.append([rec['Country'], rec['Medal'], rec['Year']])
    countries.sort()

    #counter & counting_func:
    count = ['', 0, 0, '']
    def counting(land):
        #same leading country in a row:
        if land == count[0]:
            count[1] += 1
        #same country in a row, but not leading:
        elif land == count[3]:
            count[2] += 1
        #new country in the list:
        else:
            count[2],count[3] = 1, land
        #score_check:
        if count[2] > count[1]:
            count[0], count[1], count[2] = count[3], count[2], 0

    #filter_loop:
    for country in countries:
        #print('NEXT:::', country)
        if country[1] == 'Gold' and int(max_year) >= int(country[2]) and int(country[2]) <= int(min_year):
            counting(country[0])

    print(count)
    #code to full_country_name:
    for land in tolist_lands(COUNTRIES_FILEPATH):
        if count[0] == land['Code']:
            return print(land['Country'])
        return(print(count[0]))


def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    pass  # YOUR CODE HERE


if __name__ == '__main__':
    country_with_most_gold_medals(sys.argv[1], sys.argv[2])
