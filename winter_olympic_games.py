# pylint: disable=missing-docstring

import sys
import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"


#csv-to-list-functions:
def tolist(file):
    csv_list = []
    with open(file, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_list.append(row)
    return csv_list

#counting_funtion:
def counting(counter, item):
    #count x in a row, as champ:
    if item == counter[0]:
        counter[1] += 1
    #count x in a row, not as champ:
    elif item == counter[3]:
        counter[2] += 1
    #new canidate in the list:
    else:
        counter[2],counter[3] = 1, item
    #champ_check, if new switch the numbers:
    if counter[2] > counter[1]:
        counter[0], counter[1], counter[2] = counter[3], counter[2], 0


def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    #creating an informative list with needed details:
    athletes = []
    for rec in tolist(MEDALS_FILEPATH):
        athletes.append([rec['Athlete'], rec['Medal']])
    athletes.sort()

    #counter & filter_loop:
    count = ['', 0, 0, '']
    for medal in athletes:
        counting(count, medal[0])
        print(count)
    return count[0]


def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    #creating an informative list with needed details:
    countries = []
    for rec in tolist(MEDALS_FILEPATH):
        countries.append([rec['Country'], rec['Medal'], rec['Year']])
    countries.sort()

    #nulling counter & filter_loop:
    count = ['', 0, 0, '']
    for country in countries:
        max_y = int(max_year) >= int(country[2])
        min_y = int(country[2]) >= int(min_year)
        if country[1] == 'Gold' and max_y and min_y:
            counting(count, country[0])

    #code to full_country_name:
    for land in tolist(COUNTRIES_FILEPATH):
        if count[0] == land['Code']:
            return land['Country']


def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    #creating an informative list with needed details:
    women = []
    for rec in tolist(MEDALS_FILEPATH):
        if rec['Gender'] == 'Women' and rec['Event'] == '5000M':
            women.append([rec['Athlete']])
    women.sort()
    women.reverse()

    #nulling counter & filter_loop:
    winners = []
    for loop in range(3):
        count = ['', 0, 0, '']
        for woman in women:
            counting(count, woman[0])
        winners.append(count[0])
        print(count)
        #print('WINNERS:::', winners)
        women = [x for x in women if x != [count[0]]]
    return winners





if __name__ == '__main__':
    print(country_with_most_gold_medals(sys.argv[1], sys.argv[2]))
