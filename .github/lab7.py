# Programmers: Aidan & Nicol
# Course: CS151, Dr. Rajeev
# Date: 11/4/2021
# Lab Number: 7
# Program Inputs: How many times the dice was rolled
# Program Outputs: How many times a number was rolled

# Problem Write a program which, given a number, simulates rolling a pair of six-sided dice that number of times.
# The program should keep track of how many times each possible sum comes up using a list. The
# list's first element should contain how many times a total of 2 was rolled, the second should contain how many times
# a total of 3 was rolled, and so on all the way through to 12. When all rolls are complete, the program should output
# the resulting list as well as a chart as shown in the example below, where the number of asterisks represents the
# number of times that roll came up (results will vary with each run). In this example, the user requested the dice
# be rolled 100 times:

# Resulting list: [2, 8, 11, 11, 15, 15, 17, 9, 7, 4, 1]

# Resulting chart:

# 2 **
# 3 ********
# 4 ***********
# 5 ***********
# 6 ***************
# 7 ***************
# 8 *****************
# 9 *********
# 10 *******
# 11 ****
# 12 * Input validation: Do not accept a non-integer input for the number of dice rolls to simulate.

import random
roll = input("How many times would you like to roll the dice?")

if int(roll) > 0:
    list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(int(roll)):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        total = d1 + d2
        if total == 2:
            list[0] = list[0]+1
        elif total == 3:
            list[1] = list[1]+1
        elif total == 4:
            list[2] = list[2]+1
        elif total == 5:
            list[3] = list[3]+1
        elif total == 6:
            list[4] = list[4]+1
        elif total == 7:
            list[5] = list[5]+1
        elif total == 8:
            list[6] = list[6]+1
        elif total == 9:
            list[7] = list[7]+1
        elif total == 10:
            list[8] = list[8]+1
        elif total == 11:
            list[9] = list[9]+1
        elif total == 12:
            list[10] = list[10]+1

    print("Resulting list : ", list)

    print("\nResulting chart")

    for i in range(len(list)):
        a = ""
        a = a + str(i + 2) + " "
        for j in range(list[i]):
            a = a + "*"
        print(a)
else:
    print("Invalid number")
