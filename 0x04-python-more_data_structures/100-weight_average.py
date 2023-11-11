#!/usr/bin/python3

def weight_average(my_list=[]):
    average = 0
    probability = 0
    if not len(my_list):
        return average

    for i in my_list:
        probability += i[1]
    probability = 1 / probability
    for i in my_list:
        average = average + (i[0] * (i[1] * probability))
    return average
