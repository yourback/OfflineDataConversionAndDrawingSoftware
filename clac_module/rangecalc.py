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
        "integral": integral_range_values(base_data),
    }


def integral_range_values(list_data):
    result = 0
    for index, data in enumerate(list_data):
        # 如果是第一项不做处理
        if index == 0:
            continue
        else:
            # 如果不是第一项，则这个小面积为 (data - list_data[index-1]) /2
            result += (data + list_data[index - 1]) / 2
            # print('结果：%s' % )
    return round(result, 3)
