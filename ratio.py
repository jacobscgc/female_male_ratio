"""
Simple script to check the influence of male/female distribution in the input on the output.
"""

import random
from collections import Counter
import matplotlib.pyplot as plt


## FUNCTIONS ##


def create_employee_list(reps, input_choices):
    """
    Given a list of males / females available, choose at random a set of [reps] employees. The only important aspect of
    the input_choices is the ratio, where ['M', 'F'] has an equal ratio of males and females and ['M', 'M', 'F', 'F']
    also has an equal male / female ratio but ['M', 'M', 'F'] does not.

    It returns a list of employees that are either male of female.

    """
    employee_list = [random.choice(input_choices) for i in range(reps)]
    return employee_list


def create_employee_distributions(reps, input_choices):
    """
    This function creates a employee set of 1000 employees given a set of input_choices. It then calculates the
    percentage of women in the workflow for each created set (depending on reps). It returns a list of ratios
    (percentages of women in the workforce).

    """
    ratios = []
    for i in range(reps):
        employee_list = create_employee_list(1000, input_choices)
        counts = Counter(employee_list)
        ratio = counts['F'] / 1000
        ratios.append(ratio)
    return ratios


###############

data = create_employee_distributions(1000, ['M', 'M', 'M', 'M', 'M', 'M', 'F', 'F', 'F', 'F', 'F', 'F'])
plt.hist(data, bins=30, alpha=0.5, histtype='stepfilled', color='steelblue', edgecolor='none')
plt.xlim(xmin=0.1, xmax=0.6)
plt.title('Percentage of women when input ratio is 1:1 (M/F) and 12 candidates')
plt.show()


data = create_employee_distributions(1000, ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F', 'F', 'F', 'F'])
plt.hist(data, bins=30, alpha=0.5, histtype='stepfilled', color='steelblue', edgecolor='none')
plt.xlim(xmin=0.1, xmax=0.6)
plt.title('Percentage of women when input ratio is 2:1 (M/F) and 12 candidates')
plt.show()

data = create_employee_distributions(1000, ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F', 'F', 'F'])
plt.hist(data, bins=30, alpha=0.5, histtype='stepfilled', color='steelblue', edgecolor='none')
plt.xlim(xmin=0.1, xmax=0.6)
plt.title('Percentage of women when input ratio is 3:1 (M/F) and 12 candidates')
plt.show()

data = create_employee_distributions(1000, ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F', 'F'])
plt.hist(data, bins=30, alpha=0.5, histtype='stepfilled', color='steelblue', edgecolor='none')
plt.xlim(xmin=0.1, xmax=0.6)
plt.title('Percentage of women when input ratio is 5:1 (M/F) and 12 candidates')
plt.show()
