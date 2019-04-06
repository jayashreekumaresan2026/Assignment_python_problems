# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?h_r=internal-search
def beautiful_days_at_movie(starting_day, ending_day, divisor):
    count = 0
    for i in range(starting_day, ending_day+1):
        reversed_number = str(i)[::-1]
        if (i - int(reversed_number)) % divisor == 0:
            count = count + 1
    print(count)


starting_day = 20
ending_day = 23
divisor = 6
beautiful_days_at_movie(starting_day, ending_day, divisor)

