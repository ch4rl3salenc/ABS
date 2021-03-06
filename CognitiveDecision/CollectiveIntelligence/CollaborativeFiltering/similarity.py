#! python3
# ways to represent different people
# and their preferences
from math import sqrt


# ecludean's distance score
# return a distance-based similarity score for 2 people
# movies will be the axes
# people will be the points
def sim_distance(prefs, person1, person2):
    # shared item
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:
        return 0
    # add the square of all differences
    sum_of_squares = sum([
        pow(prefs[person1][item] - prefs[person2][item], 2)
        for item in prefs[person1] if item in prefs[person2]
    ])
    # to make result is between 0 and 1
    # compare result with 1 (divide by 1)
    # to avoid divide by 0, add 1 to the sqrt(result) above
    return 1 / (1 + sqrt(sum_of_squares))


# Pearson Correlation Score
# Correlation Coefficient is a measure of how well
# two sets of data fit on a straight line
# people will be the axes
# movies will be the points
# more: https://youtu.be/ugd4k3dC_8Y
# score varies based on x-scatter/y-scatter
# Pearson Correlation Coefficient r
# r = (nSum(xy) - Sum(x)Sum(y))/(sqrt(nSum(x**2)-Sum(x)**2).sqrt(nSum(y**2)-Sum(y)**2))
# where n is the number of sample
# x = xi (i = 0, 1 ..)
# y = yi (i = 0, 1 ..)
def sim_pearson(prefs, p1, p2):
    # get the list of mutually rated item
    similar = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            similar[item] = 1

    n = len(similar)
    if n == 0:
        return 0

    # add all preference, Sum(x) Sum(y)
    sumx = sum([prefs[p1][it] for it in similar])
    sumy = sum([prefs[p2][it] for it in similar])

    # Sum(x**2) Sum(y**2)
    sumx_sqr = sum([pow(prefs[p1][it], 2) for it in similar])
    sumy_sqr = sum([pow(prefs[p2][it], 2) for it in similar])

    # Sum(xy)
    sumxy = sum([prefs[p1][it] * prefs[p2][it] for it in similar])

    # score
    num = n * sumxy - sumx * sumy
    den = (sqrt(n * sumx_sqr - sumx ** 2)) * (sqrt(n * sumy_sqr - sumy ** 2))
    if den == 0:
        return 0
    return num / den

