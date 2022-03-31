# Exercise 1

As a submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263

This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you’re dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)

In this example, there are 7 measurements that are larger than the previous measurement.



## Assignment

How many measurements are larger than the previous measurement? Determine this in the following way:

Write a function sonar that takes the pathname (of type str) of a text file containing a sonar sweep report. Each line of the report is a measurement of the sea floor depth. The function must return the number of measurements (of type int) that are larger than the previous measurement.



## Example
In this interactive session we assume the text files sweep01.txt and sweep02.txt to be located in the current directory.

```
>>> sonar('sweep01.txt')
7
>>> sonar('sweep02.txt')
1696
```
