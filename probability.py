import numpy as np

def main():
    numbers,percentage = get_numbers()
    do_math(numbers,percentage)

def get_numbers():
    math_problem = input("How many succesfull out of how many unsuccessful? ")
    numbers = []
    for word in math_problem:
        if word.isnumeric():
            numbers.append(int(word))
        else:
            continue
    percentage = input("What is the percentage of a succuss? ")
    percentage_number = ""
    for character in percentage:
        if character.isnumeric():
            percentage_number += character
        else:
            continue
    return numbers, percentage

def do_math(numbers,percentage):
    
