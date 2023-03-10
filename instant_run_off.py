# COMP 202 A3
# Name: Davis Cover
# ID: 260906663

from single_winner import *
import math

################################################################################


def votes_needed_to_win(ballots, num_winners):
    '''(list) -> int
    Returns the number of votes a candidate needs to win the election using the Droop Quota.

    >>> votes_needed_to_win([{'CPC':3, 'NDP':5}, {'NDP':2, 'CPC':4},{'CPC':3, 'NDP':5}], 1)
    2
    >>> votes_needed_to_win(['g']*20, 2)
    7
    >>> votes_needed_to_win([{'GREEN': 1, 'NDP': 2, 'LIBERAL':5}, {'NDP': 2, 'CPC': 4, 'LIBERAL': 6}], 2)
    1
    >>> votes_needed_to_win([{'GREEN': 1, 'LIBERAL': 3}, {'GREEN': 5, 'LIBERAL': 3}, {'GREEN': 1, 'LIBERAL': 2}, \
     {'GREEN': 5, 'LIBERAL': 5}], 1)
    3
    '''

    return math.floor(len(ballots)/(num_winners + 1)) + 1


def has_votes_needed(result, votes_needed):
    '''(dict) -> bool
    Returns if candidate has enough votes given by votes_needed from the results parameter.

     >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 4)
     True
     >>> has_votes_needed({'NDP': 5, 'LIBERAL': 5}, 4)
     True
     >>> has_votes_needed({'NDP': 2, 'LIBERAL': 1, 'GREEN':3}, 4)
     False
     >>> has_votes_needed({'NDP': 1, 'LIBERAL': 3}, 4)
     False
    '''

    highest = 0

    for item in result:
        if result[item] > highest:
            highest = result[item]

    return highest >= votes_needed


################################################################################


def eliminate_candidate(ballots, to_eliminate):
    '''(list) -> list
    Eliminates all candidates in to_eliminate from ballots.

     >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
     [[], ['GREEN'], ['BLOC']]
     >>> eliminate_candidate([['NDP', 'LIBERAL', 'GREEN'], ['GREEN', 'NDP', 'BLOC'], ['NDP', 'LIBERAL']], ['NDP'])
     [['LIBERAL', 'GREEN'], ['GREEN', 'BLOC'], ['LIBERAL']]
     >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'BLOC'], ['NDP', 'BLOC', 'LIBERAL']], ['NDP', 'LIBERAL', 'BLOC'])
     [[], ['GREEN'], []]
     >>> eliminate_candidate([['CPC', 'GREEN', 'NDP', 'LIBERAL'], ['LIBERAL'], ['LIBERAL', 'BLOC']], ['LIBERAL'])
     [['CPC', 'GREEN', 'NDP'], [], ['BLOC']]
    '''

    eliminated_list = []

    # Loops through each item in ballots and makes a new new_list each time.
    for item in ballots:
        new_list = []
        # Loops through each candidate, and if the candidate shouldn't be eliminated, it is added to new_list.
        for candidate in item:
            if candidate not in to_eliminate:
                new_list.append(candidate)
        eliminated_list.append(new_list)

    return eliminated_list


################################################################################


def count_irv(ballots):
    '''(list) -> dictionary
    Returns a dictionary displaying the final round of an IRV election based of ballots given.

    >>> pr_dict(count_irv([['NDP'], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL','NDP'], \
    ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], \
    ['BLOC', 'CPC'], ['LIBERAL', 'GREEN'], ['NDP']]))
    {'BLOC': 0, 'CPC': 0, 'GREEN': 0, 'LIBERAL': 3, 'NDP': 5}
    '''

    candidate_list = []

    # Initializes these two values in order to form a basis for the while loop.
    approval_ballots = count_first_choices(ballots)
    votes_to_win = votes_needed_to_win(ballots, 1)

    # While no candidate has votes needed to win, the first choices variable is initialized, \
    # the last place is added to candidate_list and is removed from ballots. Once ballots has \
    # the values in order to form a majority, the loop stops.
    while not has_votes_needed(approval_ballots, votes_to_win):
        approval_ballots = count_first_choices(ballots)
        candidate_list.append(last_place(approval_ballots))
        ballots = eliminate_candidate(ballots, candidate_list)

    # This goes through all the candidates other than the top 2, and adds them with a value of 0 to \
    # approval ballots.
    for loser in candidate_list:
        if loser not in approval_ballots:
            approval_ballots[loser] = 0

    return approval_ballots




################################################################################

if __name__ == '__main__':
    doctest.testmod()
