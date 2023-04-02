#!/usr/bin/env python3


#I need a 2nd argument, the number of days
#80 is the default given the example and content of output file
def lanternfish_population(filename, days=80):
    # TODO


#read the line from the input file, split by comma, and turn them into lanternfish objects
#instantiate with constructor
#el numero de iteraciones es el numero de dias, el loop corre n veces
#create a list of objects of class Lanternfish
#create methods in lanternfish class to handle the biological timer
#a count() method will get me the end result
    return 0


def main():
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
