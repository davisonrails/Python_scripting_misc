# COMP 202 A3
# Name: Davis Cover
# Student ID: 260906663

from a3_helpers import *


def count_plurality(ballots):
    '''(list) -> dictionary
    Returns a dictionary of how many votes each candidate in the list received.

    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL'])
    {'LIBERAL': 3, 'NDP': 1}
    >>> count_plurality(['LIBERAL', 'NDP', 'NDP', 'CPC'])
    {'LIBERAL': 1, 'NDP': 2, 'CPC': 1}
    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL', 'CONSERVATIVE', 'CONSERVATIVE'])
    {'LIBERAL': 3, 'NDP': 1, 'CONSERVATIVE': 2}
    >>> count_plurality(['LIBERAL', 'CPC', 'NDP', 'GREEN'])
    {'LIBERAL': 1, 'CPC': 1, 'NDP': 1, 'GREEN': 1}
    '''

    ballot_dict = {}

    for i in range(len(ballots)):
        ballot_dict[ballots[i]] = ballots.count(ballots[i])

    return ballot_dict

    
def count_approval(ballots):
    '''(list) -> dictionary
    Returns a dictionary of how many approval votes each candidate got.

    >>> count_approval([ ['LIBERAL', 'NDP'], ['NDP'], ['NDP', 'GREEN', 'BLOC']] )
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    >>> count_approval([ ['LIBERAL', 'BLOC', 'CPC'], ['BLOC', 'NDP'], ['LIBERAL']] )
    {'LIBERAL': 2, 'BLOC': 2, 'CPC': 1, 'NDP': 1}
    >>> count_approval([ ['GREEN', 'NDP'], ['NDP', 'LIBERAL'], ['NDP', 'BLOC']] )
    {'GREEN': 1, 'NDP': 3, 'LIBERAL': 1, 'BLOC': 1}
    >>> count_approval([ ['LIBERAL', 'GREEN', 'BLOC'], ['NDP', 'GREEN', 'BLOC']] )
    {'LIBERAL': 1, 'GREEN': 2, 'BLOC': 2, 'NDP': 1}
    '''

    flattened_list = flatten_lists(ballots)

    return count_plurality(flattened_list)


def count_rated(ballots):
    '''(list) -> dictionary
    Returns a dictionary of the summed-up scores given to each candidate by each ballot.

    >>> count_rated([{'LIBERAL': 5, 'NDP':2}, {'NDP':4, 'GREEN':5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}
    >>> count_rated([{'LIBERAL': 12, 'GREEN':7}, {'NDP':4, 'GREEN':5}])
    {'GREEN': 12, 'LIBERAL': 12, 'NDP': 4}
    >>> count_rated([{'CPC': 0, 'NDP':2}, {'CPC':1, 'GREEN':9}])
    {'NDP': 2, 'CPC': 1, 'GREEN': 9}
    >>> count_rated([{'LIBERAL': 2, 'NDP':2, 'GREEN': 6}, {'CPC':1}])
    {'GREEN': 6, 'LIBERAL': 2, 'NDP': 2, 'CPC': 1}
    '''

    rated_list = []

    for item in ballots:
        rated_list.append(flatten_dict(item))

    rated_list = count_approval(rated_list)

    return rated_list


def count_first_choices(ballots):
    '''(list) -> dictionary
    Returns a dictionary containing the amount of times a candidate was ranked first.

    >>> count_first_choices([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']])
    {'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0}
    >>> count_first_choices([['NDP', 'LIBERAL'], ['NDP', 'GREEN', 'LIBERAL'], ['BLOC', 'NDP', 'LIBERAL']])
    {'NDP': 2, 'BLOC': 1, 'LIBERAL': 0, 'GREEN': 0}
    >>> count_first_choices([['LIBERAL', 'NDP', 'GREEN'], ['BLOC', 'NDP'], ['NDP', 'BLOC', 'LIBERAL', 'GREEN']])
    {'LIBERAL': 1, 'BLOC': 1, 'NDP': 1, 'GREEN': 0}
    >>> count_first_choices([['CONSERVATIVE', 'CPC', 'BLOC'], ['GREEN', 'NDP', 'BLOC'], ['NDP', 'GREEN', 'LIBERAL']])
    {'CONSERVATIVE': 1, 'GREEN': 1, 'NDP': 1, 'CPC': 0, 'BLOC': 0, 'LIBERAL': 0}
    '''

    first_list = []
    not_first = []

    # Loops through each list in ballots and appends the first item to first_list, and every other item to not_first.
    for item in ballots:
        if item != []:
            first_list.append(item[0])
            for i in range(len(item)-1):
                not_first.append(item[i+1])

    # Counts the amount of times each candidate in first_list appears.
    first_choice = count_plurality(first_list)

    # Loops through all the losers, and if they were never anyone's first choice, 0 is assigned to them in the list.
    for loser in not_first:
        if loser not in first_list:
            first_choice[loser] = 0

    return first_choice



if __name__ == '__main__':
    doctest.testmod()
