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
outcomes = ["Sunny", "Cloudy", "Rainy"] # outcomes of weather to randomly select from
probabilities = [0.4667, 0.4, 0.1333]  # Probabilities must sum to 1, probability of each outcome
# I came up with these values by summing the chance it was sunny based on all 3 previous possible days 
# and then dividing by the total sum of sunny, rainy, cloudy

# Pick Weather on the first day
Weather_init = np.random.choice(outcomes, p=probabilities) # selects randomly the first day of weather based on probabilities 


# Create a list to store the weather sequence
Weather_List = [Weather_init]


# Pick Weather for the next 5 days
for i in range(10): # days shortened to 10 for code run time, for statistical significance run with larger number

# pick the weather based on the previous day's weather. Porbabilities based on the previous days weather
 if Weather_List[i] == "Sunny":
     probabilities = [0.8, 0.2, 0]  # Probabilities must sum to 1
     Weather_tomorrow = np.random.choice(outcomes, p=probabilities) #selects the next day of weather based on the probabilities if the previous day was sunny

 elif Weather_List[i] == "Cloudy":
     probabilities = [0.4, 0.4, 0.2]  # Probabilities must sum to 1
     Weather_tomorrow = np.random.choice(outcomes, p=probabilities) #selects the next day of weather based on the probabilities if the previous day was cloudy

 elif Weather_List[i] == "Rainy":
     probabilities = [0.2, 0.6, 0.2]  # Probabilities must sum to 1 
     Weather_tomorrow = np.random.choice(outcomes, p=probabilities) #selects the next day of weather based on the probabilities if the previous day was rainy

 Weather_List.append(Weather_tomorrow) # adds the weather tomorrow selected by the if-elif statements above

#print("Weather Sequence: ", Weather_List) # used to verify testing

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

"""
Excersise 2.d
What is th estationary distribution based on the state transition matrix?
Did this one by hand, may come back to solve with system of equations functions in python later
"""

# equations written out by hand in my notebook using this as an
# opportunity to practice solving systems of equations in python
A = np.array([
    [1, 1, 1], # sum of propabilites equals to 1
    [-0.2, 0.4, 0.2], # reworking probabilities of it being sunny
    [0.2, -0.6, 0.6] # reworking probabilities of it being cloudy
])
b = np.array([1, 0, 0])

solution = np.linalg.solve(A, b)
print("Probability Sunny Closed form Solution:", solution[0])
print("Probability Cloudy Closed form Solution:", solution[1])
print("Probability Rainy Closed form Solution:", solution[2])

"""
Exerise 2.e
What is the entropy of the stationary distribution
"""
Probability_Sunny = 0.6429
Probability_Cloudy = 0.2857
Probability_Rainy = 0.0714

Hp = - (Probability_Sunny * np.log2(Probability_Sunny) + Probability_Cloudy * np.log2(Probability_Cloudy) + Probability_Rainy * np.log2(Probability_Rainy))
print("Entropy of the Stationary distribution: ", Hp)
