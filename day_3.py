import statistics

def get_rating(ratings, default_to_keep):

    for i in range(0, len(ratings[0])):
        filter_on = default_to_keep if statistics.mean([int(val[i]) for val in ratings]) >= 0.5 else default_to_keep^1
        ratings = [rating for rating in ratings if int(rating[i]) == filter_on]

        if len(ratings) == 1:
            return(ratings[0])


with open("day-3.txt", "r") as input:
    measurements = input.read().split("\n")
    length = len(measurements[0])

    measurements_list = [int(val) for measurement in measurements for val in measurement]
  
    gamma = ''
    epsilon = ''

    for i in range(0, length):
        mcv = statistics.mean(measurements_list[i::length]) > 0.5

        gamma += '1' if mcv > 0.5 else '0'
        epsilon += '1' if mcv < 0.5 else '0'

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print("Part 1: ", epsilon * gamma)

    ox_rating = get_rating(measurements, 1)
    co_rating = get_rating(measurements, 0)

    print("Part 2:")
    print(ox_rating, co_rating)
    print(int(ox_rating, 2) * int(co_rating, 2))






