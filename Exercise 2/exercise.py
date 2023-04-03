#!/usr/bin/env python3


def sonar(filename):
    sum_measurements = []  # sum of 3 individual measurements
    measurements = []
    file_content = []
    large_measurements_list = []
    largest_measurement = 0
    count = 0
    index = 0

    with open(filename) as file:
        file_content = file.readlines()

    for element in file_content:
        measurements.append(int(element.strip()))

    # iterating through measurements to group them and add them up
    while index < len(measurements) - 2:
        sum_measurements.append(measurements[index] + measurements[index + 1] + measurements[index + 2])
        index += 1

    while count < len(sum_measurements) - 1:
        if sum_measurements[count + 1] > sum_measurements[count]:
            largest_measurement = sum_measurements[count + 1]
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
