def study_schedule(permanence_period, target_time):
    # [(1, 3), (2, 5), (1, 4)]
    hours_dict = {}

    if(target_time == None or not isinstance(permanence_period, list)): return None
    for student in permanence_period:
        if(not isinstance(student, tuple)): return None
        if(type(student[0]) != int or type(student[1]) != int): return None
        hour = student[0]
        while hour <= student[1]:
            if(hour not in hours_dict):
                hours_dict[hour] = 1
                hour += 1
            else:
                hours_dict[hour] += 1
                hour += 1



        # for hour in range(student[0], student[1] + 1):
    return hours_dict.get(target_time, None)
    # raise NotImplementedError
