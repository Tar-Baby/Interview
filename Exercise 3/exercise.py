#!/usr/bin/env python3


# I need a 2nd argument, the number of days
# 80 is the default given the example and content of output file
# read the line from the input file, split by comma, and turn them into lanternfish objects
# instantiate with constructor
# the number of iterations is the number of days, the loop executes n times
# create a list of objects of class Lanternfish
# create methods in lanternfish class to handle the biological timer
# a count() method will get me the end result


class Lanternfish:

    def __init__(self, x: int = 9):
        self.timer = x

    def __repr__(self):
        rep = f"{self.timer}"
        return rep

    def breed_countdown(self):
        self.timer = self.timer - 1

    def check_countdown(self, lanternfish_list: list):
        if self.timer == 0:
            self.timer = 7
            lanternfish_list.append(Lanternfish())  # could be improved


def lanternfish_population(filename: str, days=80):
    file_content = []  # list of string values
    lanternfish_school = []  # list of lanternfish-type objects

    with open(filename) as file:
        file_content = file.readline().split(',')

    for element in file_content:
        lanternfish_school.append(Lanternfish(int(element.strip())))

    # loop for lanternfish population
    for temp in range(days):
        for fish in lanternfish_school:
            fish.check_countdown(lanternfish_school)
            fish.breed_countdown()

    return len(lanternfish_school)


def main():
    # result = lanternfish_population("input/input_01.txt", 18)  # quick way to verify results with .txt files
    # print(result)

    with open("output.txt") as f:
        output = [int(x.strip()) for x in f.readlines()]
    for i, expected in enumerate(output):
        filename = f"input/input_{i + 1:02}.txt"
        result = lanternfish_population(filename)
        if result == expected:
            print(f"Correct result for case {i + 1}: {result}")
        else:
            print(f"Incorrect result for case {i + 1}: {expected} is " \
                  f"expected, but {result} is returned")


if __name__ == "__main__":
    main()
