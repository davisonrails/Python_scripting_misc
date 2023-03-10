# Davis Cover
# 260906663


class Patient:
    def __init__(self, num, day_diagnosed, age, sex_gender, postal, state, temps, days_symptomatic):
        self.num = num
        self.day_diagnosed = day_diagnosed
        self.age = age

        if sex_gender.startswith('M') or sex_gender.startswith('H') or sex_gender.startswith('B'):
            self.sex_gender = 'M'
        elif sex_gender.startswith('F') or sex_gender.startswith('G') or sex_gender.startswith('W'):
            self.sex_gender = 'F'
        else:
            self.sex_gender = 'X'

        self.postal = postal[:3]
        self.state = state

        temps = temps.replace(',', '.')
        temps = temps.replace('C', '')
        temps = temps.replace('F', '')
        temps = temps.replace('°', '')
        # first cuts out any of the 45,6F or 32,1C occurrences to just be 1 float value.

        if float(temps) > 45.0:
            self.temps = round((float(temps) - 32) * 5 / 9, 2)
        else:
            self.temps = temps

        self.days_symptomatic = days_symptomatic

    def __str__(self):
        '''(object) -> list
        Prints out the objects in the order requested.

        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102,2', '12')
        >>> str(p)
        '0\\t42\\tF\\tH3Z\\t0\\tI\\t12\\t39.0'

        '''
        string_to_print = ''
        string_to_print += self.num + '\t'
        string_to_print += self.age + '\t'
        string_to_print += self.sex_gender + '\t'
        string_to_print += self.postal + '\t'
        string_to_print += self.day_diagnosed + '\t'
        string_to_print += self.state + '\t'
        string_to_print += self.days_symptomatic + '\t'
        string_to_print += str(self.temps)

        return string_to_print

    def update(self, other_obj):
        '''(Patient obj, Patient obj) -> Patient obj
        Updates self with temps, state, and days_symptomatic of other_obj if they're the same person. If not, an \
        AssertionError is raised.

        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> p1 = Patient('0', '1', '42', 'F', 'H3Z', 'D', '40,0 C', '13')
        >>> p.update(p1)
        >>> str(p)
        '0\\t42\\tF\\tH3Z\\t0\\tD\\t13\\t39.0;40.0 '

        '''
        if self.num == other_obj.num and self.sex_gender == other_obj.sex_gender and self.postal == other_obj.postal:
            self.days_symptomatic = other_obj.days_symptomatic
            self.state = other_obj.state
            self.temps = str(self.temps) + ';' + other_obj.temps
            # My temps initializes as a float, so I convert to string in order to concatenate it.
        else:
            raise AssertionError


def stage_four(open_file, write_file):
    '''(file, file) -> dictionary

    >>> p = stage_four('short_stage_three.tsv', 'short_stage_four.tsv')
    >>> print(str(p))
    '0\\t42\\tF\\tH3Z\\t0\\tI\\t12\\t40.0;39.13;39.45;39.5;39.36;39.2;39.0;39.04;38.82;37.7'

    '''

    to_read = open(open_file, 'r', encoding='utf-8')
    to_write = open(write_file, 'w', encoding='utf-8')
    patients_dict = {}

    first_line = to_read.readline().split()

    first_num = first_line[1]
    first_day_diagnosed = first_line[2]
    first_age = first_line[3]
    first_sex = first_line[4]
    first_postal = first_line[5]
    first_state = first_line[6]
    first_temps = first_line[7]
    first_dayssick = first_line[8]

    patient_zero = Patient(first_num, first_day_diagnosed, first_age, first_sex, first_postal, first_state, \
    first_temps, first_dayssick)

#    return patient_zero

    previous_patient = patient_zero

    for line in to_read:

        this_line = line.split()
        this_num = this_line[1]
        this_day_diagnosed = this_line[2]
        this_age = this_line[3]
        this_sex = this_line[4]
        this_postal = this_line[5]
        this_state = this_line[6]
        this_temps = this_line[7]
        this_dayssick = this_line[8]

        this_patient = Patient(this_num, this_day_diagnosed, this_age, this_sex, this_postal, this_state, \
        this_temps, this_dayssick)

        if this_patient.num == previous_patient.num and this_patient.sex_gender == previous_patient.sex_gender and \
        this_patient.postal == previous_patient.postal:
            this_patient.temps = this_patient.temps + ';' + previous_patient.temps
            previous_patient = Patient(this_num, this_day_diagnosed, this_age, this_sex, this_postal, this_state, \
            this_temps, this_dayssick)
        else:
            patients_dict[this_num] = str(this_patient)
            previous_patient = Patient(this_num, this_day_diagnosed, this_age, this_sex, this_postal, this_state, \
            this_temps, this_dayssick)

    to_write.write(str(patients_dict) + '\n')

    return patients_dict





    #patients_keys = sorted(patients_dict)

    #sorted_patient_dict = {}

    #for key in patients_keys:
    #    sorted_patient_dict[key] = patients_dict[key]
    #    to_write.write(sorted_patient_dict[key] + '\n')









