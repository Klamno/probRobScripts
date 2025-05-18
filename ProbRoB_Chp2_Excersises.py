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


# Outcomes and their probabilities
outcomes = ["Sunny", "Cloudy", "Rainy"]
probabilities = [0.4667, 0.4, 0.1333]  # Probabilities must sum to 1

# Pick Weather on the first day
Weather_init = np.random.choice(outcomes, p=probabilities)


# Create a list to store the weather sequence
Weather_List = [Weather_init]


# Pick Weather for the next 5 days
for i in range(10000000):


 if Weather_List[i] == "Sunny":
     probabilities = [0.8, 0.2, 0]  # Probabilities must sum to 1
     Weather_tomorrow = np.random.choice(outcomes, p=probabilities)

 elif Weather_List[i] == "Cloudy":
     probabilities = [0.4, 0.4, 0.2]  # Probabilities must sum to 1
     Weather_tomorrow = np.random.choice(outcomes, p=probabilities)

 elif Weather_List[i] == "Rainy":
     probabilities = [0.2, 0.6, 0.2]  # Probabilities must sum to 1 
     Weather_tomorrow = np.random.choice(outcomes, p=probabilities)

 Weather_List.append(Weather_tomorrow)

#print("Weather Sequence: ", Weather_List)

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

total_days = Sunny_Sum + Cloudy_Sum + Rainy_Sum
print("Total Days: ", total_days)

Probability_Sunny = Sunny_Sum / total_days
Probability_Cloudy = Cloudy_Sum / total_days
Probability_Rainy = Rainy_Sum / total_days

print("Probability of Sunny: ", Probability_Sunny)
print("Probability of Cloudy: ", Probability_Cloudy)
print("Probability of Rainy: ", Probability_Rainy)