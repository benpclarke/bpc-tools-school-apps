import random


def run_math_addition_loop(qty_questions):
    correct = 0
    print('Solve these ' + str(qty_questions) + ' Addition problems')
    for i in range(0, qty_questions):
        a = random.randint(0, 25)
        z = random.randint(0, 25)
        prompt = input(str(a) + ' + ' + str(z) + ':')
        result = a + z
        if result == int(prompt):
            correct += 1
    rate = correct/qty_questions * 100
    print('You got ' + str(correct) + ' correct out of ' + str(qty_questions))
    print('This is a passing rate of ' + str(rate) + '%')


def run_math_subtraction_loop(qty_questions):
    correct = 0
    print('Solve these ' + str(qty_questions) + ' Subtraction problems')
    for i in range(0, qty_questions):
        a = random.randint(0, 25)
        z = random.randint(0, 25)
        result = a + z
        prompt = input(str(result) + ' - ' + str(z) + ':')
        if a == int(prompt):
            correct += 1
    rate = correct/qty_questions * 100
    print('You got ' + str(correct) + ' correct out of ' + str(qty_questions))
    print('This is a passing rate of ' + str(rate) + '%')


def run_math_multiplication_loop(qty_questions):
    correct = 0
    print('Solve these ' + str(qty_questions) + ' Multiplication problems')
    for i in range(0, qty_questions):
        a = random.randint(0, 12)
        z = random.randint(0, 12)
        prompt = input(str(a) + ' x ' + str(z) + ':')
        result = a * z
        if result == int(prompt):
            correct += 1
    rate = correct/qty_questions * 100
    print('You got ' + str(correct) + ' correct out of ' + str(qty_questions))
    print('This is a passing rate of ' + str(rate) + '%')


def run_math_division_loop(qty_questions):
    correct = 0
    print('Solve these ' + str(qty_questions) + ' Multiplication problems')
    for i in range(0, qty_questions):
        a = random.randint(0, 12)
        z = random.randint(0, 12)
        result = a * z
        prompt = input(str(result) + ' / ' + str(z) + ':')
        if a == int(prompt):
            correct += 1
    rate = correct/qty_questions * 100
    print('You got ' + str(correct) + ' correct out of ' + str(qty_questions))
    print('This is a passing rate of ' + str(rate) + '%')
