#!/usr/bin/env python
# ===============================================================================
# Apps_Nokia_Main
#
# Description:
#   Menu function to run AsBuilt parsers and validation scripts
#
# Version:
#   MM.mm   DD/MM/YY
#   00.00   26/06/25    First version (from AsBuilt_Nokia v0.03)
#
# Example/Usage:
#
#
# ===============================================================================

import re

from control import scripts_app

from src.scripts_math import (run_math_addition_loop, run_math_subtraction_loop,
                              run_math_multiplication_loop,
                              run_math_division_loop)
from src.scripts_geography import (display_capitals, display_abbreviations,
                                   run_geo_capital_loop, run_geo_state_loop)


def display_main_menu(menu, config_string, qty_questions=5):
    options = menu.keys()
    format1 = '{0:3} {1:2} {2:30} {3:3} {4:}'
    format2 = '{0:3} {1:2} {2:30}'

    print("MENU OPTIONS")
    print('Key    Task                              Flag/Notes')
    print('---    -------------------------------   ------------------')
    for entry in options:
        try:
            if isinstance(entry, int):
                print(format1.format(entry, '::', menu[entry], '>>', config_string[entry]))
            elif entry == 'W':
                print(format1.format(entry, '::', menu[entry], '::', str(qty_questions)))
            else:
                print(format2.format(entry, '::', menu[entry]))
        except KeyError:
            print(format2.format(entry, '::', menu[entry]))
    print('\n')


def execute_menu(menu, config_string, qty_questions=10):
    # runs menu with a while loop
    while True:
        display_main_menu(menu, config_string)
        selection = input('Please Select A Task (by typing a number/letter):')
        selFunction = {'0': lambda: build_menu_math(qty_questions),
                       '1': lambda: build_menu_geography(qty_questions),

                       'Q': terminate,
                       'q': terminate,
                       '42': terminate42}

        if selection in selFunction.keys():
            if selection in ['Q', 'q', '42']:
                selFunction[selection]()
                break
            else:
                selFunction[selection]()
        else:
            print("Please Choose A Valid Task!\n")


def execute_menu_math(menu, config_string, qty_questions):
    # runs menu with a while loop
    while True:
        display_main_menu(menu, config_string, qty_questions)

        selection = input('Please Select A Task (by typing a number/letter):')
        selFunction = {'0': lambda: run_math_addition_loop(qty_questions),
                       '1': lambda: run_math_subtraction_loop(qty_questions),
                       '2': lambda: run_math_multiplication_loop(qty_questions),
                       '3': lambda: run_math_division_loop(qty_questions),
                       'W': lambda: scripts_app.set_qty_questions(),
                       'w': lambda: scripts_app.set_qty_questions()}
        if selection in ['Z', 'z']:
            break
        elif selection in ['W', 'w']:
            qty_questions = selFunction[selection]()
        elif selection in selFunction.keys():
            selFunction[selection]()
        else:
            print("Please Choose A Valid Task!\n")


def execute_menu_geo(menu, config_string, qty_questions):
    # runs menu with a while loop
    while True:
        display_main_menu(menu, config_string, qty_questions)

        selection = input('Please Select A Task (by typing a number/letter):')
        selFunction = {'0': lambda: run_geo_capital_loop(qty_questions),
                       '1': lambda: run_geo_state_loop(qty_questions),
                       'A': lambda: display_capitals(),
                       'a': lambda: display_capitals(),
                       'B': lambda: display_abbreviations(),
                       'b': lambda: display_abbreviations(),
                       'W': lambda: scripts_app.set_qty_questions(),
                       'w': lambda: scripts_app.set_qty_questions()}
        if selection in ['Z', 'z']:
            break
        elif selection in ['W', 'w']:
            qty_questions = selFunction[selection]()
        elif selection in selFunction.keys():
            selFunction[selection]()
        else:
            print("Please Choose A Valid Task!\n")


def terminate():
    print('program terminated\n')
    return False


def terminate42():
    print('This is the answer to everything')
    return False


def build_menu_math(qty_questions):
    menu = {0: 'Addition',
            1: 'Subtraction',
            2: 'Multiplication',
            3: 'Division',
            'W': 'Number of Questions in Set',
            'Z': 'Main menu'}

    execute_menu_math(menu, {}, qty_questions)


def build_menu_geography(qty_questions):
    menu = {0: 'Capitals',
            1: 'States',
            'A': 'Display States & Capitals',
            'B': 'Display State Abbreviations',
            'W': 'Number of Questions in Set',
            'Z': 'Main menu'}

    execute_menu_geo(menu, {}, qty_questions)


def build_main_menu():
    # build dictionary to hold menu options
    menu = {0: 'Math',
            1: 'Geography',
            'Q': 'Exit Program'}

    config_string = {0: 'Sub-menu for math testing',
                     1: 'Sub-menu for geopgraphy'}

    execute_menu(menu, config_string)


def main():
    # call build menu method
    build_main_menu()


if __name__ == '__main__':
    main()
