def timespliting(user_input):
    time_list=[]
    year=user_input.index("y")
    extract_the_year=user_input[:year]
    time_list.append(extract_the_year)
    hour = user_input.index("h")
    extract_the_hour = user_input[len(extract_the_year)+1:hour]
    time_list.append(extract_the_hour)
    mini = user_input.index("m")
    extract_the_min = user_input[len(extract_the_year)+1+len(extract_the_hour)+1:mini]
    time_list.append(extract_the_min)
    sec = user_input.index("s")
    extract_the_year = user_input[len(extract_the_min)+1+len(extract_the_year)+1+len(extract_the_hour)+1:sec]
    time_list.append(extract_the_year)
    print(time_list)
user_input='0y0h0m1s'
timespliting(user_input)
