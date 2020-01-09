# 区间数据计算
# 获取最小值

def max_calc(list_data):
    i = list_data[0]
    for d in list_data:
        if i < d:
            i = d
    return i


def min_calc(list_data):
    i = list_data[0]
    for d in list_data:
        if i > d:
            i = d
    return i


def average_calc(list_data):
    i = 0
    for d in list_data:
        i += round(d, 2)
    return round(i / len(list_data), 2)


def max_min(list_data):
    return round(max_calc(list_data) - min_calc(list_data), 2)


def get_range_values(base_data):
    return {
        "max": max_calc(base_data),
        "min": min_calc(base_data),
        "diff": max_min(base_data),
        "average": average_calc(base_data),
    }
