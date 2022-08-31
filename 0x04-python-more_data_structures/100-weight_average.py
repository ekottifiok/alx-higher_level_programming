#!/usr/bin/python3

def weight_average(my_list=[]):
    num_sum = 0
    dem_sum = 0
    num_buffer = 1
    if len(my_list) == 0:
        return 0
    for i in my_list:
        for j in i:
            num_buffer *= j
        dem_sum += i[-1]
        num_sum += num_buffer
        num_buffer = 1

    return num_sum / dem_sum
