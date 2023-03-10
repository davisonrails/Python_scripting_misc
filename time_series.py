# Davis Cover
# 260906663

from datetime import datetime
from initial_clean import *
import math
import matplotlib.pyplot as plt


def date_diff(first_date, second_date):
    '''(str, str) -> int
    How many days apart the first and second dates are as integers.

    >>> date_diff('2019-10-31', '2019-11-2')
    2
    >>> date_diff('2018-03-23', '2018-03-26')
    3
    >>> date_diff('1945-01-03', '1945-01-28')
    25
    >>> date_diff('2020-03-01', '2020-02-25')
    -5

    '''

    date_one = datetime.strptime(first_date, "%Y-%m-%d")
    date_two = datetime.strptime(second_date, "%Y-%m-%d")

    return (date_two - date_one).days


def get_age(first_date, second_date):
    '''(str, str) -> int
    Returns how many complete years apart the 2 dates are.

    >>> get_age('2018-10-31', '2019-11-2')
    1
    >>> get_age('2018-10-31', '2000-11-2')
    -17
    >>> get_age('2001-03-26', '2019-03-27')
    18
    >>> get_age('2010-02-04', '2005-02-03')
    -5

    '''

    years_apart = date_diff(first_date, second_date) / 365.2425

    if years_apart > 0:
        return math.floor(years_apart)
    elif years_apart < 0:
        return math.ceil(years_apart)


def stage_three(open_file, write_file):
    '''(file, file) -> dictionary
    Replaces date of each record with date_diff of it and the index date, replaces date of \
    birth with age at index date, and replaces status with I, D, or R.

    >>> stage_three('short_stage_two.tsv', 'short_stage_three.tsv')
    {0: {'I': 1, 'D': 0, 'R': 0}, 1: {'I': 4, 'D': 0, 'R': 0}, 2: {'I': 9, 'D': 1, 'R': 0}}

    '''

    sick_folk = {}
    sick_folk[0] = {'I': 1, 'D': 0, 'R': 0}
    sick_num = 1
    rec_num = 0
    dead_num = 0

    to_read = open(open_file, 'r', encoding='utf-8')
    to_write = open(write_file, 'w', encoding='utf-8')

    first_line = to_read.readline().split()
    index_date = first_line[2]
    days_since_index = date_diff(index_date, first_line[2])
    current_age = get_age(first_line[3], index_date)
    first_line[2] = str(days_since_index)
    first_line[3] = str(current_age)

    final_string = ','.join(first_line)
    final_string = final_string.replace(which_delimiter(final_string), '\t')
    final_string += '\n'

    to_write.write(final_string)
    # I did this all outside of the for loop because I was having problems where the index date would just be \
    # the date in the 3rd column of every line, so I did the first line's iteration of this stage outside of \
    # the loop.

    lines_written = 1

    for line in to_read:
        line_split = line.split()

        days_since_index = date_diff(index_date, line_split[2])
        current_age = get_age(line_split[3], index_date)
        line_split[2] = str(days_since_index)
        line_split[3] = str(current_age)
        # These 4 lines get the values needed to replace the 3rd and 4th columns with, and replace them.

        if line_split[6].startswith('I'):
            line_split[6] = 'I'
            sick_num += 1
        elif line_split[6].startswith('D') or line_split[6].startswith('M'):
            line_split[6] = 'D'
            dead_num += 1
        elif line_split[6].startswith('R'):
            line_split[6] = 'R'
            rec_num += 1

        # Since Infected/Dead(Mort)/Recovered can be written/abbreviated in many ways, I just checked for the first \
        # letter, which is good enough for my data.

        lines_written += 1

        sick_folk[days_since_index] = {'I': sick_num, 'D': dead_num, 'R': rec_num}

        if 'NOT' in line_split[7]:
            line_split[7] = 'NOT APPLICABLE'
            del line_split[8]

        # I had a weird problem where NON/NOT APPLICABLE wouldn't combine into a 9 column string with this function, \
        # so I made this test function at the end that would solve it.

        final_string = ','.join(line_split)
        final_string = final_string.replace(which_delimiter(final_string), '\t')
        final_string += '\n'

        to_write.write(final_string)

    return sick_folk


def plot_time_series(d):
    ''' (dict of dict) -> list of lists
    Returns a list of list in the same format as the previous returned dict,
    and graphs the results.

    >>> d = stage_three('short_stage_two.tsv', 'short_stage_three.tsv')
    >>> plot_time_series(d)
    [[1, 0, 0], [4, 0, 0], [9, 1, 0]]

    '''

    threes_dictionary = stage_three('long_stage_two.tsv', 'long_stage_three.tsv')

    dict_keys = threes_dictionary.keys()

    dict_as_list = []

    for key in dict_keys:
        dict_as_list.append([threes_dictionary[key]['I'], threes_dictionary[key]['D'], threes_dictionary[key]['R']])

    plt.plot(dict_as_list)
    plt.xlabel('Days Into Pandemic')
    plt.ylabel('Number of People')
    plt.legend(['Infected', 'Dead', 'Recovered'])
    plt.title('Time series of early pandemic, by Davis Cover')
    plt.savefig('time_series.png')
    #plt.show()

    return dict_as_list


