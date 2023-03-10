# COMP 202 A1: Part 4
# Footprint of computing and diet
# Author: Davis Cover 260906663

import doctest
from unit_conversion import *

INCOMPLETE = -1

######################################


def fp_of_computing(daily_online_use, daily_phone_use, new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num) -> float

    Metric tonnes of CO2E from computing, based on daily hours of online & phone use, and how many small (phone/tablet/etc) & large (laptop) & workstation devices you bought.

    Source for online use: How Bad Are Bananas
        55 g CO2E / hour

    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day

    Source for new devices: How Bad Are Bananas
        200kg: new laptop
        800kg: new workstation
        And from: https://www.cnet.com/news/apple-iphone-x-environmental-report/
        I'm estimating 75kg: new small device

    >>> fp_of_computing(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_computing(6, 0, 0, 0, 0), 4)
    0.1205
    >>> round(fp_of_computing(0, 1, 0, 0, 0), 4)
    1.25
    >>> fp_of_computing(0, 0, 1, 0, 0)
    0.075
    >>> fp_of_computing(0, 0, 0, 1, 0)
    0.2
    >>> fp_of_computing(0, 0, 0, 0, 1)
    0.8
    >>> round(fp_of_computing(4, 2, 2, 1, 1), 4)
    3.7304
    '''

# this variable stores the hourly amount of CO2E from using a phone as given by the information in the doctest

    hourly_phone_co2e = annual_to_daily(1250)

    fp_new_devices = kg_to_tonnes((200 * new_medium_devices) + (800 * new_heavy_devices) + (75 * new_light_devices))

# I split these two variables up so it would be easier to read.

    fp_activity = kg_to_tonnes(daily_to_annual((daily_online_use * 0.55)/10) + daily_to_annual(daily_phone_use * hourly_phone_co2e))

    return fp_activity + fp_new_devices


######################################

def fp_of_diet(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''
    (num, num, num, num) -> flt
    Approximate annual CO2E footprint in metric tonnes, from diet, based on daily consumption of meat in grams, cheese in grams, milk in litres, and eggs.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.
    I infer approximately 0.0268 kgCO2E/day per gram of meat eaten.

    This calculation misses forms of dairy that are not milk or cheese, such as ice cream, yogourt, etc.

    From How Bad Are Bananas:
        1 pint of milk (2.7 litres) -> 723 g CO2E
                ---> 1 litre of milk: 0.2677777 kg of CO2E
        1 kg of hard cheese -> 12 kg CO2E
                ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E
        12 eggs -> 3.6 kg CO2E
                ---> 0.3 kg CO2E per egg

    >>> round(fp_of_diet(0, 0, 0, 0), 4) # vegan
    1.0556
    >>> round(fp_of_diet(0, 0, 0, 1), 4) # 1 egg
    1.1651
    >>> round(fp_of_diet(0, 0, 1, 0), 4) # 1 L milk
    1.1534
    >>> round(fp_of_diet(0, 0, 1, 1), 4) # egg and milk
    1.2629
    >>> round(fp_of_diet(0, 10, 0, 0), 4) # cheeese
    1.0994
    >>> round(fp_of_diet(0, 293.52, 1, 1), 4) # egg and milk and cheese
    2.5494
    >>> round(fp_of_diet(25, 0, 0, 0), 4) # meat
    1.3003
    >>> round(fp_of_diet(25, 293.52, 1, 1), 4)
    2.7941
    >>> round(fp_of_diet(126, 293.52, 1, 1), 4)
    3.7827
    '''

    vegan_fp = daily_to_annual(kg_to_tonnes(2.89))

    fp_meat = daily_g_meat * 0.0268
    fp_cheese = grams_to_kg(daily_g_cheese * 12)
    fp_milk = daily_L_milk * 0.2677777
    fp_eggs = daily_num_eggs * 0.3
    non_vegan_fp = kg_to_tonnes(daily_to_annual(fp_cheese + fp_eggs + fp_meat + fp_milk))

# I used this statement because of the first doctest being a vegan diet. If your non_vegan_fp is 0, meaning you're a vegan,
# the program will return the yearly vegan value stored in vegan_fp

    if non_vegan_fp != 0:
        return non_vegan_fp + vegan_fp
    else:
        return vegan_fp


#################################################

if __name__ == '__main__':
    doctest.testmod()
