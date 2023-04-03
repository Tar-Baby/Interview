#!/usr/bin/env python3


def sonar(filename):
    measurements = []
    file_content = []
    large_measurements_list = []
    largest_measurement = 0
    count = 0

    with open(filename) as file:
        file_content = file.readlines()

    for element in file_content:
        measurements.append(int(element))

    while count < len(measurements) - 1:
        if measurements[count + 1] > measurements[count]:
            largest_measurement = measurements[count + 1]
            large_measurements_list.append(largest_measurement)
        count += 1

    return len(large_measurements_list)


def main():
    with open("output.txt") as f:
        output = [int(x.strip()) for x in f.readlines()]
    for i, expected in enumerate(output):
        filename = f"input/input_{i + 1:02}.txt"
        result = sonar(filename)
        if result == expected:
            print(f"Correct result for case {i + 1}: {result}")
        else:
            print(f"Incorrect result for case {i + 1}: {expected} is " \
                  f"expected, but {result} is returned")


if __name__ == "__main__":
    main()
