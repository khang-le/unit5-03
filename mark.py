#!/usr/bin/env python3

# Created by: Khang Le
# Created on: November 2019
# This program shows mark percentage


def calculate_percentage(user_input):
    # level to percentage converter

    percentage_mark = None

    if user_input == "4+":
        percentage_mark = 97
    elif user_input == "4":
        percentage_mark = 90
    elif user_input == "3+":
        percentage_mark = 79
    elif user_input == "3":
        percentage_mark = 76
    elif user_input == "2+":
        percentage_mark = 69
    elif user_input == "2":
        percentage_mark = 66
    elif user_input == "1+":
        percentage_mark = 59
    elif user_input == "1":
        percentage_mark = 56
    elif user_input == "0+":
        percentage_mark = 49
    elif user_input == "0":
        percentage_mark = 39
    else:
        percentage_mark = -1

    return percentage_mark


def main():
    # solution

    user_input1 = input("Enter your level: ")
    calculated = calculate_percentage(user_input1)
    print("Your mark percentage is: {}".format(calculated))


if __name__ == "__main__":
    main()
