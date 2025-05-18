"""
Author: Alex Garrow
Script: ProbRoB_Chp2_Excersises.py
Description: This script is to work through the exercises in Chapter 2 of "Probabilistic Robotics".
Date: 2025-05-17
"""

import numpy as np


"""
Exercise 2.b
Random Weather Sequence Generator
The weather can be either sunny, cloudy, or rainy.
"""


# Pick Weather on the first day
rand_int_init = np.random.randint(1, 4)

if rand_int_init == 1:
     Weather_init = "Sunny"
elif rand_int_init == 2:
     Weather_init = "Cloudy"
elif rand_int_init == 3:
     Weather_init = "Rainy"

# Create a list to store the weather sequence
Weather_List = [Weather_init]


# Pick Weather for the next 5 days
for i in range(5):

 rand_int = np.random.randint(1, 4)

 if rand_int == 1:
     Weather_tomorrow = "Sunny"
 elif rand_int == 2:
     Weather_tomorrow = "Cloudy"
 elif rand_int == 3:
     Weather_tomorrow = "Rainy"

 Weather_List.append(Weather_tomorrow)

print("Weather Sequence: ", Weather_List)

"""
Exercise 2.c
Calculate the stationary distribution of this markov chain
"""

# initialize the sums
Sunny_Sum = 0
Cloudy_Sum = 0
Rainy_Sum = 0

# Count the number of each weather type
for day in Weather_List:
    if day == "Sunny":
        Sunny_Sum += 1
    elif day == "Cloudy":
        Cloudy_Sum += 1
    elif day == "Rainy":
        Rainy_Sum += 1

print("Sunny: ", Sunny_Sum)
print("Cloudy: ", Cloudy_Sum)
print("Rainy: ", Rainy_Sum)