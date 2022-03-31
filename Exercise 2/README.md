# Exercise 2

Considering every single measurement isn't as useful as you expected: there’s just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the example of the previous exercise:

```
199  A
200  A B
208  A B C
210    B C D
200  E   C D
207  E F   D
240  E F G
269    F G H
260      G H
263        H
```

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked `A (199, 200, 208)`; their sum is `199 + 200 + 208 = 607`. The second window is marked `B (200, 208, 210)`; its sum is `618`. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare `A` with `B`, then compare `B` with `C`, then `C` with `D`, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

```
A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
```

In this example, there are 5 sums that are larger than the previous sum.



## Assignment
Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum? Determine this in the following way:

Write a function `sonar` that takes the pathname (of type `str`) of a text file containing a sonar sweep report. Each line of the report is a measurement of the sea floor depth. The function must return the number of sums (of type `int`) that are larger than the previous sum in a three-measurement sliding window.



## Example

In this interactive session we assume the text files `input_01.txt` and `input_02.txt` to be located in the current directory.

```
>>> sonar('input_01.txt')
5
>>> sonar('input_02.txt')
1737
```
