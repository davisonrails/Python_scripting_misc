# Davis Cover
# 260906663


def which_delimiter(str):
    ''''(str) -> str
    Returns the most commonly used delimiter in the string.
    >>> which_delimiter('0 1 2,3')
    ' '
    >>> which_delimiter('\\t1\\t2,3 5')
    '\\t'
    >>> which_delimiter('0,1, 2\\t3')
    ','
    >>> which_delimiter('0,1 2\\t3\\t')
    '\\t'

    '''

    comma_count = str.count(',')
    space_count = str.count(' ')
    tab_count = str.count('\t')

    if space_count == 0 and comma_count == 0 and tab_count == 0:
        raise AssertionError

    most = ''

    if space_count > tab_count and space_count > comma_count:
        most = ' '
    elif tab_count > space_count and tab_count > comma_count:
        most = '\t'
    else:
        most = ','

    return most


def stage_one(open_file, write_file):
    '''(file, file) -> int
    Changes most common delimiter to tab, capitalizes all text, and changes all '/' and '.' to a hyphen in the new file.
    Then, the amount of lines written is returned.

    >>> stage_one('short_file.txt', 'short_stage_one.tsv')
    10
    >>> stage_one('long_file.txt', 'long_stage_one.tsv')
    3000

    '''

    to_read = open(open_file, 'r', encoding='utf-8')
    to_write = open(write_file, 'w', encoding='utf-8')

    strings_written = 0

    for line in to_read:
        upper_line = line.upper()
        this_without_slash = upper_line.replace('/', '-')
        this_delimited = this_without_slash.replace(which_delimiter(this_without_slash), '\t')
        split_line = this_delimited.split()

        for i in range(len(split_line)):
            if i < 6:
                split_line[i] = split_line[i].replace('.', '-')
                # This is so that a - is not put in temperatures, so it stops at the column where the temperatures \
                # are located.

        final_string = ','.join(split_line)
        final_string = final_string.replace(which_delimiter(final_string), '\t')
        final_string += '\n'
        # I could've made these 3 lines above a helper function, which makes my split list into one string again, but \
        # I got pretty deep into this assignment doing it like this, and making a whole helper function would've \
        # caused more headache than it would've solved.

        strings_written += 1

        to_write.write(final_string)

    return strings_written


def contains_digits(str):
    '''(str) -> bool
    Returns whether or not the string contains any digits to be used in stage 2.
    This function is used to differentiate between postal codes and non-postal codes to clean up the data.

    >>> contains_digits('h3a')
    True
    >>> contains_digits('2b0')
    True
    >>> contains_digits('abc')
    False
    >>> contains_digits('ghiowjaf4aklfwaf')
    True

    '''

    count = 0
    for i in range(len(str)):
        if str[i].isdigit():
            count += 1
        else:
            continue

    if count > 0:
        return True
    else:
        return False


def stage_two(open_file, write_file):
    '''(file, file) -> int
    Changes most common delimiter to tab, capitalizes all text, and changes all '/' and '.' to a hyphen in the new file.
    Then, the amount of lines written is returned.

    >>> stage_two('short_stage_one.tsv', 'short_stage_two.tsv')
    10
    >>> stage_two('long_stage_one.tsv', 'long_stage_two.tsv')
    3000

    '''

    to_read = open(open_file, 'r', encoding='utf-8')
    to_write = open(write_file, 'w', encoding='utf-8')

    temp_sixth = ''
    temp_eighth = ''
    final_string = ''
    strings_written = 0

    for line in to_read:
        temp_string = line.split()

        if len(temp_string) > 9:
            # This if statement goes into the process of changing all values that make the column count > 9.
            for i in range(len(temp_string[6])):
                maybe_code = temp_string[6]
                if contains_digits(maybe_code):
                    temp_sixth = temp_string[5] + temp_string[6]
                    temp_string[5] = temp_sixth
                    del temp_string[6]
                    # This if statement combines the 2 portions of the postal code
            if 'NOT' in temp_string[7] or 'NON' in temp_string[7]:
                temp_eighth = temp_string[7] + ' ' + temp_string[8]
                temp_string[7] = temp_eighth
                del temp_string[8]
                # This if statement combines 'NON APPLICABLE/ NOT APPLICABLE' which is in multiple columns of my \
                # split line.
            elif len(temp_string) == 10:
                if contains_digits(temp_string[7]):
                    temp_eighth = temp_string[7] +  temp_string[8]
                    temp_string[7] = temp_eighth
                    del temp_string[8]
                    # This if statement would combine a 40\t35 temp to be 40.35
                else:
                    temp_eighth = temp_string[7] + temp_string[8]
                    temp_string[7] = temp_eighth
                    del temp_string[8]
                    # This if statement would combine a 40\tC temp to be 40C
            elif len(temp_string) == 11:
                temp_eighth = temp_string[7] + '.' + temp_string[8] + temp_string[9]
                temp_string[7] = temp_eighth
                del temp_string[8]
                del temp_string[8]
                # This if statement would combine a 40\t35\tC temp to be 40.35C

            final_string = '|'.join(temp_string)
            final_string = final_string.replace('|', '\t')
            final_string += '\n'
            to_write.write(final_string)
        else:
            to_write.write(line)
            # This executes when the columns are already correct.

        strings_written += 1

    return strings_written






