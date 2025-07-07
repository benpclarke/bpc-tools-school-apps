
def set_qty_questions():
    prompt = 'Enter a number (for questions in set/multiplication factor): '
    qty_questions = input(prompt)
    try:
        qty_questions = int(qty_questions)
    except ValueError:
        print('Debug: scripts_app.set_qty_questions; defaulting to 10. Invalid entry: ' + qty_questions)
        qty_questions = 10
    return qty_questions


def display_menu(menu, prompt='Select by number: '):
    options = menu.keys()
    format2 = '{0:3} {1:2} {2:20}'
    for entry in options:
        print(format2.format(entry, '::', menu[entry]))
    selection = input(prompt)
    return selection


def build_abcd_menu(list_options):
    menu_options = {}
    alpha = 'a'
    for idx in range(len(list_options)):
        menu_options.update({alpha: list_options[idx]})
        if alpha == 'a': alpha = 'b'
        elif alpha == 'b': alpha = 'c'
        elif alpha == 'c': alpha = 'd'
        elif alpha == 'd': alpha = 'y'
    return menu_options


def build_menu_and_prompt(list_options, prompt):
    menu_options = build_abcd_menu(list_options)
    selection = display_menu(menu_options, prompt)
    return selection, menu_options

