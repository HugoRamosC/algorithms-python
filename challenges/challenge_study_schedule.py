def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0
    for student in permanence_period:
        is_true = (
            type(student) is tuple
            and type(student[0]) is int
            and type(student[1]) is int
        )
        # print('>>>>>>>>', type(student) is tuple)
        if not is_true:
            return None

        if student[0] <= target_time <= student[1]:
            count += 1

    return count
    # raise NotImplementedError


1, 3
4, 5
1, 5
