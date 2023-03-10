# COMP 202 A3
# Name: Davis Cover
# Student ID: 260906663

from instant_run_off import *

################################################################################


def irv_to_stv_ballot(ballots, num_winners):
    '''(list) -> list
    Returns every party in ballots the number of times designated by num_winners listed after the party name.

    >>> irv_to_stv_ballot([['NDP', 'CPC'], ['GREEN']], 3)
    [['NDP0', 'NDP1', 'NDP2', 'CPC0', 'CPC1', 'CPC2'], ['GREEN0', 'GREEN1', 'GREEN2']]
    >>> irv_to_stv_ballot([['NDP', 'CPC', 'LIBERAL'], ['GREEN', 'CPC']], 2)
    [['NDP0', 'NDP1', 'CPC0', 'CPC1', 'LIBERAL0', 'LIBERAL1'], ['GREEN0', 'GREEN1', 'CPC0', 'CPC1']]
    >>> irv_to_stv_ballot([['NDP'], ['CPC']], 5)
    [['NDP0', 'NDP1', 'NDP2', 'NDP3', 'NDP4'], ['CPC0', 'CPC1', 'CPC2', 'CPC3', 'CPC4']]
    >>> irv_to_stv_ballot([['CPC'], ['GREEN', 'NDP']], 4)
    [['CPC0', 'CPC1', 'CPC2', 'CPC3'], ['GREEN0', 'GREEN1', 'GREEN2', 'GREEN3', 'NDP0', 'NDP1', 'NDP2', 'NDP3']]

    '''

    final_list = []

    # Creates a list that prints party + number 0..num_winners-1
    for item in ballots:
        current_list = []
        for sublist in item:
            for i in range(num_winners):
                current_list.append(sublist + str(i))
        # Once the list with party + number 0...num_winners -1 is made, it is appended to final_list
        final_list.append(current_list)

    return final_list


################################################################################


def eliminate_n_ballots_for(ballots, to_eliminate, n):
    '''(lst, str) -> lst
    Remove n of the ballots in ballots where the first choice is for the candidate to_eliminate.

    Provided to students. Do not edit.

    >>> ballots = [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 2)
    [['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3', 'GREEN1'], 5)
    [['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> b = [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    >>> eliminate_n_ballots_for(b, ['GREEN1'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    '''
    quota = n
    new_ballots = []
    elims = 0
    for i,b in enumerate(ballots):
        if (elims >= quota) or  (len(b) > 0 and b[0] not in to_eliminate):
            new_ballots.append(b)
        else:
            elims += 1
    return new_ballots


def stv_vote_results(ballots, num_winners):
    '''(lst of list, int) -> dict

    From the ballots, elect num_winners many candidates using Single-Transferable Vote
    with Droop Quota. Return how many votes each candidate has at the end of all transfers.
    
    Provided to students. Do not edit.

    >>> random.seed(3) # make the random tie-break consistent
    >>> g = ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1']
    >>> n = ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 2, 'NDP3': 0}
    >>> random.seed(1)
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 0, 'NDP3': 0}
    >>> green = ['GREEN', 'NDP', 'BLOC', 'LIBERAL', 'CPC']
    >>> ndp = ['NDP', 'GREEN', 'BLOC', 'LIBERAL', 'CPC']
    >>> liberal = ['LIBERAL', 'CPC', 'GREEN', 'NDP', 'BLOC']
    >>> cpc = ['CPC', 'NDP', 'LIBERAL', 'BLOC', 'GREEN']
    >>> bloc = ['BLOC', 'NDP', 'GREEN', 'CPC', 'LIBERAL']
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 2))
    {'BLOC': 32, 'CPC': 34, 'GREEN': 0, 'LIBERAL': 0, 'NDP': 34}
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 3))
    {'BLOC': 26, 'CPC': 26, 'GREEN': 0, 'LIBERAL': 22, 'NDP': 26}
    '''
    quota = votes_needed_to_win(ballots, num_winners)

    to_eliminate = []
    result = {}
    final_result = {}

    for i in range(num_winners):
        # start off with quasi-IRV

        result = count_first_choices(ballots)

        while (not has_votes_needed(result, quota)) and len(result) > 0:
            to_eliminate.append( last_place(result) ) 
            ballots = eliminate_candidate(ballots, to_eliminate)
            result = count_first_choices(ballots)

        # but now with the winner, reallocate ballots above quota and keep going
        winner = get_winner(result)
        if winner:
            final_result[winner] = quota # winner only needs quota many votes
            ballots = eliminate_n_ballots_for(ballots, final_result.keys(), quota)
            ballots = eliminate_candidate(ballots, final_result.keys())
            result = count_first_choices(ballots)

    # remember the candidates we eliminated, their count should be 0
    for candidate in to_eliminate:
        final_result[candidate] = 0
    final_result.update(result)
    return final_result


################################################################################


def count_stv(ballots, num_winners):
    '''(list) -> dictionary
    Returns a list of parties and how many winners each party had depending on the results of \
    the STV election.

    >>> random.seed(3)
    >>> g = ['GREEN', 'NDP', 'BLOC']
    >>> n = ['NDP', 'GREEN', 'BLOC']
    >>> pr_dict(count_stv([g]*5 + [n]*3, 4))
    {'BLOC': 0, 'GREEN': 3, 'NDP': 1}
    '''

    # Initializes values needed for the for loops.
    converted_stv = irv_to_stv_ballot(ballots, num_winners)
    stv_counted = stv_vote_results(converted_stv, num_winners)
    all_candidates = get_all_candidates(ballots)

    winners_list = []

    # Loops through all elements in stv_counted to append all elements with equal to or more votes than needed. \
    # It appends all of the winners to the winners_list.
    for item in stv_counted:
        if stv_counted[item] >= votes_needed_to_win(converted_stv, num_winners):
            winners_list.append(item)

    party_winners_list = []

    # This takes all of the winners, sorts them by party, and adds each party to the party_winners_list.
    for candidate in winners_list:
        word_minus_number = ''
        for char in range(len(candidate)-1):
            word_minus_number += candidate[char]
        party_winners_list.append(word_minus_number)

    # This counts how many winners each party has.
    party_plurality = count_plurality(party_winners_list)

    # This adds all parties that didn't win any seats to party_plurality and assigns the values of them to 0.
    for cand in all_candidates:
        if cand not in party_plurality:
            party_plurality[cand] = 0

    return party_plurality


################################################################################


def count_SL(results, num_winners):
    '''(list) -> dictionary
    Returns the electoral results of a Saint-Laguë election from results and num_winners.

    >>> pr_dict(count_SL(['A'] * 10 + ['B'] * 8 + ['C'] * 3 + ['D'] * 2, 8))
    {'A': 3, 'B': 3, 'C': 1, 'D': 1}
    '''

    # Initializes all values needed to start the for loops below.
    all_candidates = get_all_candidates(results)
    votes = count_plurality(results)
    winners = {}
    divisor = {}

    # Assigns
    for item in all_candidates:
        winners[item] = 0
        divisor[item] = 0

    for i in range(num_winners):
        for cand in all_candidates:
            divisor[cand] = votes[cand]/((2 * winners[cand]) + 1)
        winners[get_winner(divisor)] += 1

    return winners


################################################################################


if __name__ == '__main__':
    doctest.testmod()
