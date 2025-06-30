import json
import random


from control.scripts_app import build_menu_and_prompt


def init_usstate():
    dict_state = {'Alabama': 'AL',
                  'Alaska': 'AK',
                  'Arizona': 'AZ',
                  'Arkansas': 'AR',
                  'California': 'CA',
                  'Colorado': 'CO',
                  'Connecticut': 'CT',
                  'Delaware': 'DE',
                  'Florida': 'FL',
                  'Georgia': 'GA',
                  'Hawaii': 'HI',
                  'Idaho': 'ID',
                  'Illinois': 'IL',
                  'Indiana': 'IN',
                  'Iowa': 'IA',
                  'Kansas': 'KS',
                  'Kentucky': 'KY',
                  'Louisiana': 'LA',
                  'Maine': 'ME',
                  'Maryland': 'MD',
                  'Massachusetts': 'MA',
                  'Michigan': 'MI',
                  'Minnesota': 'MN',
                  'Mississippi': 'MS',
                  'Missouri': 'MO',
                  'Montana': 'MT',
                  'North Carolina': 'NC',
                  'North Dakota': 'ND',
                  'Nebraska': 'NE',
                  'Nevada': 'NV',
                  'New Hampshire': 'NH',
                  'New Jersey': 'NJ',
                  'New Mexico': 'NM',
                  'New York': 'NY',
                  'Ohio': 'OH',
                  'Oklahoma': 'OK',
                  'Oregon': 'OR',
                  'Pennsylvania': 'PA',
                  'Rhode Island': 'RI',
                  'South Carolina': 'SC',
                  'South Dakota': 'SD',
                  'Tennessee': 'TN',
                  'Texas': 'TX',
                  'Utah': 'UT',
                  'Vermont': 'VT',
                  'Virginia': 'VA',
                  'Washington': 'WA',
                  'West Virginia': 'WV',
                  'Wisconsin': 'WI',
                  'Wyoming': 'WY'}
    return dict_state


def init_db_capitals():
    dict_capitals = {'Alabama': 'Montgomery',
                     'Alaska': 'Juneau',
                     'Arizona': 'Phoenix',
                     'Arkansas': 'Little Rock',
                     'California': 'Sacramento',
                     'Colorado': 'Denver',
                     'Connecticut': 'Hartford',
                     'Delaware': 'Dover',
                     'Florida': 'Tallahassee',
                     'Georgia': 'Atlanta',
                     'Hawaii': 'Honolulu',
                     'Idaho': 'Boise',
                     'Illinois': 'Springfield',
                     'Indiana': 'Indianapolis',
                     'Iowa': 'Des Moines',
                     'Kansas': 'Topeka',
                     'Kentucky': 'Frankfort',
                     'Louisiana': 'Baton Rouge',
                     'Maine': 'Augusta',
                     'Maryland': 'Annapolis',
                     'Massachusetts': 'Boston',
                     'Michigan': 'Lansing',
                     'Minnesota': 'St. Paul',
                     'Mississippi': 'Jackson',
                     'Missouri': 'Jefferson City',
                     'Montana': 'Helena',
                     'Nebraska': 'Lincoln',
                     'Nevada': 'Carson City',
                     'New Hampshire': 'Concord',
                     'New Jersey': 'Trenton',
                     'New Mexico': 'Santa Fe',
                     'New York': 'Albany',
                     'North Carolina': 'Raleigh',
                     'North Dakota': 'Bismarck',
                     'Ohio': 'Columbus',
                     'Oklahoma': 'Oklahoma City',
                     'Oregon': 'Salem',
                     'Pennsylvania': 'Harrisburg',
                     'Rhode Island': 'Providence',
                     'South Carolina': 'Columbia',
                     'South Dakota': 'Pierre',
                     'Tennessee': 'Nashville',
                     'Texas': 'Austin',
                     'Utah': 'Salt Lake City',
                     'Vermont': 'Montpelier',
                     'Virginia': 'Richmond',
                     'Washington': 'Olympia',
                     'West Virginia': 'Charleston',
                     'Wisconsin': 'Madison',
                     'Wyoming': 'Cheyenne'}
    return dict_capitals


def display_capitals():
    dict_capitals = init_db_capitals()
    print(json.dumps(dict_capitals, indent=4))


def display_abbreviations():
    dict_state = init_usstate()
    print(json.dumps(dict_state, indent=4))


def run_geo_capital_loop(qty_questions):
    correct = 0
    print('Pick the letter of the correct state capital for the provided state')
    dict_capitals = init_db_capitals()

    for i in range(0, qty_questions):
        choices = []
        while len(choices) < 4:
            a = random.randint(1,50)
            if a not in choices:
                choices.append(a)

        # set up possible options
        uss = {}
        ix = 1
        for k, v in dict_capitals.items():
            if ix in choices:
                uss.update({k: v})
            ix += 1

        # pick a random option
        x = random.randint(1,4)
        ix = 1
        this_uss = 'TBD'
        this_cap = 'tbd'
        for k, v in uss.items():
            if ix == x:
                this_uss = k
                this_cap = v
                break
            ix += 1
        capitals = list(uss.values())
        prompt = 'Pick the correct capital of ' + this_uss + ': '
        selection, menu_options = build_menu_and_prompt(capitals, prompt)
        if selection in menu_options.keys():
            user_cap = menu_options[selection]
            if user_cap == this_cap:
                correct += 1
                print('Correct!\n')
            else:
                print('Incorrect. The correct answer was ' + this_cap + '\n')
        else:
            print('Incorrect. The correct answer was ' + this_cap + '\n')

    rate = correct / qty_questions * 100
    print('You got ' + str(correct) + ' correct out of ' + str(qty_questions))
    print('This is a passing rate of ' + str(rate) + '%')
    return


def run_geo_state_loop(qty_questions):
    correct = 0
    print('Pick the letter of the correct US state for the provided capital city')
    dict_capitals = init_db_capitals()

    for i in range(0, qty_questions):
        choices = []
        while len(choices) < 4:
            a = random.randint(1,50)
            if a not in choices:
                choices.append(a)

        # set up possible options
        uss = {}
        ix = 1
        for k, v in dict_capitals.items():
            if ix in choices:
                uss.update({k: v})
            ix += 1

        # pick a random option
        x = random.randint(1,4)
        ix = 1
        this_uss = 'TBD'
        this_cap = 'tbd'
        for k, v in uss.items():
            if ix == x:
                this_uss = k
                this_cap = v
                break
            ix += 1
        usstates = list(uss.keys())
        prompt = 'Pick the correct state for the city of ' + this_cap + ': '
        selection, menu_options = build_menu_and_prompt(usstates, prompt)
        if selection in menu_options.keys():
            user_st = menu_options[selection]
            if user_st == this_uss:
                correct += 1
                print('Correct!\n')
            else:
                print('Incorrect. The correct answer was ' + this_uss + '\n')
        else:
            print('Incorrect. The correct answer was ' + this_uss + '\n')

    rate = correct / qty_questions * 100
    print('You got ' + str(correct) + ' correct out of ' + str(qty_questions))
    print('This is a passing rate of ' + str(rate) + '%')
    return
